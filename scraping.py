from bs4 import BeautifulSoup
import requests

def get_headlines():
    r=requests.get("http://www.msnbc.com")
    c=r.content
    soup=BeautifulSoup(c, "html.parser")
    all=soup.find_all("h2", {"class":"featured-slider__teaser__title"})
    headlines={}
    for a in all:
        if "www" in a.find("a", href=True)['href']:
            headlines[a.a.text]=a.find("a", href=True)['href']
        else:
            headlines[a.a.text]="http://www.msnbc.com" + a.find("a", href=True)['href']
    return headlines
