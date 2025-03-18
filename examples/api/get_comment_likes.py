import json
import os

from boxapi import BoxApiClient

username = os.environ.get("BOXAPI_USERNAME")
password = os.environ.get("BOXAPI_PASSWORD")

box_client = BoxApiClient(username, password)

response = box_client.instagram.get_comment_likes(18126508303072945)

print(json.dumps(response, indent=4, ensure_ascii=False))
