from async_appwrite.async_client import AsyncClient
from async_appwrite.services.async_account import AsyncAccount

client = AsyncClient()
client.set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

account = AsyncAccount(client)

result = account.create(
    user_id = '<USER_ID>',
    email = 'email@example.com',
    password = '',
    name = '<NAME>' # optional
)
