from flask import Flask, render_template
import scraping

app=Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/headlines/')
def headlines():
    heads=scraping.get_headlines()
    return render_template("headlines.html", hls=heads)

@app.route('/weather/')
def current():
    curr=scraping.get_weather(98019)
    return render_template("weather.html", curr=curr[0])

@app.route('/forecast/')
def forecast():
    fcast=scraping.get_weather(98019)
    print(fcast[1])
    return render_template("forecast.html", fcast=fcast[1])

if __name__ == "__main__":
    app.run(debug=True)
