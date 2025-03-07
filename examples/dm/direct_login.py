from boxapi import BoxApiClient

box_client = BoxApiClient("your_boxapi_username", "your_boxapi_password")

login_response = box_client.instagram_dm.direct_login("insta_username", "insta_password")
print(login_response)