from boxapi import BoxApiClient

box_client = BoxApiClient("your_boxapi_username", "your_boxapi_password")

user_info = box_client.instagram.get_user_info("leomessi")

print(user_info)