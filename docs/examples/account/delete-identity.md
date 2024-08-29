from async_appwrite.async_client import AsyncClient
from async_appwrite.services.async_account import AsyncAccount

client = AsyncClient()
client.set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

account = AsyncAccount(client)

result = account.delete_identity(
    identity_id = '<IDENTITY_ID>'
)
