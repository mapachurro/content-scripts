import requests
import json

response = requests.get('https://support.metamask.io/api/v2/locales.json')

data = response.json()

for locale in data['locales']:
    print(locale['locale'])