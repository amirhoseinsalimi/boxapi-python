from .instagram.instagram_api_client import InstagramAPIClient
from .instagram.instagram_dm_client import InstagramDMClient
from .constants import INSTAGRAM_BASE_URL, INSTAGRAM_DM_BASE_URL


class BoxApiClient:
    """
    A client for interacting with the Box API.
    """

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.auth = (self.username, self.password)

        self.instagram = InstagramAPIClient(base_url=INSTAGRAM_BASE_URL, auth=self.auth)
        self.instagram_dm = InstagramDMClient(base_url=INSTAGRAM_DM_BASE_URL, auth=self.auth)
