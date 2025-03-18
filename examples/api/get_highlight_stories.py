import json
import os

from boxapi import BoxApiClient

username = os.environ.get("BOXAPI_USERNAME")
password = os.environ.get("BOXAPI_PASSWORD")

box_client = BoxApiClient(username, password)

response = box_client.instagram.get_highlight_stories([17921323208305478])

print(json.dumps(response, indent=4, ensure_ascii=False))
