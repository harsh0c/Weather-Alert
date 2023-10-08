from django.shortcuts import render

from dotenv import load_dotenv
import os
import requests

load_dotenv()

from . models import CityData,AlertData
# Create your views here.


def index(request):
    if request.method == 'POST':

        city = request.POST['city']
        mintemp = request.POST['mintemp']
        maxtemp = request.POST['maxtemp']
        if CityData:
            CityData.objects.all().delete()
        
        c=CityData()
        c.name=city
        c.mintemp=mintemp
        c.maxtemp=maxtemp
        c.save()

        weather_API_KEY = os.environ.get('WEATHER_API_KEY')
        
        # source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid='+weather_API_KEY).read()
        # print(source)
        # response = json.loads(source)
        response=requests.get(url='http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid='+weather_API_KEY).json()

        try :
            
            data = {
                "country_code": str(response['sys']['country']),
                "coordinate": str(response['coord']['lon']) + ', '
                + str(response['coord']['lat']),

                "temp": str(response['main']['temp']) + ' °C',
                "pressure": str(response['main']['pressure']),
                "humidity": str(response['main']['humidity']),
                'main': str(response['weather'][0]['main']),
                'description': str(response['weather'][0]['description']),
                'icon': response['weather'][0]['icon'],
                'city': city,
                'exception_occured': False
            }

            if AlertData:
                msgData=AlertData.objects.first()
                if msgData:
                    message=str(msgData.alertmsg)
                    data['alertmsg']=message
            # print(data)
        except:
            data={}
            data['exception_occured']=True
        

    else:
       data={}
    
    return render(request,"walert/index.html",data)