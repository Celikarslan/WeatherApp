from django.shortcuts import render
# Create your views here.

import urllib.request
import json

def index(request):
    if request.method == "POST":
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + 
                                        city + '&units=imperial&appid=<YOUR API HERE>').read()
        list_of_data = json.loads(source)
        
        data ={
            "city": request.POST['city'],
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
    return render(request, "main/index.html", data)