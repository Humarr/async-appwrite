from async_appwrite.async_client import AsyncClient
from async_appwrite.services.async_account import AsyncAccount
import asyncio

client = AsyncClient()
client.set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

account = AsyncAccount(client)

result = account.create_email_token(
    user_id = '<USER_ID>',
    email = 'email@example.com',
    phrase = False # optional
)

async def create_email_token:
    await account.create_email_token(

        user_id = '<USER_ID>',
        email = 'email@example.com',
        phrase = False # optional
    )

asyncio.run(create_email_token())