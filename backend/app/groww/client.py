import pyotp

from growwapi import GrowwAPI

from .config import (
    TOTP_SECRET,
    TOTP_TOKEN,
)


class GrowwClient:
    """
    Lazy-loading Groww client.

    Authentication happens only when the first API method is called.
    The authenticated client is then cached and reused.
    """

    def __init__(self):
        self._client = None

    def _login(self):
        print("🔐 Authenticating with Groww...")

        totp = pyotp.TOTP(TOTP_SECRET)

        access_token = GrowwAPI.get_access_token(
            api_key=TOTP_TOKEN,
            totp=totp.now(),
        )

        self._client = GrowwAPI(access_token)

        print("✅ Groww authentication successful.")

    @property
    def client(self):
        if self._client is None:
            self._login()

        return self._client

    def refresh(self):
        """
        Force a fresh login.
        Useful if the access token expires.
        """
        self._client = None
        return self.client

    def __getattr__(self, name):
        """
        Forward every method/property to the real Groww client.

        This allows:

            groww.get_option_chain(...)
            groww.get_quotes(...)
            groww.get_historical_data(...)

        without changing any existing code.
        """
        return getattr(self.client, name)


# Singleton
groww = GrowwClient()