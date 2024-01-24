downloaded_articles = set()

# Load
if os.path.exists('downloaded.json'):
  #load file
  with open('downloaded.json', 'r') as f:
    downloaded_articles = json.load(f)
else:
  downloaded_articles = set()

# Convert back to set
downloaded_articles = set(downloaded_articles)
