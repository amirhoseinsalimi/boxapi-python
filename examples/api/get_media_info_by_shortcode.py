import json
import os

from boxapi import BoxApiClient

username = os.environ.get("BOXAPI_USERNAME")
password = os.environ.get("BOXAPI_PASSWORD")

box_client = BoxApiClient(username, password)

shortcode = "DHOj889NIXc"

response = box_client.instagram.get_media_info_by_shortcode(shortcode)

print(json.dumps(response, indent=4, ensure_ascii=False))
