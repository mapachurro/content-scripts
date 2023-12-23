import requests
import json
import os
from markdownify import markdownify as md

def create_filepath(title):
    # Replace / with _
    title = title.replace("/", "_")

    # Ensure the .markdown directory exists
    if not os.path.exists(".markdown"):
        os.mkdir(".markdown")

    # Create the article directory
    try:
        os.mkdir(f".markdown/{title}")
    except FileExistsError:
        print(f"Folder already exists")

    # Return the path of the created directory
    return f".markdown/{title}"

i = 1
while True:
    response = requests.get(f"https://support.metamask.io/api/v2/help_center/articles.json?page={i}")
    data = response.json()

    # If there are no articles in the response, break the loop
    if not data["articles"]:
        break

    for article in data["articles"]:
        title = article["title"]
        # Replace / with _ in the title
        safe_title = title.replace("/", "_")
        filepath = create_filepath(safe_title)
        with open(f"{filepath}/{safe_title}.md", "w") as file:
            md_file = md(article["body"])
            file.write(md_file)
        
    print(f"Page {i} complete")
    i += 1
