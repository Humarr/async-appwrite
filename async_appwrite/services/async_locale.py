from ..async_service import AsyncService
from appwrite.exception import AppwriteException
from ..async_client import AsyncClient


class AsyncLocale(AsyncService):

    def __init__(self, client: AsyncClient):
        super(AsyncLocale, self).__init__(client)

    async def get(self):
        """Get user locale"""

        api_path = "/locale"
        api_params = {}

        return await self.client.call(
            "get",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def list_codes(self):
        """List Locale Codes"""

        api_path = "/locale/codes"
        api_params = {}

        return await self.client.call(
            "get",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def list_continents(self):
        """List continents"""

        api_path = "/locale/continents"
        api_params = {}

        return await self.client.call(
            "get",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def list_countries(self):
        """List countries"""

        api_path = "/locale/countries"
        api_params = {}

        return await self.client.call(
            "get",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def list_countries_eu(self):
        """List EU countries"""

        api_path = "/locale/countries/eu"
        api_params = {}

        return await self.client.call(
            "get",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def list_countries_phones(self):
        """List countries phone codes"""

        api_path = "/locale/countries/phones"
        api_params = {}

        return await self.client.call(
            "get",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def list_currencies(self):
        """List currencies"""

        api_path = "/locale/currencies"
        api_params = {}

        return await self.client.call(
            "get",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def list_languages(self):
        """List languages"""

        api_path = "/locale/languages"
        api_params = {}

        return await self.client.call(
            "get",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )
