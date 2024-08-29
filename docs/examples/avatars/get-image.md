from async_appwrite.async_client import AsyncClient
from async_appwrite.services.async_avatars import AsyncAvatars


client = AsyncClient()
client.set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

avatars = AsyncAvatars(client)

result = avatars.get_image(
    url = 'https://example.com',
    width = 0, # optional
    height = 0 # optional
)
