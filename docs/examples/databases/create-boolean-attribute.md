from async_appwrite.async_client import AsyncClient
from async_appwrite.services.async_databases import AsyncDatabases


client = AsyncClient()
client.set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_key('<YOUR_API_KEY>') # Your secret API key

databases = AsyncDatabases(client)

result = databases.create_boolean_attribute(
    database_id = '<DATABASE_ID>',
    collection_id = '<COLLECTION_ID>',
    key = '',
    required = False,
    default = False, # optional
    array = False # optional
)
