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
  name = re.sub(r'[^\w\s-]', '', name).strip().lower()
  return name

def get_categories(locale):
  url = CATEGORIES_URL.format(locale=locale)
  response = requests.get(url)
  data = response.json()
  return data['categories']

def get_sections(locale, category_id):
  url = SECTIONS_URL.format(locale=locale, category_id=category_id)
  response = requests.get(url)
  data = response.json()
  return data['sections']

def get_articles(locale, section_id):
  url = ARTICLES_URL.format(locale=locale, section_id=section_id)
  response = requests.get(url)
  data = response.json()
  return data['articles']

# Loop through locales
for locale in locales:

  print(f'Processing {locale}')

  # Fetch categories
  categories = get_categories(locale)

  if categories:

    print(f'- {len(categories)} categories found')

    locale_dir = os.path.join(output_dir, locale)
    os.makedirs(locale_dir, exist_ok=True)

  # Loop through categories
    for category in categories:
        
        # Fetch sections
        sections = get_sections(locale, category['id'])
        print(f'- {len(sections)} sections found')
        
        # Check for sections
        if sections:

            # Category dir
                cat_dir = os.path.join(locale_dir, category['name'])
                os.makedirs(cat_dir, exist_ok=True)

                # Loop through sections
                for section in sections:
                        section_articles = get_articles(locale, section['id'])
                        print(f'- {len(section_articles)} section articles')

                        section_id = section['id']
                        section_name = sanitize_filename(section['name'])   

                        print(f"  - Section: {section_name}")

                        # Section dir
                        sec_dir = os.path.join(cat_dir, section['name'])
                        os.makedirs(sec_dir, exist_ok=True)

                        articles = get_articles(locale, section['id'])
                        print(f'- {len(articles)} articles found')

                        if not articles:
                            continue     

                        # Create section dir
                        sec_dir = os.path.join(cat_dir, section['name'])

                        articles = get_articles(locale, section['id'])
                

                        # Write articles
                        for article in articles:
        
                        # Check for empty articles
                            if not article:
                                print(f'No articles found for section {section_id}')
                            continue 

                        title = sanitize_filename(article['title'])
                        body = article['body']
                       
                    # Write HTML file
                file_path = os.path.join(sec_dir, f"{title}.html")
                with open(file_path, 'w') as f:
                  f.write(body)
        
                print(f"    - Wrote file: {file_path}")
        
                # Wait
                time.sleep(1)

print('Done!')