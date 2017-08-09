from bs4 import BeautifulSoup
import requests

def get_weather(zip):
    current_raw=requests.get('https://www.wunderground.com/cgi-bin/findweather/getForecast?query=%s' % zip)
    c=current_raw.content
    soup=BeautifulSoup(c, "html.parser")
    curr_cond=get_current_conditions(soup)
    fcast=get_forecast(soup)
    return (curr_cond, fcast)

def get_current_conditions(soup):
    temp_container=soup.find("div", {"id":"curTemp"})
    current_temp=temp_container.find("span", {"class":"wx-value"}).text

    cond_container=soup.find("div", {"id":"curCond"})
    current_cond=cond_container.find("span", {"class":"wx-value"}).text

    wspd_container=soup.find("div", {"id":"windCompassSpeed"})
    current_wspd=wspd_container.find("span", {"class":"wx-value"}).text

    wdir_container=soup.find("div", {"id":"windDir"})
    current_wdir=wdir_container.find("span", {"class":"wx-value"}).text

    return (current_temp, current_cond, current_wspd, current_wdir)

def get_forecast(soup):
    r=requests.get("https://forecast.weather.gov/MapClick.php?lat=47.7773&lon=-121.6456&unit=0&lg=english&FcstType=text&TextType=2")
    c=r.content
    soup=BeautifulSoup(c, "html.parser")
    table=soup.find_all("table")[1]
    graphical=table.find_all("tr")[0]
    img=graphical.find_all("img")
    forecast=[]
    for i in img:
        forecast.append(i['alt'])
    return forecast

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
