import requests
import json
import os
import time
import re
from markdownify import markdownify as md
from bs4 import BeautifulSoup


def create_filepath(title, language, section_id):
    # Replace / with _
    title = title.replace("/", "_")

    # Fetch section information
    section_response = requests.get(
        f"https://support.metamask.io/api/v2/help_center/{language}/sections/{section_id}.json"
    )
    section_data = section_response.json()
    section_name = section_data["section"]["name"].replace("/", "_")

    # Fetch category information
    category_id = section_data["section"]["category_id"]
    category_response = requests.get(
        f"https://support.metamask.io/api/v2/help_center/{language}/categories/{category_id}.json"
    )
    category_data = category_response.json()
    category_name = category_data["category"]["name"].replace("/", "_")

    # Ensure the language directory exists
    if not os.path.exists(f".html/{language}"):
        os.mkdir(f".html/{language}")

    # Ensure the category directory exists
    if not os.path.exists(f".html/{language}/{category_name}"):
        os.mkdir(f".html/{language}/{category_name}")

    # Ensure the section directory exists
    if not os.path.exists(f".html/{language}/{category_name}/{section_name}"):
        os.mkdir(f".html/{language}/{category_name}/{section_name}")

    # Create the article directory
    try:
        os.mkdir(f".html/{language}/{category_name}/{section_name}/{title}")
    except FileExistsError:
        print(f"Folder already exists")

    # Return the path of the created directory
    return f".html/{language}/{category_name}/{section_name}/{title}"


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
    "en-us",
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
    "ko",
]

# Directory containing the local image files
directory_b = "./../static/img/"

# List of local image files
image_files = get_image_files(directory_b)


def sanitize_filename(filename):
    # Replace spaces with hyphens
    filename = filename.replace(" ", "-")
    # Convert to lowercase
    filename = filename.lower()
    # Remove apostrophes
    filename = filename.replace("'", "")
    # Replace double dashes with single dash
    filename = filename.replace("--", "-")
    # Remove question marks
    filename = filename.replace("?", "")
    # Remove colons
    filename = filename.replace(":", "")
    # Remove semicolons
    filename = filename.replace(";", "")
    # Remove parentheses
    filename = filename.replace("(", "").replace(")", "")
    # Remove any other special characters
    filename = re.sub(r"[^a-zA-Z0-9\-]", "", filename)
    return filename


for language in languages:
    i = 1
    while True:
        response = requests.get(
            f"https://support.metamask.io/api/v2/help_center/{language}/articles.json?page={i}"
        )
        data = response.json()

        # If the 'articles' key is not present in the response or there are no articles in the response, break the loop
        if "articles" not in data or not data["articles"]:
            print(f"No more articles in page {i} for language {language}")
            break

        for article in data["articles"]:
            title = article["title"]
            # Replace / with _ in the title
            safe_title = title.replace("/", "_")
            # Sanitize the filename
            filename = sanitize_filename(safe_title)
            filepath = create_filepath(filename, language, article["section_id"])
            with open(f"{filepath}/{filename}.mdx", "w") as file:
                # Add front matter with original title
                front_matter = f"---\ntitle: '{title}'\n---\n\n"
                file.write(front_matter)

                # Load article body into BeautifulSoup
                soup = BeautifulSoup(article["body"], "html.parser")

                # Convert images to specified format
                for img in soup.find_all("img"):
                    src = img.get("src")
                    alt = img.get("alt", "")

                    # Replace URL with local file path
                    image_file_name = os.path.basename(src)
                    local_image_file = next(
                        (
                            f
                            for f in image_files
                            if os.path.basename(f) == image_file_name
                        ),
                        None,
                    )
                    if local_image_file:
                        src = os.path.relpath(local_image_file, directory_b).replace(
                            "\\", "/"
                        )

                    # Replace whitespace and capital letters in file names
                    src = src.replace(" ", "-").lower()

                    # Create new img tag with specified format
                    new_img_tag = soup.new_tag("img", src=src, alt=alt)
                    img_medium_div = soup.new_tag("div", **{"class": "img-medium"})
                    img_medium_div.append(new_img_tag)
                    center_container_div = soup.new_tag(
                        "div", **{"class": "center-container"}
                    )
                    center_container_div.append(img_medium_div)

                    img.replace_with(center_container_div)

                # Convert tabbed content to Docusaurus format
                for tabs_div in soup.find_all("div", class_="tabs"):
                    # Create new Tabs tag
                    tabs = soup.new_tag("Tabs")

                    # Find all tab labels and tab content divs
                    tab_labels = tabs_div.find("div", class_="tabs-menu").find_all(
                        "span", class_="tabs-link"
                    )
                    tab_divs = tabs_div.find_all("div", class_="tab")

                    # Create a TabItem for each tab
                    for label, div in zip(tab_labels, tab_divs):
                        tab_item = soup.new_tag(
                            "TabItem", value=label.text, label=label.text
                        )
                        tab_item.string = div.text
                        tabs.append(tab_item)

                    tabs_div.replace_with(tabs)

                # Convert callouts to Docusaurus format
                for callout in soup.find_all("div", class_="callout"):
                    # Determine the type of the callout based on its classes
                    if "callout--info" in callout["class"]:
                        callout_type = "info"
                    elif "callout--transparent" in callout["class"]:
                        callout_type = "note"  # Map to a Docusaurus type
                    elif "callout--success" in callout["class"]:
                        callout_type = "tip"  # Map to a Docusaurus type
                    elif "callout--warning" in callout["class"]:
                        callout_type = "warning"
                    elif "callout--danger" in callout["class"]:
                        callout_type = "danger"
                    elif "callout--primary" in callout["class"]:
                        callout_type = "info"  # Map to a Docusaurus type
                    else:
                        callout_type = "note"  # Default type

                    # Find the title and content of the callout
                    title = callout.find(class_="callout__title").text
                    content = callout.find("p").text

                    # Create new admonition with specified format
                    admonition = soup.new_tag("div")
                    admonition.string = (
                        f":::{callout_type}[{title}]\n\n{content}\n\n:::"
                    )

                    callout.replace_with(admonition)

    # Write the modified HTML to the file
    file.write(str(soup))

    print(f"Page {i} in {language} complete")
    i += 1

    # Wait for 1 second before making the next request
    time.sleep(1)
