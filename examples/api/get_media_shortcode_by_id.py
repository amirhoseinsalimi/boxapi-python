import json
import os

from boxapi import BoxApiClient

username = os.environ.get("BOXAPI_USERNAME")
password = os.environ.get("BOXAPI_PASSWORD")

box_client = BoxApiClient(username, password)

media_id = 3589949054983440021

response = box_client.instagram.get_media_shortcode_by_id(media_id)

print(json.dumps(response, indent=4, ensure_ascii=False))
