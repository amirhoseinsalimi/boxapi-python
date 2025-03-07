import requests


class BoxApiClient:
    """
    A client for interacting with the Box API.
    """

    def __init__(self, username: str, password: str, base_url: str = "https://boxapi.ir"):
        self.username = username
        self.password = password
        self.base_url = base_url
        self.auth = (self.username, self.password)

    def get_instagram_user_info(self, username: str) -> dict:
        """
        Retrieve Instagram user information using the Box API.

        :param username: Instagram username to look up.
        :return: JSON response as a dictionary.
        """
        url = f"{self.base_url}/api/instagram/user/get_info"
        payload = {"username": username}
        response = requests.post(url, auth=self.auth, json=payload)
        response.raise_for_status()

        return response.json()

    def get_web_profile_info(self, username: str) -> dict:
        """
        Retrieve Instagram web profile information via the Box API.

        :param username: Instagram username to look up.
        :return: JSON response as a dictionary.
        :raises ValueError: If 'username' is not provided.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not username:
            raise ValueError("The 'username' parameter is required.")

        url = f"{self.base_url}/api/instagram/user/get_web_profile_info"
        payload = {"username": username}
        response = requests.post(url, auth=self.auth, json=payload)

        response.raise_for_status()

        return response.json()

    def get_instagram_user_info_by_id(self, user_id: int) -> dict:
        """
        Retrieve Instagram user information by ID via the Box API.

        :param user_id: The integer ID of the Instagram user.
        :return: JSON response as a dictionary.
        :raises ValueError: If 'user_id' is not provided or invalid.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not user_id:
            raise ValueError("The 'user_id' parameter is required and must be a positive integer.")

        url = f"{self.base_url}/api/instagram/user/get_info_by_id"
        payload = {"id": user_id}

        response = requests.post(url, auth=self.auth, json=payload)
        response.raise_for_status()

        return response.json()

    def get_instagram_user_media(self, user_id: int, count: int = 12, max_id: str = None) -> dict:
        """
        Retrieve a list of Instagram media by user ID via the Box API.

        :param user_id: The integer ID of the Instagram user.
        :param count: Number of media items to retrieve (default=12, max=12).
        :param max_id: Used for pagination; pass the last media ID from a previous call.
        :return: JSON response as a dictionary.
        :raises ValueError: If 'user_id' is not provided or invalid.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not user_id:
            raise ValueError("The 'user_id' parameter is required and must be a positive integer.")

        url = f"{self.base_url}/api/instagram/user/get_media"
        payload = {
            "id": user_id,
            "count": count
        }
        if max_id is not None:
            payload["max_id"] = max_id

        response = requests.post(url, auth=self.auth, json=payload)
        response.raise_for_status()

        return response.json()
