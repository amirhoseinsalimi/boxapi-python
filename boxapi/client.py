from .instagram import InstagramAPI


class BoxApiClient:
    """
    A client for interacting with the Box API.
    """

    def __init__(self, username: str, password: str, base_url: str = "https://boxapi.ir"):
        self.username = username
        self.password = password
        self.base_url = base_url
        self.auth = (self.username, self.password)

        self.instagram = InstagramAPI(base_url=self.base_url, auth=self.auth)
