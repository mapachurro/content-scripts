import os
from bs4 import BeautifulSoup

def find_callouts(directory):
    # Set to store unique callout types
    callout_types = set()

    # Walk through all files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    soup = BeautifulSoup(f, 'html.parser')

                    # Find all callouts and add their types to the set
                    for callout in soup.find_all('div', class_='callout'):
                        callout_type = next((cls for cls in callout['class'] if cls.startswith('callout--')), None)
                        if callout_type:
                            callout_types.add(callout_type)

    # Print all unique callout types
    for callout_type in callout_types:
        print(callout_type)

# Provide the path of the directory with HTML files
directory = './../zendesk-export/.html/en-us/'

# Call the function to find callouts in the HTML files
find_callouts(directory)