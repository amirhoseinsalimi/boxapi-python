import requests


class BaseUrlSession(requests.Session):
    def __init__(self, base_url: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.base_url = base_url.rstrip('/')

    def request(self, method, url, *args, **kwargs):
        if not url.startswith("http"):
            url = f"{self.base_url}/{url.lstrip('/')}"

        return super().request(method, url, *args, **kwargs)
