from async_appwrite.async_client import AsyncClient
from async_appwrite.services.async_account import AsyncAccount

from appwrite.enums import AuthenticatorType

client = AsyncClient()
client.set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
client.set_project('<YOUR_PROJECT_ID>') # Your project ID
client.set_session('') # The user session to authenticate with

account = AsyncAccount(client)

result = account.update_mfa_authenticator(
    type = AuthenticatorType.TOTP,
    otp = '<OTP>'
)
