#!/usr/bin/env python

import argparse
from boxapi import BoxApiClient


def main():
    parser = argparse.ArgumentParser(description="Box API Client Development Runner")
    parser.add_argument("--username", type=str, required=True, help="Box API username")
    parser.add_argument("--password", type=str, required=True, help="Box API password")
    parser.add_argument("--insta-username", type=str, default="Boxapi.ir", help="Instagram username to lookup")
    args = parser.parse_args()

    client = BoxApiClient(args.username, args.password)
    output = client.get_instagram_user_info(args.insta_username)
    print(f"Output:\n{output}")


if __name__ == "__main__":
    main()
