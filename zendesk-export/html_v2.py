import requests
import json
import os
import re
import time

# API URLs
CATEGORIES_URL = 'https://support.metamask.io/api/v2/help_center/{locale}/categories.json'  
SECTIONS_URL = 'https://support.metamask.io/api/v2/help_center/{locale}/categories/{category_id}/sections.json'
ARTICLES_URL = 'https://support.metamask.io/api/v2/help_center/{locale}/sections/{section_id}/articles.json'

# List of locales
locales = [
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
  "ko"
]

output_dir = 'output'

def sanitize_filename(name):
  name = name.replace(' ', '-')
  name = name.replace('/', '-') 
  name = name.replace('?', '')
  # etc for other chars
  
  name = re.sub(r'[^\w\s-]', '', name).strip().lower()
  
  return name

# Cache section info to reduce API calls
section_cache = {}

def get_sections(locale, category_id):

  key = f"{locale}_{category_id}"

  if key in section_cache:
    return section_cache[key]

  # API call
  url = SECTIONS_URL.format(locale=locale, category_id=category_id)
  
  response = requests.get(url)

  sections = response.json()['sections']

  # Cache 
  section_cache[key] = sections

  return sections

def get_categories(locale):
  url = CATEGORIES_URL.format(locale=locale)
  response = requests.get(url)
  data = response.json()
  print(f'Locale: {locale}, Categories: {data}')  # print response data
  return data['categories']

downloaded_articles = []

try:
  with open('downloaded.json') as f:
    downloaded_articles = json.load(f)
    downloaded_articles = set(downloaded_articles)
except FileNotFoundError:
   pass # File not created yet
   
# Run script

with open('downloaded.json', 'w') as f:
  json.dump(downloaded_articles, f) 

def get_articles(locale, section_id):

  page = 1
  while True:
    url = ARTICLES_URL.format(locale=locale, section_id=section_id, page=page)
    
    print(f"Requesting {url}")
    
    response = requests.get(url)
    data = response.json()

    articles = data['articles']

    if not articles:
        break
    
    for article in articles:
        if article['id'] in downloaded_articles:
           continue
        
        # Add article id to set
        downloaded_articles.add(article['id'])

        yield article

    # Increment page number    
    page += 1  

    # Check for next_page
    if not data.get('next_page'):
        break

    time.sleep(1)

  # Convert article set to list
  downloaded_articles_list = list(downloaded_articles)
  # Save list to JSON
  with open('downloaded.json', 'w') as f:
   json.dump(downloaded_articles_list, f)
 
def write_articles(locale, section_dir, articles):

  for article in articles:
    # Sanitize title
    title = sanitize_filename(article['title'])

    # Write file
    file_path = os.path.join(section_dir, f"{title}.html")
    with open(file_path, 'w') as f:
        f.write(article['body'])

    print(f"Wrote article '{title}' to {file_path}")

# Loop through locales
for locale in locales:
  
  # Fetch categories
  categories = get_categories(locale)

  if not categories:
    continue

  print(f'Processing {locale}')

  locale_dir = os.path.join(output_dir, locale)
  os.makedirs(locale_dir, exist_ok=True)

  print(f'- {len(categories)} categories found')

  # Loop through categories
  for category in categories:
    
    cat_dir = os.path.join(locale_dir, sanitize_filename(category['name']))
    os.makedirs(cat_dir, exist_ok=True)

    sections = get_sections(locale, category['id'])

    for section in sections:

      section_dir = os.path.join(cat_dir, sanitize_filename(section['name'])) 
      os.makedirs(section_dir, exist_ok=True)

      #Write articles
      articles = list(get_articles(locale, section['id']))
      print(f'Section directory: {section_dir}')
      write_articles(locale, section_dir, articles)
          
print("Done!")
