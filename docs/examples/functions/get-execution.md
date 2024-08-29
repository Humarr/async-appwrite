from async_appwrite.async_client import AsyncClient
from async_appwrite.services.async_functions import AsyncFunctions


client = AsyncClient()
client.set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

functions = AsyncFunctions(client)

result = functions.get_execution(
    function_id = '<FUNCTION_ID>',
    execution_id = '<EXECUTION_ID>'
)
