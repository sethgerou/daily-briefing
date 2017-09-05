from flask import Flask, render_template
import scraping
import weather
from datetime import datetime
from headlines import get_articles

application=Flask(__name__)

@application.route('/')
def index():
    formatted_datetime = datetime.now().strftime("%A, %B%e, %G")
    return render_template("index.html", current_date=formatted_datetime)

@application.route('/headlines/<src>')
def headlines(src):
    heads=get_articles(src)
    return render_template("headlines.html", hls=heads, src=src)

@application.route('/weather/')
def current():
    curr=weather.get_weather(98019)
    return render_template("weather.html", curr=curr[0])

@application.route('/forecast/')
def forecast():
    fcast=weather.get_weather(98019)
    return render_template("forecast.html", fcast=fcast[1])

@application.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    application.debug = True
    application.run()
