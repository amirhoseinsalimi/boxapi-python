import requests


def get_user_info(auth: tuple, base_url: str, username: str) -> dict:
    """
    Retrieve Instagram user information via the Box API.

    :param auth: A tuple (username, password) for basic authentication.
    :param base_url: The base URL for the Box API.
    :param username: Instagram username to fetch information for.
    :return: JSON response as a dictionary.
    """
    url = f"{base_url}/api/instagram/user/get_info"
    payload = {"username": username}
    response = requests.post(url, auth=auth, json=payload)
    response.raise_for_status()
    return response.json()
