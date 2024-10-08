from ..async_service import AsyncService
from appwrite.exception import AppwriteException

from ..async_client import AsyncClient


class AsyncAccount(AsyncService):
    def __init__(self, client: AsyncClient):
        super().__init__(client)

        # self.client = client

    async def get(self):
        """Get account"""

        api_path = "/account"
        api_params = {}

        return await self.client.call(
            "get",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def create(self, user_id, email, password, name=None):
        """Create account"""

        api_path = "/account"
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if email is None:
            raise AppwriteException('Missing required parameter: "email"')

        if password is None:
            raise AppwriteException('Missing required parameter: "password"')

        api_params["userId"] = user_id
        api_params["email"] = email
        api_params["password"] = password
        api_params["name"] = name

        return await self.client.call(
            "post",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def update_email(self, email, password):
        """Update email"""

        api_path = "/account/email"
        api_params = {}
        if email is None:
            raise AppwriteException('Missing required parameter: "email"')

        if password is None:
            raise AppwriteException('Missing required parameter: "password"')

        api_params["email"] = email
        api_params["password"] = password

        return await self.client.call(
            "patch",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def list_identities(self, queries=None):
        """List Identities"""

        api_path = "/account/identities"
        api_params = {}

        api_params["queries"] = queries

        return await self.client.call(
            "get",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def delete_identity(self, identity_id):
        """Delete identity"""

        api_path = "/account/identities/{identityId}"
        api_params = {}
        if identity_id is None:
            raise AppwriteException('Missing required parameter: "identity_id"')

        api_path = api_path.replace("{identityId}", identity_id)

        return await self.client.call(
            "delete",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def create_jwt(self):
        """Create JWT"""

        api_path = "/account/jwt"
        api_params = {}

        return await self.client.call(
            "post",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def list_logs(self, queries=None):
        """List logs"""

        api_path = "/account/logs"
        api_params = {}

        api_params["queries"] = queries

        return await self.client.call(
            "get",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def update_mfa(self, mfa):
        """Update MFA"""

        api_path = "/account/mfa"
        api_params = {}
        if mfa is None:
            raise AppwriteException('Missing required parameter: "mfa"')

        api_params["mfa"] = mfa

        return await self.client.call(
            "patch",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def create_mfa_authenticator(self, type):
        """Add Authenticator"""

        api_path = "/account/mfa/authenticators/{type}"
        api_params = {}
        if type is None:
            raise AppwriteException('Missing required parameter: "type"')

        api_path = api_path.replace("{type}", type)

        return await self.client.call(
            "post",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def update_mfa_authenticator(self, type, otp):
        """Verify Authenticator"""

        api_path = "/account/mfa/authenticators/{type}"
        api_params = {}
        if type is None:
            raise AppwriteException('Missing required parameter: "type"')

        if otp is None:
            raise AppwriteException('Missing required parameter: "otp"')

        api_path = api_path.replace("{type}", type)

        api_params["otp"] = otp

        return await self.client.call(
            "put",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def delete_mfa_authenticator(self, type, otp):
        """Delete Authenticator"""

        api_path = "/account/mfa/authenticators/{type}"
        api_params = {}
        if type is None:
            raise AppwriteException('Missing required parameter: "type"')

        if otp is None:
            raise AppwriteException('Missing required parameter: "otp"')

        api_path = api_path.replace("{type}", type)

        api_params["otp"] = otp

        return await self.client.call(
            "delete",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def create_mfa_challenge(self, factor):
        """Create 2FA Challenge"""

        api_path = "/account/mfa/challenge"
        api_params = {}
        if factor is None:
            raise AppwriteException('Missing required parameter: "factor"')

        api_params["factor"] = factor

        return await self.client.call(
            "post",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def update_mfa_challenge(self, challenge_id, otp):
        """Create MFA Challenge (confirmation)"""

        api_path = "/account/mfa/challenge"
        api_params = {}
        if challenge_id is None:
            raise AppwriteException('Missing required parameter: "challenge_id"')

        if otp is None:
            raise AppwriteException('Missing required parameter: "otp"')

        api_params["challengeId"] = challenge_id
        api_params["otp"] = otp

        return await self.client.call(
            "put",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def list_mfa_factors(self):
        """List Factors"""

        api_path = "/account/mfa/factors"
        api_params = {}

        return await self.client.call(
            "get",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def get_mfa_recovery_codes(self):
        """Get MFA Recovery Codes"""

        api_path = "/account/mfa/recovery-codes"
        api_params = {}

        return await self.client.call(
            "get",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def create_mfa_recovery_codes(self):
        """Create MFA Recovery Codes"""

        api_path = "/account/mfa/recovery-codes"
        api_params = {}

        return await self.client.call(
            "post",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def update_mfa_recovery_codes(self):
        """Regenerate MFA Recovery Codes"""

        api_path = "/account/mfa/recovery-codes"
        api_params = {}

        return await self.client.call(
            "patch",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def update_name(self, name):
        """Update name"""

        api_path = "/account/name"
        api_params = {}
        if name is None:
            raise AppwriteException('Missing required parameter: "name"')

        api_params["name"] = name

        return await self.client.call(
            "patch",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def update_password(self, password, old_password=None):
        """Update password"""

        api_path = "/account/password"
        api_params = {}
        if password is None:
            raise AppwriteException('Missing required parameter: "password"')

        api_params["password"] = password
        api_params["oldPassword"] = old_password

        return await self.client.call(
            "patch",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def update_phone(self, phone, password):
        """Update phone"""

        api_path = "/account/phone"
        api_params = {}
        if phone is None:
            raise AppwriteException('Missing required parameter: "phone"')

        if password is None:
            raise AppwriteException('Missing required parameter: "password"')

        api_params["phone"] = phone
        api_params["password"] = password

        return await self.client.call(
            "patch",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def get_prefs(self):
        """Get account preferences"""

        api_path = "/account/prefs"
        api_params = {}

        return await self.client.call(
            "get",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def update_prefs(self, prefs):
        """Update preferences"""

        api_path = "/account/prefs"
        api_params = {}
        if prefs is None:
            raise AppwriteException('Missing required parameter: "prefs"')

        api_params["prefs"] = prefs

        return await self.client.call(
            "patch",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def create_recovery(self, email, url):
        """Create password recovery"""

        api_path = "/account/recovery"
        api_params = {}
        if email is None:
            raise AppwriteException('Missing required parameter: "email"')

        if url is None:
            raise AppwriteException('Missing required parameter: "url"')

        api_params["email"] = email
        api_params["url"] = url

        return await self.client.call(
            "post",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def update_recovery(self, user_id, secret, password):
        """Create password recovery (confirmation)"""

        api_path = "/account/recovery"
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')

        if password is None:
            raise AppwriteException('Missing required parameter: "password"')

        api_params["userId"] = user_id
        api_params["secret"] = secret
        api_params["password"] = password

        return await self.client.call(
            "put",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def list_sessions(self):
        """List sessions"""

        api_path = "/account/sessions"
        api_params = {}

        return await self.client.call(
            "get",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def delete_sessions(self):
        """Delete sessions"""

        api_path = "/account/sessions"
        api_params = {}

        return await self.client.call(
            "delete",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def create_anonymous_session(self):
        """Create anonymous session"""

        api_path = "/account/sessions/anonymous"
        api_params = {}

        return await self.client.call(
            "post",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def create_email_password_session(self, email, password):
        """Create email password session"""

        api_path = "/account/sessions/email"
        api_params = {}
        if email is None:
            raise AppwriteException('Missing required parameter: "email"')

        if password is None:
            raise AppwriteException('Missing required parameter: "password"')

        api_params["email"] = email
        api_params["password"] = password

        return await self.client.call(
            "post",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def update_magic_url_session(self, user_id, secret):
        """Update magic URL session"""

        api_path = "/account/sessions/magic-url"
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')

        api_params["userId"] = user_id
        api_params["secret"] = secret

        return await self.client.call(
            "put",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def update_phone_session(self, user_id, secret):
        """Update phone session"""

        api_path = "/account/sessions/phone"
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')

        api_params["userId"] = user_id
        api_params["secret"] = secret

        return await self.client.call(
            "put",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def create_session(self, user_id, secret):
        """Create session"""

        api_path = "/account/sessions/token"
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')

        api_params["userId"] = user_id
        api_params["secret"] = secret

        return await self.client.call(
            "post",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def get_session(self, session_id):
        """Get session"""

        api_path = "/account/sessions/{sessionId}"
        api_params = {}
        if session_id is None:
            raise AppwriteException('Missing required parameter: "session_id"')

        api_path = api_path.replace("{sessionId}", session_id)

        return await self.client.call(
            "get",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def update_session(self, session_id):
        """Update session"""

        api_path = "/account/sessions/{sessionId}"
        api_params = {}
        if session_id is None:
            raise AppwriteException('Missing required parameter: "session_id"')

        api_path = api_path.replace("{sessionId}", session_id)

        return await self.client.call(
            "patch",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def delete_session(self, session_id):
        """Delete session"""

        api_path = "/account/sessions/{sessionId}"
        api_params = {}
        if session_id is None:
            raise AppwriteException('Missing required parameter: "session_id"')

        api_path = api_path.replace("{sessionId}", session_id)

        return await self.client.call(
            "delete",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def update_status(self):
        """Update status"""

        api_path = "/account/status"
        api_params = {}

        return await self.client.call(
            "patch",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def create_email_token(self, user_id, email, phrase=None):
        """Create email token (OTP)"""

        api_path = "/account/tokens/email"
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if email is None:
            raise AppwriteException('Missing required parameter: "email"')

        api_params["userId"] = user_id
        api_params["email"] = email
        api_params["phrase"] = phrase

        return await self.client.call(
            "post",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def create_magic_url_token(self, user_id, email, url=None, phrase=None):
        """Create magic URL token"""

        api_path = "/account/tokens/magic-url"
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if email is None:
            raise AppwriteException('Missing required parameter: "email"')

        api_params["userId"] = user_id
        api_params["email"] = email
        api_params["url"] = url
        api_params["phrase"] = phrase

        return await self.client.call(
            "post",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def create_o_auth2_token(
        self, provider, success=None, failure=None, scopes=None
    ):
        """Create OAuth2 token"""

        api_path = "/account/tokens/oauth2/{provider}"
        api_params = {}
        if provider is None:
            raise AppwriteException('Missing required parameter: "provider"')

        api_path = api_path.replace("{provider}", provider)

        api_params["success"] = success
        api_params["failure"] = failure
        api_params["scopes"] = scopes

        return await self.client.call(
            "get",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
            response_type="location",
        )

    async def create_phone_token(self, user_id, phone):
        """Create phone token"""

        api_path = "/account/tokens/phone"
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if phone is None:
            raise AppwriteException('Missing required parameter: "phone"')

        api_params["userId"] = user_id
        api_params["phone"] = phone

        return await self.client.call(
            "post",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def create_verification(self, url):
        """Create email verification"""

        api_path = "/account/verification"
        api_params = {}
        if url is None:
            raise AppwriteException('Missing required parameter: "url"')

        api_params["url"] = url

        return await self.client.call(
            "post",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def update_verification(self, user_id, secret):
        """Create email verification (confirmation)"""

        api_path = "/account/verification"
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')

        api_params["userId"] = user_id
        api_params["secret"] = secret

        return await self.client.call(
            "put",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def create_phone_verification(self):
        """Create phone verification"""

        api_path = "/account/verification/phone"
        api_params = {}

        return await self.client.call(
            "post",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )

    async def update_phone_verification(self, user_id, secret):
        """Create phone verification (confirmation)"""

        api_path = "/account/verification/phone"
        api_params = {}
        if user_id is None:
            raise AppwriteException('Missing required parameter: "user_id"')

        if secret is None:
            raise AppwriteException('Missing required parameter: "secret"')

        api_params["userId"] = user_id
        api_params["secret"] = secret

        return await self.client.call(
            "put",
            api_path,
            {
                "content-type": "application/json",
            },
            api_params,
        )
