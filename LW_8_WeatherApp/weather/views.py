import requests
from django.shortcuts import render

# Create your views here.

def index(request):
    appid = '759d711629b03e0bfec9637c86390e2c'
    url=('https://api.openweathermap.org/data/2.5/'
         'weather?q={}&units=metric&appid='+appid)

    cities = {
        'London',
        'Rostov-On-Don',
        'Moscow',
        'New York',
        'Saint Petersburg'
    }

    cit = []

    for city in cities:
        res = requests.get(url.format(city)).json()

        city_info = {
            'city':city,
            'temp': res['main']['temp'],
            'wind': res['wind']['speed'],
            'cloud': res['clouds']['all'],
            'icon': res['weather'][0]['icon']
        }
        cit.append(city_info)

    context = {'info':cit}


    return render(request, 'index.html', context)
