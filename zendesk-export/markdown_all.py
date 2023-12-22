import requests
import json
import os
from markdownify import markdownify as md

def create_filepath(title):
    try:
        os.mkdir(f".markdown/{title}")
    except FileExistsError:
        print(f"Folder already exists")

i = 1
response = requests.get(f"https://support.metamask.io/api/v2/help_center/articles.json?page={i}")

data = response.json()

page_count = data["page_count"]

for i in range(0, page_count):
    page = i + 1
    data = response.json()
    for article in data["articles"]:
        title = article["title"]
        filepath = create_filepath(title)
        with open(f"{filepath}/{title}.md", "w") as file:
            md_file = md(article["body"])
            file.write(md_file)
        
    print(f"Page {i + 1} complete")
