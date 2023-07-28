#!/usr/bin/python3

import os
import re
from beautifulsoup4 import BeautifulSoup

def fix_links(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                fix_file_links(file_path)

def fix_file_links(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # Use BeautifulSoup to parse the Markdown content
    soup = BeautifulSoup(content, 'html.parser')

    # Find all anchor tags
    for link in soup.find_all('a'):
        href = link.get('href')

        # Check if the link is a relative link to an .md file
        if href and not href.startswith(('http', '/', '#')) and href.endswith('.md'):
            new_href = update_link_href(href, file_path)
            link['href'] = new_href

    # Update the content with the modified links
    content = str(soup)

    with open(file_path, 'w') as f:
        f.write(content)

def update_link_href(href, file_path):
    file_directory = os.path.dirname(file_path)
    linked_file_path = os.path.join(file_directory, href)

    # Get the relative path of the linked file from the current file's directory
    relative_path = os.path.relpath(linked_file_path, file_directory)
    relative_path = relative_path.replace('\\', '/')

    return relative_path.replace('.md', '.html')

# Provide the path of the root directory containing the content
root_directory = '/home/mapachurro/mm-hc/docs-mm-helpcenter/docs'

# Call the function to fix the links in the content
fix_links(root_directory)
