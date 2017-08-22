import requests

def get_weather(zip="98019"):
    wujson = requests.get("http://api.wunderground.com/api/<weather_underground_api_key>/conditions/forecast/q/%s.json" % zip)
    wdata = wujson.json()

    current = wdata['current_observation']

    curtemp = current['temp_f']
    curhum = current['relative_humidity']
    curcond = current['weather']
    curwins = current['wind_mph']
    curwdir = current['wind_dir']

    cur_display_data = (curtemp, curhum, curcond, curwins, curwdir)

    fcast_display_data = {}

    days = wdata['forecast']['simpleforecast']['forecastday']

    for day in days:
        weekday = day['date']['weekday']
        fcast_display_data[weekday] = {
            'cond': day['conditions'],
            'high': day['high']['fahrenheit'],
            'low': day['low']['fahrenheit'],
            'precip': day['qpf_allday']['in']
        }

    return (cur_display_data, fcast_display_data)
