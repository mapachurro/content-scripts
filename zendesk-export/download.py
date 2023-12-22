import requests
import json
import os

# Access API
page = 1
response = requests.get(f"https://support.metamask.io/api/v2/help_center/articles.json?page={page}&per_page=50")

# Get article to be downloaded 
id = str(input("Article ID: "))
id = id.strip()

# Convert to JSON
data = response.json()

# Locate and save article
page_count = data["page_count"]

for i in range(0, page_count):
    page = i + 1
    data = response.json()
    for article in data["articles"]:
        if article["id"] == id:
            print("Found article")
            file = open(f"{id}.json", "w")
            file.write(article["body"])
            print(f"Success: article saved to {os.getcwd} as {id}.json")
    print(f"Page {i + 1} searched")

print("Operation complete")