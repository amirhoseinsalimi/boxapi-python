from functools import wraps
from typing import Callable, Any, Dict, Tuple, TypeVar

T = TypeVar("T", bound=Callable[..., Tuple[str, Dict[str, Any]]])


def post_request(func: T) -> T:
    """
    Decorator for handling Box API POST requests in a consistent way.

    The decorated method must return a tuple of (url, payload). This decorator:
    - Sends a POST request using self.request
    - Applies self.auth for authentication
    - Raises errors on failure
    - Returns parsed JSON response

    :param func: Method that returns (url, payload)
    :return: API response as a dictionary
    """

    @wraps(func)
    def wrapper(self, *args: Any, **kwargs: Any) -> Dict[str, Any]:
        url, payload = func(self, *args, **kwargs)
        response = self.request.post(url, auth=self.auth, json=payload)
        response.raise_for_status()
        return response.json()

    return wrapper  # type: ignore
