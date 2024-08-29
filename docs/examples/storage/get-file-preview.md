from async_appwrite.async_client import AsyncClient
from async_appwrite.services.async_storage import AsyncStorage


client = AsyncClient()
client.set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

storage = AsyncStorage(client)

result = storage.get_file_preview(
    bucket_id = '<BUCKET_ID>',
    file_id = '<FILE_ID>',
    width = 0, # optional
    height = 0, # optional
    gravity = ImageGravity.CENTER, # optional
    quality = 0, # optional
    border_width = 0, # optional
    border_color = '', # optional
    border_radius = 0, # optional
    opacity = 0, # optional
    rotation = -360, # optional
    background = '', # optional
    output = ImageFormat.JPG # optional
)
