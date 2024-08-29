from async_appwrite.async_client import AsyncClient
from async_appwrite.services.async_account import AsyncAccount
from appwrite.enums import OAuthProvider

client = AsyncClient()
client.set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID

account = AsyncAccount(client)

result = account.create_o_auth2_token(
    provider = OAuthProvider.AMAZON,
    success = 'https://example.com', # optional
    failure = 'https://example.com', # optional
    scopes = [] # optional
)
