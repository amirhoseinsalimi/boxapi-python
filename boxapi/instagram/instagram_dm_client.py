from boxapi.utils.base_url_session import BaseUrlSession


class InstagramDMClient:
    """
    A sub-client to handle API calls related to Instagram Direct Messages.
    """

    def __init__(self, base_url: str, auth: tuple):
        self.auth = auth
        self.request = BaseUrlSession(base_url)

    def verify_challenge(self, username: str, password: str, code: str) -> dict:
        """
        Verify the challenge (verification code) for an Instagram account via the Box API.

        :param username: The Instagram account username (required).
        :param password: The Instagram account password (required).
        :param code: The verification code sent to the user's Instagram account (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'username', 'password', or 'code' is not provided or empty.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not username:
            raise ValueError("The 'username' parameter is required and cannot be empty.")
        if not password:
            raise ValueError("The 'password' parameter is required and cannot be empty.")
        if not code:
            raise ValueError("The 'code' parameter is required and cannot be empty.")

        url = "/verify"
        payload = {
            "username": username,
            "password": password,
            "code": code
        }

        response = self.request.post(url, auth=self.auth, json=payload)
        response.raise_for_status()

        return response.json()

    def direct_login(self, username: str, password: str) -> dict:
        """
        Perform a direct login to the specified Instagram account via the Box API.

        :param username: The Instagram account username (required).
        :param password: The Instagram account password (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'username' or 'password' is empty.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not username:
            raise ValueError("The 'username' parameter is required and cannot be empty.")
        if not password:
            raise ValueError("The 'password' parameter is required and cannot be empty.")

        url = "/login"
        payload = {
            "username": username,
            "password": password
        }

        response = self.request.post(url, auth=self.auth, json=payload)
        response.raise_for_status()

        return response.json()

    def get_direct_threads(
            self,
            username: str,
            password: str,
            amount: int = 20,
            selected_filter: str = "",
            thread_message_limit: int = 0
    ) -> dict:
        """
        Retrieve direct threads for the specified Instagram account via the Box API.

        :param username: The Instagram account username (required).
        :param password: The Instagram account password (required).
        :param amount: Number of threads to retrieve (default=20).
        :param selected_filter: An optional filter for threads (default="").
        :param thread_message_limit: Number of messages to retrieve per thread (default=0).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'username' or 'password' is empty.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not username:
            raise ValueError("The 'username' parameter is required and cannot be empty.")
        if not password:
            raise ValueError("The 'password' parameter is required and cannot be empty.")

        url = "/direct_threads"
        payload = {
            "username": username,
            "password": password,
            "amount": amount,
            "selected_filter": selected_filter,
            "thread_message_limit": thread_message_limit
        }

        response = self.request.post(url, auth=self.auth, json=payload)
        response.raise_for_status()

        return response.json()

    def direct_send(
            self,
            username: str,
            password: str,
            text: str,
            user_ids: list[int] = None,
            thread_ids: list[str] = None
    ) -> dict:
        """
        Send a direct message to one or more recipients or threads via the Box API.

        :param username: The Instagram account username (required).
        :param password: The Instagram account password (required).
        :param text: The message text to send (required).
        :param user_ids: A list of user IDs to receive the message (optional).
        :param thread_ids: A list of existing thread IDs to receive the message (optional).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'username', 'password', or 'text' is empty,
                           or if both 'user_ids' and 'thread_ids' are empty.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not username:
            raise ValueError("The 'username' parameter is required and cannot be empty.")
        if not password:
            raise ValueError("The 'password' parameter is required and cannot be empty.")
        if not text:
            raise ValueError("The 'text' parameter is required and cannot be empty.")
        if (not user_ids) and (not thread_ids):
            raise ValueError("You must provide at least one of 'user_ids' or 'thread_ids'.")

        url = "/direct_send"
        payload = {
            "username": username,
            "password": password,
            "text": text
        }

        if user_ids is not None:
            payload["user_ids"] = user_ids
        if thread_ids is not None:
            payload["thread_ids"] = thread_ids

        response = self.request.post(url, auth=self.auth, json=payload)
        response.raise_for_status()

        return response.json()

    def get_pending_inbox(self, username: str, password: str, amount: int = 20) -> dict:
        """
        Retrieve pending inbox items (requests) for the specified Instagram account via the Box API.

        :param username: The Instagram account username (required).
        :param password: The Instagram account password (required).
        :param amount: Number of pending items to retrieve (default=20).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'username' or 'password' is empty.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not username:
            raise ValueError("The 'username' parameter is required and cannot be empty.")
        if not password:
            raise ValueError("The 'password' parameter is required and cannot be empty.")

        url = "/pending_inbox"
        payload = {
            "username": username,
            "password": password,
            "amount": amount
        }

        response = self.request.post(url, auth=self.auth, json=payload)
        response.raise_for_status()
        return response.json()

    def get_direct_messages(
            self,
            username: str,
            password: str,
            thread_id: int,
            amount: int = 20
    ) -> dict:
        """
        Retrieve messages from a specific direct message thread via the Box API.

        :param username: The Instagram account username (required).
        :param password: The Instagram account password (required).
        :param thread_id: The integer ID of the direct message thread (required).
        :param amount: Number of messages to retrieve (default=20).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'username', 'password', or 'thread_id' is invalid or missing.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not username:
            raise ValueError("The 'username' parameter is required and cannot be empty.")
        if not password:
            raise ValueError("The 'password' parameter is required and cannot be empty.")
        if thread_id is None:
            raise ValueError("The 'thread_id' parameter is required.")

        url = "/direct_messages"
        payload = {
            "username": username,
            "password": password,
            "thread_id": thread_id,
            "amount": amount
        }

        response = self.request.post(url, auth=self.auth, json=payload)
        response.raise_for_status()
        return response.json()

    def direct_answer(self, username: str, password: str, thread_id: int, text: str) -> dict:
        """
        Send an answer (reply) in a specific direct message thread via the Box API.

        :param username: The Instagram account username (required).
        :param password: The Instagram account password (required).
        :param thread_id: The integer ID of the direct message thread (required).
        :param text: The message text to send as a reply (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'username', 'password', 'thread_id', or 'text' is missing or invalid.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not username:
            raise ValueError("The 'username' parameter is required and cannot be empty.")
        if not password:
            raise ValueError("The 'password' parameter is required and cannot be empty.")
        if not thread_id:
            raise ValueError("The 'thread_id' parameter is required and cannot be empty.")
        if not text:
            raise ValueError("The 'text' parameter is required and cannot be empty.")

        url = "/direct_answer"
        payload = {
            "username": username,
            "password": password,
            "thread_id": thread_id,
            "text": text
        }

        response = self.request.post(url, auth=self.auth, json=payload)
        response.raise_for_status()

        return response.json()

    def direct_search(self, username: str, password: str, query: str) -> dict:
        """
        Search for users or messages in the direct inbox via the Box API.

        :param username: The Instagram account username (required).
        :param password: The Instagram account password (required).
        :param query: The search query (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'username', 'password', or 'query' is empty.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not username:
            raise ValueError("The 'username' parameter is required and cannot be empty.")
        if not password:
            raise ValueError("The 'password' parameter is required and cannot be empty.")
        if not query:
            raise ValueError("The 'query' parameter is required and cannot be empty.")

        url = "/direct_search"
        payload = {
            "username": username,
            "password": password,
            "query": query
        }

        response = self.request.post(url, auth=self.auth, json=payload)
        response.raise_for_status()
        return response.json()

    def get_direct_thread(
            self,
            username: str,
            password: str,
            thread_id: int,
            amount: int = 20
    ) -> dict:
        """
        Retrieve information about a specific direct message thread via the Box API.

        :param username: The Instagram account username (required).
        :param password: The Instagram account password (required).
        :param thread_id: The integer ID of the direct message thread (required).
        :param amount: Number of messages to retrieve in the thread (default=20).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'username', 'password', or 'thread_id' is missing or invalid.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not username:
            raise ValueError("The 'username' parameter is required and cannot be empty.")
        if not password:
            raise ValueError("The 'password' parameter is required and cannot be empty.")
        if not thread_id:
            raise ValueError("The 'thread_id' parameter is required and cannot be empty.")

        url = "/direct_thread"
        payload = {
            "username": username,
            "password": password,
            "thread_id": thread_id,
            "amount": amount
        }

        response = self.request.post(url, auth=self.auth, json=payload)
        response.raise_for_status()

        return response.json()

    def direct_thread_by_participants(self, username: str, password: str, user_ids: list[int]) -> dict:
        """
        Retrieve or create a direct message thread based on a list of user IDs via the Box API.

        :param username: The Instagram account username (required).
        :param password: The Instagram account password (required).
        :param user_ids: A list of user IDs (required) for which you want to find or create a DM thread.
        :return: JSON response as a dictionary.
        :raises ValueError: If 'username', 'password' is empty, or 'user_ids' is not provided or empty.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not username:
            raise ValueError("The 'username' parameter is required and cannot be empty.")
        if not password:
            raise ValueError("The 'password' parameter is required and cannot be empty.")
        if not user_ids:
            raise ValueError("The 'user_ids' parameter is required and must contain at least one user ID.")

        url = "/direct_thread_by_participants"
        payload = {
            "username": username,
            "password": password,
            "user_ids": user_ids
        }

        response = self.request.post(url, auth=self.auth, json=payload)
        response.raise_for_status()

        return response.json()
