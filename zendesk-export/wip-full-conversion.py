import requests
import json
import os
import time
from bs4 import BeautifulSoup

def create_filepath(title, language, section_id):
    # Replace / with _
    title = title.replace("/", "_")

    # Fetch section information
    section_response = requests.get(f"https://support.metamask.io/api/v2/help_center/{language}/sections/{section_id}.json")
    section_data = section_response.json()
    section_name = section_data["section"]["name"].replace("/", "_")

    # Fetch category information
    category_id = section_data["section"]["category_id"]
    category_response = requests.get(f"https://support.metamask.io/api/v2/help_center/{language}/categories/{category_id}.json")
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
languages = ["en-us", "fr", "de", "es", "it"]

# Directory containing the local image files
directory_b = '/path/to/your/local/image/files'

# List of local image files
image_files = get_image_files(directory_b)
for language in languages:
    i = 1
    while True:
        response = requests.get(f"https://support.metamask.io/api/v2/help_center/{language}/articles.json?page={i}")
        data = response.json()

        # If the 'articles' key is not present in the response or there are no articles in the response, break the loop
        if 'articles' not in data or not data["articles"]:
            print(f"No more articles in page {i} for language {language}")
            break

        for article in data["articles"]:
            title = article["title"]
            # Replace / with _ in the title
            safe_title = title.replace("/", "_")
            filepath = create_filepath(safe_title, language, article["section_id"])
            with open(f"{filepath}/{safe_title}.html", "w") as file:
                # Load article body into BeautifulSoup
                soup = BeautifulSoup(article["body"], 'html.parser')

                # Convert images to specified format
                for img in soup.find_all('img'):
                    src = img.get('src')
                    alt = img.get('alt', '')

                    # Replace URL with local file path
                    image_file_name = os.path.basename(src)
                    local_image_file = next((f for f in image_files if os.path.basename(f) == image_file_name), None)
                    if local_image_file:
                        src = os.path.relpath(local_image_file, directory_b).replace("\\", "/")

                    # Replace whitespace and capital letters in file names
                    src = src.replace(" ", "-").lower()

                    # Create new img tag with specified format
                    new_img_tag = soup.new_tag('img', src=src, alt=alt)
                    img_medium_div = soup.new_tag('div', **{'class': 'img-medium'})
                    img_medium_div.append(new_img_tag)
                    center_container_div = soup.new_tag('div', **{'class': 'center-container'})
                    center_container_div.append(img_medium_div)

                    img.replace_with(center_container_div)

                # Convert tabbed content to Docusaurus format
                for tabs_div in soup.find_all('div', class_='tabs'):
                    # Create new Tabs tag
                    tabs = soup.new_tag('Tabs')

                    # Find all tab labels and tab content divs
                    tab_labels = tabs_div.find('div', class_='tabs-menu').find_all('span', class_='tabs-link')
                    tab_divs = tabs_div.find_all('div', class_='tab')

                    # Create a TabItem for each tab
                    for label, div in zip(tab_labels, tab_divs):
                        tab_item = soup.new_tag('TabItem', value=label.text, label=label.text)
                        tab_item.string = div.text
                        tabs.append(tab_item)

                    tabs_div.replace_with(tabs)

                # Write the modified HTML to the file
                file.write(str(soup))
            
        print(f"Page {i} in {language} complete")
        i += 1

        # Wait for 1 second before making the next request
        time.sleep(1)