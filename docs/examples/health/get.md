from async_appwrite.async_client import AsyncClient
from async_appwrite.services.async_health import AsyncHealth


client = AsyncClient()
client.set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

health = AsyncHealth(client)

result = health.get()
