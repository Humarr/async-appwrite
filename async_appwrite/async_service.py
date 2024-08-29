from .async_client import AsyncClient
from appwrite.service import Service


class AsyncService(Service):
    def __init__(self, client: AsyncClient):
        self.client = client
