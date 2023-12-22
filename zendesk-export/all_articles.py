import requests
import os
import json
import csv

i = 1
response = requests.get(f"https://support.metamask.io/api/v2/help_center/articles.json?page={i}")

data = response.json()

page_count = data["page_count"]

file = open("articles.csv", "w", newline="")
writer = csv.writer(file)
writer.writerow(["Article", "URL", "Section"])

for page in range(i, page_count):
    response = requests.get(f"https://support.metamask.io/api/v2/help_center/articles.json?page={i}")
    data = response.json()
    for article in data["articles"]:
        writer.writerow([article["title"], article["html_url"], article["section_id"]])
    i += 1