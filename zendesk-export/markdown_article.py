import requests
import json
from markdownify import markdownify as md

id = input("Article ID: ")

response = requests.get(f"https://support.metamask.io/api/v2/help_center/articles/{id}/")

data = response.json()
article = data["article"]
title = article["title"]

with open(f"{title}.md", "w") as file:
    md_file = md(article["body"])
    file.write(md_file)