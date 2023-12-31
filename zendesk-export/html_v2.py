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

def get_sections(locale, parent_id):

  if locale not in section_cache:
    section_cache[locale] = {}

  if parent_id in section_cache[locale]:  
    return section_cache[locale][parent_id]

  # API call

  section_cache[locale][parent_id] = sections

  return sections

def get_categories(locale):
  url = CATEGORIES_URL.format(locale=locale)
  response = requests.get(url)
  data = response.json()
  return data['categories']
  
def get_sections(locale, parent_id):
    # include locale in id to fetch correct cache, to avoid applying the wrong locale's section cache
  key = f"{locale}_{parent_id}"

    # Check cache
  if key in section_cache:
    return section_cache[key]

  url = SECTIONS_URL.format(locale=locale, category_id=parent_id)

  response = requests.get(url)
  data = response.json()

  sections = data['sections']

# Recursively search sections
  for section in sections:
    print(f'- {len(sections)} sections found')

    subsections = section.get('subsections')

    if not subsections:
        return sections
    
    #Fetch subsections
    more_sections = get_sections(locale, section['id'])
    
    #Merge them
    sections.extend(more_sections)

    print(f'- {len(subsections)} subsections found')

# Cache results
  section_cache[key] = sections

  return sections

def get_articles(locale, section_id):

  page = 1
  
  while True:
  
    url = ARTICLES_URL.format(locale=locale, section_id=section_id, page=page)
    response = requests.get(url)
    
    data = response.json()
    articles = data['articles']
    
    if not articles:
      break

    yield articles

    page += 1

def get_subsections(locale, section_id):

  url = SECTIONS_URL.format(locale=locale, category_id=section_id)

  response = requests.get(url)
  
  data = response.json()

  response = requests.get(url)
  data = response.json()

  print(data)

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
for locale in locales:

  categories = get_categories(locale)

  if categories:

    locale_dir = os.path.join(output_dir, locale)
    os.makedirs(locale_dir, exist_ok=True)

    for category in categories:

      # Sanitize category name  
      cat_name = sanitize_filename(category['name'])
      
      cat_dir = os.path.join(locale_dir, cat_name)
      os.makedirs(cat_dir, exist_ok=True)

      sections = get_sections(locale, category['id'])

      if sections:

        for section in sections:
          
          subsections = get_subsections(locale, section['id'])
        
          # Sanitize section name
          sec_name = sanitize_filename(section['name'])       

          for subsection in subsections:

            # Sanitize subsection name
            sub_name = sanitize_filename(section['name'])

            # Use subsection name
            sub_dir = os.path.join(cat_dir, sub_name)
            os.makedirs(sub_dir, exist_ok=True)

            articles = get_articles(subsection['id'])
    
            for page in articles:
                    
                for article in page:
  
                # Sanitize title
                 title = sanitize_filename(article['title'])

                 # Write file
                 file_path = os.path.join(sub_dir, f"{title}.html")
                 with open(file_path, 'w') as f:
                  f.write(article['body'])

                print(f"Wrote {file_path}")
          
print("Done!")