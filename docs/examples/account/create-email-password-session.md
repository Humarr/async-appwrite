from async_appwrite.async_client import AsyncClient
from async_appwrite.services.async_account import AsyncAccount
import asyncio

client = AsyncClient()
client.set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

account = AsyncAccount(client)

async def create_email_password_session:
    await account.create_email_password_session(
    email = 'email@example.com',
    password = 'password'
)

result = asyncio.run(create_email_password_session())
