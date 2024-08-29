from async_appwrite.async_client import AsyncClient
from async_appwrite.services.async_storage import AsyncStorage


client = AsyncClient()
client.set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

storage = AsyncStorage(client)

result = storage.delete_bucket(
    bucket_id = '<BUCKET_ID>'
)
