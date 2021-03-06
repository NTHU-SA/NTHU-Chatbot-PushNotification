import json
import os
from .crawl import crawler
import time
import requests

def fetch_messages(**options):
    """Crawl the specific school"""
    with open(f"{os.environ['LIST_DIRECTORY']}/url_list.json", "r") as f:
        schools = json.loads(f.read())

    content = []
    for sc in options["schools"]:
        school = sc.upper()
        if school not in schools:
            print(f"The school does not exist: {school}")
            continue

        for dep, detail in schools[school]["dep"].items():
            for office, link in detail["url"].items():
                try:
                    notification = getattr(crawler(), school + "_" + dep)(office=office, ta_link=link)
                    content.append(notification)
                except requests.exceptions.RequestException as e:
                    print(f"Department {dep} has failed. Message: {e}")
    return content