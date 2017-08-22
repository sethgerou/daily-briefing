from flask import Flask, render_template
import scraping
import weather

application=Flask(__name__)

@application.route('/')
def index():
    return render_template("index.html")

@application.route('/headlines/')
def headlines():
    heads=scraping.get_headlines()
    return render_template("headlines.html", hls=heads)

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
