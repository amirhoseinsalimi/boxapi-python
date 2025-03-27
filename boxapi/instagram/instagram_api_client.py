from typing import Any, Dict, Tuple, Optional, List

from boxapi.utils.base_url_session import BaseUrlSession
from boxapi.utils.decorators import post_request


class InstagramAPIClient:
    """
    A sub-client to handle Instagram-related API calls.
    """

    def __init__(self, base_url: str, auth: tuple):
        self.auth = auth
        self.request = BaseUrlSession(base_url)

    @post_request
    def get_user_info(self, username: str) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve Instagram user information using the Box API.

        :param username: The Instagram username to look up (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'username' is empty.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not username:
            raise ValueError("The 'username' parameter is required and cannot be empty.")

        url = "/user/get_info"
        payload = {"username": username}
        return url, payload

    @post_request
    def get_web_profile_info(self, username: str) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve Instagram web profile information via the Box API.

        :param username: Instagram username to look up.
        :return: JSON response as a dictionary.
        :raises ValueError: If 'username' is not provided.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not username:
            raise ValueError("The 'username' parameter is required.")

        url = "/user/get_web_profile_info"
        payload = {"username": username}
        return url, payload

    @post_request
    def get_info_by_id(self, user_id: int) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve Instagram user information by ID via the Box API.

        :param user_id: The integer ID of the Instagram user.
        :return: JSON response as a dictionary.
        :raises ValueError: If 'user_id' is not provided or invalid.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not user_id:
            raise ValueError("The 'user_id' parameter is required and must be a positive integer.")

        url = "/user/get_info_by_id"
        payload = {"id": user_id}
        return url, payload

    @post_request
    def get_media(self, user_id: int, count: int = 12, max_id: Optional[str] = None) -> Tuple[str, Dict[str, Any]]:
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

        url = "/user/get_media"
        payload: Dict[str, Any] = {
            "id": user_id,
            "count": count
        }

        if max_id is not None:
            payload["max_id"] = max_id

        return url, payload

    @post_request
    def get_media_by_username(self, username: str, count: int = 12, max_id: Optional[str] = None) -> Tuple[
        str, Dict[str, Any]]:
        """
        Retrieve a list of Instagram media by username via the Box API.

        :param username: Instagram username (required).
        :param count: Number of media items to retrieve (default=12, max=12).
        :param max_id: Used for pagination; pass the last media ID from a previous call.
        :return: JSON response as a dictionary.
        :raises ValueError: If 'username' is not provided.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not username:
            raise ValueError("The 'username' parameter is required and cannot be empty.")

        url = "/user/get_media_by_username"
        payload: Dict[str, Any] = {
            "username": username,
            "count": count
        }

        if max_id is not None:
            payload["max_id"] = max_id

        return url, payload

    @post_request
    def get_clips(self, user_id: int, count: int = 12, max_id: Optional[str] = None) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve a list of Instagram reels (Clips) by user ID via the Box API.

        :param user_id: The integer ID of the Instagram user (required).
        :param count: Number of media items to retrieve (default=12).
        :param max_id: Used for pagination; pass the last media ID from a previous call.
        :return: JSON response as a dictionary.
        :raises ValueError: If 'user_id' is not provided or invalid.
        :raises ValueError: If 'count' is less than 1.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not user_id:
            raise ValueError("The 'user_id' parameter is required and must be a positive integer.")
        if count < 1:
            raise ValueError("The 'count' parameter must be >= 1.")

        url = "/user/get_clips"
        payload: Dict[str, Any] = {
            "id": user_id,
            "count": count
        }

        if max_id is not None:
            payload["max_id"] = max_id

        return url, payload

    @post_request
    def get_guides(self, user_id: int, max_id: Optional[str] = None) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve Instagram Guides for a user by ID via the Box API.

        :param user_id: The integer ID of the Instagram user (required).
        :param max_id: Used for pagination; pass the last guide ID from a previous call.
        :return: JSON response as a dictionary.
        :raises ValueError: If 'user_id' is not provided or invalid.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not user_id:
            raise ValueError("The 'user_id' parameter is required and must be a positive integer.")

        url = "/user/get_guides"
        payload: Dict[str, Any] = {"id": user_id}

        if max_id is not None:
            payload["max_id"] = max_id

        return url, payload

    @post_request
    def get_tags(self, user_id: int, count: int = 12, max_id: Optional[str] = None) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve a list of media in which the user is tagged, via the Box API.

        :param user_id: The integer ID of the Instagram user (required).
        :param count: Number of media items to retrieve (default=12).
        :param max_id: Used for pagination; pass the last media ID from a previous call.
        :return: JSON response as a dictionary.
        :raises ValueError: If 'user_id' is invalid or 'count' is less than 1.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not user_id:
            raise ValueError("The 'user_id' parameter is required and must be a positive integer.")
        if count < 1:
            raise ValueError("The 'count' parameter must be >= 1.")

        url = "/user/get_tags"
        payload: Dict[str, Any] = {
            "id": user_id,
            "count": count
        }

        if max_id is not None:
            payload["max_id"] = max_id

        return url, payload

    @post_request
    def get_followers(self, user_id: int, count: int = 10, max_id: Optional[str] = None, query: Optional[str] = None) -> \
            Tuple[str, Dict[str, Any]]:
        """
        Retrieve a list of followers for a user by ID via the Box API.

        :param user_id: The integer ID of the Instagram user (required).
        :param count: Number of followers to retrieve (default=10).
        :param max_id: Used for pagination; pass the last follower ID from a previous call.
        :param query: A search string to filter the follower list (optional).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'user_id' is invalid or 'count' is less than 1.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not user_id:
            raise ValueError("The 'user_id' parameter is required and must be a positive integer.")
        if count < 1:
            raise ValueError("The 'count' parameter must be >= 1.")

        url = "/user/get_followers"
        payload: Dict[str, Any] = {
            "id": user_id,
            "count": count
        }

        if max_id is not None:
            payload["max_id"] = max_id

        if query:
            payload["query"] = query

        return url, payload

    @post_request
    def get_following(self, user_id: int, count: int = 10, max_id: Optional[str] = None, query: Optional[str] = None) -> \
            Tuple[str, Dict[str, Any]]:
        """
        Retrieve a list of users that the given user is following, via the Box API.

        :param user_id: The integer ID of the Instagram user (required).
        :param count: Number of users to retrieve (default=10).
        :param max_id: Used for pagination; pass the last user ID from a previous call.
        :param query: A search string to filter the following list (optional).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'user_id' is invalid or 'count' is less than 1.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not user_id:
            raise ValueError("The 'user_id' parameter is required and must be a positive integer.")
        if count < 1:
            raise ValueError("The 'count' parameter must be >= 1.")

        url = "/user/get_following"
        payload: Dict[str, Any] = {
            "id": user_id,
            "count": count
        }

        if max_id is not None:
            payload["max_id"] = max_id

        if query:
            payload["query"] = query

        return url, payload

    @post_request
    def get_stories(self, user_ids: List[int]) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve Instagram stories for a list of user IDs via the Box API.

        :param user_ids: A list of integer IDs for the Instagram users (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'user_ids' is empty or invalid.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not user_ids:
            raise ValueError("The 'user_ids' parameter is required and cannot be empty.")

        url = "/user/get_stories"
        payload = {"ids": user_ids}

        return url, payload

    @post_request
    def get_highlights(self, user_id: int) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve Instagram highlights for a user by ID via the Box API.

        :param user_id: The integer ID of the Instagram user (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'user_id' is not provided or invalid.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not user_id:
            raise ValueError("The 'user_id' parameter is required and must be a positive integer.")

        url = "/user/get_highlights"
        payload = {"id": user_id}

        return url, payload

    @post_request
    def get_live(self, user_id: int) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve live information for a user by ID via the Box API.

        :param user_id: The integer ID of the Instagram user (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'user_id' is not provided or invalid.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not user_id:
            raise ValueError("The 'user_id' parameter is required and must be a positive integer.")

        url = "/user/get_live"
        payload = {"id": user_id}

        return url, payload

    @post_request
    def get_similar_accounts(self, user_id: int) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve similar Instagram accounts for a user by ID via the Box API.

        :param user_id: The integer ID of the Instagram user (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'user_id' is not provided or invalid.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not user_id:
            raise ValueError("The 'user_id' parameter is required and must be a positive integer.")

        url = "/user/get_similar_accounts"
        payload = {"id": user_id}

        return url, payload

    @post_request
    def search_users(self, query: str) -> Tuple[str, Dict[str, Any]]:
        """
        Search for Instagram users via the Box API.

        :param query: The search query (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'query' is not provided or empty.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not query:
            raise ValueError("The 'query' parameter is required and cannot be empty.")

        url = "/user/search"
        payload = {"query": query}

        return url, payload

    @post_request
    def get_media_info(self, media_id: int) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve Instagram media information by media ID via the Box API.

        :param media_id: The integer ID of the media (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'media_id' is not provided or invalid.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not media_id:
            raise ValueError("The 'media_id' parameter is required and must be a positive integer.")

        url = "/media/get_info"
        payload = {"id": media_id}

        return url, payload

    @post_request
    def get_media_info_by_shortcode(self, shortcode: str) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve Instagram media information by shortcode via the Box API.

        :param shortcode: The media shortcode (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'shortcode' is not provided or empty.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not shortcode:
            raise ValueError("The 'shortcode' parameter is required and cannot be empty.")

        url = "/media/get_info_by_shortcode"
        payload = {"shortcode": shortcode}

        return url, payload

    @post_request
    def get_media_comments(self, media_id: int, min_id: Optional[str] = None, can_support_threading: bool = True) -> \
            Tuple[str, Dict[str, Any]]:
        """
        Retrieve comments for an Instagram media item via the Box API.

        :param media_id: The integer ID of the media (required).
        :param min_id: Used for pagination; pass the last comment ID from a previous call.
        :param can_support_threading: If True, supports threaded comments; if False, chronological order.
        :return: JSON response as a dictionary.
        :raises ValueError: If 'media_id' is not provided or invalid.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not media_id:
            raise ValueError("The 'media_id' parameter is required and must be a positive integer.")

        url = "/media/get_comments"
        payload: Dict[str, Any] = {
            "id": media_id,
            "can_support_threading": can_support_threading
        }

        if min_id is not None:
            payload["min_id"] = min_id

        return url, payload

    @post_request
    def get_media_likes_by_shortcode(self, shortcode: str) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve the users who liked a media item (up to 1000) via the Box API.

        :param shortcode: The media shortcode (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'shortcode' is not provided or empty.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not shortcode:
            raise ValueError("The 'shortcode' parameter is required and cannot be empty.")

        url = "/media/get_likes_by_shortcode"
        payload = {"shortcode": shortcode}

        return url, payload

    @post_request
    def get_media_id_by_shortcode(self, shortcode: str) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve a media ID given its shortcode via the Box API.

        :param shortcode: The media shortcode (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'shortcode' is not provided or empty.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not shortcode:
            raise ValueError("The 'shortcode' parameter is required and cannot be empty.")

        url = "/media/get_id_by_shortcode"
        payload = {"shortcode": shortcode}

        return url, payload

    @post_request
    def get_media_shortcode_by_id(self, media_id: int) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve a media shortcode given its ID via the Box API.

        :param media_id: The integer ID of the media (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'media_id' is not provided or invalid.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not media_id:
            raise ValueError("The 'media_id' parameter is required and must be a positive integer.")

        url = "/media/get_shortcode_by_id"
        payload = {"id": media_id}

        return url, payload

    @post_request
    def get_guide_info(self, guide_id: int) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve information about a specific Instagram guide via the Box API.

        :param guide_id: The integer ID of the guide (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'guide_id' is not provided or invalid.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not guide_id:
            raise ValueError("The 'guide_id' parameter is required and must be a positive integer.")

        url = "/guide/get_info"
        payload = {"id": guide_id}

        return url, payload

    @post_request
    def get_location_info(self, location_id: int) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve information about a specific Instagram location via the Box API.

        :param location_id: The integer ID of the location (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'location_id' is not provided or invalid.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not location_id:
            raise ValueError("The 'location_id' parameter is required and must be a positive integer.")

        url = "/location/get_info"
        payload = {"id": location_id}

        return url, payload

    @post_request
    def get_location_media(self, location_id: int, page: int = 1, max_id: Optional[str] = None) -> Tuple[
        str, Dict[str, Any]]:
        """
        Retrieve media associated with a specific Instagram location via the Box API.

        :param location_id: The integer ID of the location (required).
        :param page: Page number for pagination (default=1).
        :param max_id: Used for pagination; pass the last media ID from a previous call.
        :return: JSON response as a dictionary.
        :raises ValueError: If 'location_id' is not provided or invalid, or if 'page' is less than 1.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not location_id:
            raise ValueError("The 'location_id' parameter is required and must be a positive integer.")

        if page < 1:
            raise ValueError("The 'page' parameter must be >= 1.")

        url = "/location/get_media"
        payload: Dict[str, Any] = {
            "id": location_id,
            "page": page
        }

        if max_id is not None:
            payload["max_id"] = max_id

        return url, payload

    @post_request
    def search_locations(self, query: str) -> Tuple[str, Dict[str, Any]]:
        """
        Search for Instagram locations via the Box API.

        :param query: The search query (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'query' is not provided or empty.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not query:
            raise ValueError("The 'query' parameter is required and cannot be empty.")

        url = "/location/search"
        payload = {"query": query}

        return url, payload

    @post_request
    def get_hashtag_info(self, name: str) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve information about a specific Instagram hashtag via the Box API.

        :param name: The hashtag name (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'name' is not provided or empty.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not name:
            raise ValueError("The 'name' parameter is required and cannot be empty.")

        url = "/hashtag/get_info"
        payload = {"name": name}

        return url, payload

    @post_request
    def get_hashtag_media(self, name: str, tab: str = "recent", page: int = 1, max_id: Optional[str] = None) -> Tuple[
        str, Dict[str, Any]]:
        """
        Retrieve media for a specific Instagram hashtag via the Box API.

        :param name: The hashtag name (required).
        :param tab: Which tab to retrieve (e.g., "recent" or "clips"). Default is "recent".
        :param page: Page number for pagination (default=1).
        :param max_id: Used for pagination; pass the last media ID from a previous call.
        :return: JSON response as a dictionary.
        :raises ValueError: If 'name' is empty, or if 'page' is less than 1.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not name:
            raise ValueError("The 'name' parameter is required and cannot be empty.")

        if page < 1:
            raise ValueError("The 'page' parameter must be >= 1.")

        url = "/hashtag/get_media"
        payload: Dict[str, Any] = {
            "name": name,
            "tab": tab,
            "page": page
        }

        if max_id is not None:
            payload["max_id"] = max_id

        return url, payload

    @post_request
    def search_hashtags(self, query: str) -> Tuple[str, Dict[str, Any]]:
        """
        Search for Instagram hashtags via the Box API.

        :param query: The search query (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'query' is not provided or empty.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not query:
            raise ValueError("The 'query' parameter is required and cannot be empty.")

        url = "/hashtag/search"
        payload = {"query": query}

        return url, payload

    @post_request
    def get_audio_media(self, audio_id: int, max_id: Optional[str] = None) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve media associated with a specific Instagram audio track via the Box API.

        :param audio_id: The integer ID of the audio (required).
        :param max_id: Used for pagination; pass the last media ID from a previous call.
        :return: JSON response as a dictionary.
        :raises ValueError: If 'audio_id' is not provided or invalid.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not audio_id:
            raise ValueError("The 'audio_id' parameter is required and must be a positive integer.")

        url = "/audio/get_media"
        payload = {"id": audio_id}

        if max_id is not None:
            payload["max_id"] = max_id

        return url, payload

    @post_request
    def get_highlight_stories(self, highlight_ids: List[int]) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve stories for one or more Instagram highlights via the Box API.

        :param highlight_ids: A list of integer IDs for the highlights (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'highlight_ids' is empty or invalid.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not highlight_ids:
            raise ValueError("The 'highlight_ids' parameter must be a non-empty list of integers.")

        url = "/highlight/get_stories"
        payload = {"ids": highlight_ids}

        return url, payload

    @post_request
    def get_comment_likes(self, comment_id: int, max_id: Optional[str] = None) -> Tuple[str, Dict[str, Any]]:
        """
        Retrieve the users who liked a specific Instagram comment via the Box API.

        :param comment_id: The integer ID of the comment (required).
        :param max_id: Used for pagination; pass the last like ID from a previous call.
        :return: JSON response as a dictionary.
        :raises ValueError: If 'comment_id' is not provided or invalid.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not comment_id:
            raise ValueError("The 'comment_id' parameter is required and must be a positive integer.")

        url = "/comment/get_likes"
        payload = {"id": comment_id}

        if max_id is not None:
            payload["max_id"] = max_id

        return url, payload

    @post_request
    def get_comment_replies(self, comment_id: int, media_id: int, max_id: Optional[str] = None) -> Tuple[
        str, Dict[str, Any]]:
        """
        Retrieve replies for a specific Instagram comment via the Box API.

        :param comment_id: The integer ID of the comment (required).
        :param media_id: The integer ID of the media to which the comment belongs (required).
        :param max_id: Used for pagination; pass the last reply ID from a previous call.
        :return: JSON response as a dictionary.
        :raises ValueError: If 'comment_id' or 'media_id' is not provided or invalid.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not comment_id:
            raise ValueError("The 'comment_id' parameter is required and must be a positive integer.")

        if not media_id:
            raise ValueError("The 'media_id' parameter is required and must be a positive integer.")

        url = "/comment/get_replies"
        payload: Dict[str, Any] = {
            "id": comment_id,
            "media_id": media_id
        }

        if max_id is not None:
            payload["max_id"] = max_id

        return url, payload

    @post_request
    def search_audios(self, query: str) -> Tuple[str, Dict[str, Any]]:
        """
        Search for Instagram audio tracks via the Box API.

        :param query: The search query (required).
        :return: JSON response as a dictionary.
        :raises ValueError: If 'query' is not provided or empty.
        :raises requests.exceptions.HTTPError: If the HTTP request fails.
        """
        if not query:
            raise ValueError("The 'query' parameter is required and cannot be empty.")

        url = "/audio/search"
        payload = {"query": query}

        return url, payload
