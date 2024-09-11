from async_appwrite.async_client import AsyncClient
from async_appwrite.services.async_account import AsyncAccount
import asyncio

client = AsyncClient()
client.set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

account = AsyncAccount(client)

result = account.create_jwt()

async def create_jwt(account):
    await account.create_jwt()

asyncio.run(create_jwt())