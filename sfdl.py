#!/usr/bin/env python3
import os
import requests
import sys

from bs4 import BeautifulSoup

if len(sys.argv) == 1:
  print(f"Usage: {sys.argv[0]} project_name")
  sys.exit(1)

PROJECT = sys.argv[1]
RSS_URL = f"https://sourceforge.net/projects/{PROJECT}/rss?path=/"

rss_data = requests.get(RSS_URL)


def download(name, link):
  response = requests.get(link)
  try:
    response.raise_for_status()
  except:
    print(f"{response.status_code} {link}")
    return
  path = f"./{name}"
  dir = os.path.dirname(path)
  if not os.path.exists(dir):
    os.makedirs(dir)
  with open(path, "wb") as f:
    f.write(response.content)

soup = BeautifulSoup(rss_data.text, "xml")

for item in soup.find_all("item"):
  print(item.title.text, item.link.text)
  download(item.title.text, item.link.text)

