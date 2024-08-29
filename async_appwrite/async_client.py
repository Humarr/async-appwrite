import io
import httpx
import json
import os
from appwrite.input_file import InputFile
from appwrite.exception import AppwriteException
from appwrite.encoders.value_class_encoder import ValueClassEncoder

from typing import Dict, Optional, Any
from appwrite.client import Client  # Import the original Client class


class AsyncClient(Client):  # Inherit from the original Client class
    def __init__(self):
        super().__init__()  # Call the parent constructor

    async def call(
        self,
        method: str,
        path: str = "",
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        response_type: str = "json",
    ) -> Any:
        if headers is None:
            headers = {}

        if params is None:
            params = {}

        params = {
            k: v for k, v in params.items() if v is not None
        }  # Remove None values from params dictionary

        data = {}
        files = {}
        stringify = False

        headers = {**self._global_headers, **headers}

        if method.lower() != "get":
            data = params
            params = {}

        if headers.get("content-type", "").startswith("application/json"):
            data = json.dumps(data, cls=ValueClassEncoder)

        if headers.get("content-type", "").startswith("multipart/form-data"):
            del headers["content-type"]
            stringify = True
            for key in list(data.keys()):
                if isinstance(data[key], InputFile):
                    files[key] = (data[key].filename, data[key].data)
                    del data[key]
            data = self.flatten(data, stringify=stringify)

        async with httpx.AsyncClient(
            timeout=30.0, verify=(not self._self_signed)
        ) as client:
            try:
                response = await client.request(
                    method=method,
                    url=self._endpoint + path,
                    params=self.flatten(params, stringify=stringify),
                    data=data,
                    files=files,
                    headers=headers,
                    follow_redirects=False if response_type == "location" else True,
                )

                response.raise_for_status()

                content_type = response.headers.get("Content-Type", "")

                if response_type == "location":
                    return response.headers.get("Location")

                if content_type.startswith("application/json"):
                    return response.json()

                return response.content
            except httpx.HTTPStatusError as e:
                content_type = e.response.headers.get("Content-Type", "")
                if content_type.startswith("application/json"):
                    raise AppwriteException(
                        e.response.json().get("message"),
                        e.response.status_code,
                        e.response.json().get("type"),
                        e.response.json(),
                    )
                else:
                    raise AppwriteException(e.response.text, e.response.status_code)
            except Exception as e:
                raise AppwriteException(e)

    async def chunked_upload(
        self,
        path,
        headers=None,
        params=None,
        param_name="",
        on_progress=None,
        upload_id="",
    ):
        input_file = params[param_name]

        if input_file.source_type == "path":
            size = os.stat(input_file.path).st_size
            input = open(input_file.path, "rb")
        elif input_file.source_type == "bytes":
            size = len(input_file.data)
            input = io.BytesIO(input_file.data)

        if size < self._chunk_size:
            if input_file.source_type == "path":
                input_file.data = input.read()

            params[param_name] = input_file
            return await self.call("post", path, headers, params)

        offset = 0
        counter = 0

        if upload_id != "unique()":
            try:
                result = await self.call("get", path + "/" + upload_id, headers)
                counter = result["chunksUploaded"]
            except:
                pass

        if counter > 0:
            offset = counter * self._chunk_size
            input.seek(offset)

        while offset < size:
            if input_file.source_type == "path":
                input_file.data = input.read(self._chunk_size) or input.read(
                    size - offset
                )
            elif input_file.source_type == "bytes":
                if offset + self._chunk_size < size:
                    end = offset + self._chunk_size
                else:
                    end = size - offset
                input_file.data = input[offset:end]

            params[param_name] = input_file
            headers["content-range"] = (
                f"bytes {offset}-{min((offset + self._chunk_size) - 1, size - 1)}/{size}"
            )

            result = await self.call(
                "post",
                path,
                headers,
                params,
            )

            offset = offset + self._chunk_size

            if "$id" in result:
                headers["x-appwrite-id"] = result["$id"]

            if on_progress is not None:
                end = min(
                    (((counter * self._chunk_size) + self._chunk_size) - 1), size - 1
                )
                on_progress(
                    {
                        "$id": result["$id"],
                        "progress": min(offset, size) / size * 100,
                        "sizeUploaded": end + 1,
                        "chunksTotal": result["chunksTotal"],
                        "chunksUploaded": result["chunksUploaded"],
                    }
                )

            counter = counter + 1

        return result

    def flatten(self, data, prefix="", stringify=False):
        output = {}
        i = 0

        for key in data:
            value = data[key] if isinstance(data, dict) else key
            finalKey = prefix + "[" + key + "]" if prefix else key
            finalKey = (
                prefix + "[" + str(i) + "]" if isinstance(data, list) else finalKey
            )
            i += 1

            if isinstance(value, list) or isinstance(value, dict):
                output = {**output, **self.flatten(value, finalKey, stringify)}
            else:
                if stringify:
                    output[finalKey] = str(value)
                else:
                    output[finalKey] = value

        return output
