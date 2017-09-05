import requests
from keys import newsapi

def get_articles(src):
    raw = requests.get("https://newsapi.org/v1/articles?source=%s&sortBy=top&apiKey=%s" % (src, newsapi))
    data = raw.json()
    return data['articles']
