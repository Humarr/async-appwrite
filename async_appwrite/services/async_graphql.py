from ..async_service import AsyncService
from appwrite.exception import AppwriteException
from ..async_client import AsyncClient


class AsyncGraphql(AsyncService):

    def __init__(self, client: AsyncClient):
        super(AsyncGraphql, self).__init__(client)

    async def query(self, query):
        """GraphQL endpoint"""

        api_path = "/graphql"
        api_params = {}
        if query is None:
            raise AppwriteException('Missing required parameter: "query"')

        api_params["query"] = query

        return await self.client.call(
            "post",
            api_path,
            {
                "x-sdk-graphql": "true",
                "content-type": "application/json",
            },
            api_params,
        )

    async def mutation(self, query):
        """GraphQL endpoint"""

        api_path = "/graphql/mutation"
        api_params = {}
        if query is None:
            raise AppwriteException('Missing required parameter: "query"')

        api_params["query"] = query

        return await self.client.call(
            "post",
            api_path,
            {
                "x-sdk-graphql": "true",
                "content-type": "application/json",
            },
            api_params,
        )
