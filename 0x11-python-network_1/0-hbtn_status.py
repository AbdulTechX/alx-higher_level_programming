#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        body = response.read()
        decoded_body = body.decode('utf-8')

        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", decoded_body)
