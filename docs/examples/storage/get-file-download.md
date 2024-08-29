from async_appwrite.async_client import AsyncClient
from async_appwrite.services.async_storage import AsyncStorage


client = AsyncClient()
client.set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

storage = AsyncStorage(client)

result = storage.get_file_download(
    bucket_id = '<BUCKET_ID>',
    file_id = '<FILE_ID>'
)
