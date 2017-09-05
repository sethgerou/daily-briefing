import requests
from keys import wunderground

def get_weather(zc="98019"):
    wujson = requests.get("http://api.wunderground.com/api/%s/conditions/forecast/q/%s.json" % (wunderground, zc))
    wdata = wujson.json()

    current = wdata['current_observation']

    curtemp = current['temp_f']
    curhum = current['relative_humidity']
    curcond = current['weather']
    curwins = current['wind_mph']
    curwdir = current['wind_dir']

    cur_display_data = (curtemp, curhum, curcond, curwins, curwdir)

    fcast_display_data = []

    days = wdata['forecast']['simpleforecast']['forecastday']

    for day in days:

        fcast_display_data.append(
            {
            'weekday': day['date']['weekday'],
            'cond': day['conditions'],
            'high': day['high']['fahrenheit'],
            'low': day['low']['fahrenheit'],
            'precip': day['qpf_allday']['in']
            }
        )

    return (cur_display_data, fcast_display_data)
