import requests
import json
import os
from markdownify import markdownify as md

def create_filepath(title, language):
    # Replace / with _
    title = title.replace("/", "_")

    # Ensure the language directory exists
    if not os.path.exists(f".markdown/{language}"):
        os.mkdir(f".markdown/{language}")

    # Create the article directory
    try:
        os.mkdir(f".markdown/{language}/{title}")
    except FileExistsError:
        print(f"Folder already exists")

    # Return the path of the created directory
    return f".markdown/{language}/{title}"

# List of languages you want to fetch articles in
languages = [
    "ar-eg",
    "ar",
    "ms",
    "bg",
    "ca",
    "sr-me",
    "da",
    "de",
    "de-at",
    "de-ch",
    "et",
    "en-US",
    "en-au",
    "en-be",
    "en-ca",
    "en-ie",
    "en-in",
    "en-nz",
    "en-ph",
    "en-sg",
    "en-za",
    "en-gb",
    "es",
    "es-es",
    "es-419",
    "es-mx",
    "fil",
    "fr",
    "fr-be",
    "fr-ca",
    "fr-ch",
    "hr",
    "id",
    "it",
    "lv",
    "lt",
    "hu",
    "nl-be",
    "nl",
    "no",
    "fa",
    "pl",
    "pt-br",
    "pt",
    "ro",
    "ro-ro",
    "sk",
    "sl",
    "sr",
    "fi",
    "sv",
    "th",
    "tr",
    "vi",
    "fr-fr",
    "is",
    "cs",
    "el",
    "ru",
    "uk",
    "he",
    "hi",
    "ja",
    "zh-cn",
    "zh-tw",
    "ko"
]

for language in languages:
    i = 1
    while True:
        response = requests.get(f"https://support.metamask.io/api/v2/help_center/{language}/articles.json?page={i}")
        data = response.json()

        # If the 'articles' key is not present in the response or there are no articles in the response, break the loop
        if 'articles' not in data or not data["articles"]:
            break

        for article in data["articles"]:
            title = article["title"]
            # Replace / with _ in the title
            safe_title = title.replace("/", "_")
            filepath = create_filepath(safe_title, language)
            with open(f"{filepath}/{safe_title}.md", "w") as file:
                md_file = md(article["body"])
                file.write(md_file)
            
        print(f"Page {i} in {language} complete")
        i += 1