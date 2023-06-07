from django.shortcuts import render
import urllib.request
import json
import datetime

def index(request):
    if request.method == "POST":
        city = request.POST['city']
        API_KEY = open('config.py', 'r').read()
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                        city + '&units=imperial&appid=' + API_KEY).read()
        list_of_data = json.loads(source)
        lat = str(list_of_data['coord']['lat'])
        lon = str(list_of_data['coord']['lon'])
        source2 = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?lat=' +
                                         lat + '&lon=' + lon + '&units=imperial&appid=' + API_KEY).read()
        list_of_forecasts = json.loads(source2)
        print(list_of_forecasts)
        forecasts = []
        data = {
            "city": request.POST['city'],
            "day": datetime.datetime.fromtimestamp(list_of_data['dt']).strftime("%A"),
            "temp": str(list_of_data['main']['temp']) + '°F',
            "feels_like": str(list_of_data['main']['feels_like']) + '°F',
            "main": str(list_of_data['weather'][0]['main']),
            "description": str(list_of_data['weather'][0]['description']),
            "icon": str(list_of_data['weather'][0]['icon']),
            "clouds": str(list_of_data['clouds']['all']),
        }
        if 'rain' in str(list_of_data['weather'][0]):
            data['rain'] = str(list_of_data['rain']['1h'])
        if 'snow' in str(list_of_data['weather'][0]):
            data['snow'] = str(list_of_data['snow']['1h'])
        for forecast in list_of_forecasts['list'][::8]:
            timestamp = forecast['dt']
            day_name = datetime.datetime.fromtimestamp(timestamp).strftime("%A")
            forecasts.append({
                "day": day_name,
                "temp": str(forecast['main']['temp']) + '°F',
                "feels_like": str(forecast['main']['feels_like']) + '°F',
                "main": str(forecast['weather'][0]['main']),
                "description": str(forecast['weather'][0]['description']),
                "icon": str(forecast['weather'][0]['icon']),
                "clouds": str(forecast['clouds']['all']),
            })
        data['forecasts'] = forecasts[1:]
    else:
        data = {}
    return render(request, "main/index.html", data)
