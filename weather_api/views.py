from django.shortcuts import render,redirect
from django.views.generic.base import View
from django.http import HttpRequest,HttpResponse,Http404,JsonResponse
import requests 
import datetime
import os
from django.contrib import messages
from decouple import config
# Create your views here.


class Weather(View):
    template_name='weather/weather.html'
    
    def get(self,request):
        return render(request,self.template_name)
    
    def post(self,request:HttpRequest):
        app_id=config('api_key')
        url1='http://api.openweathermap.org/data/2.5/weather?appid={}&q={}'
        url2='http://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}'
        
        try:
            city=request.POST.get('city','')
        except:
            messages.info(request,'enter the city name ...')
            return render(request,self.template_name,)
        else:
            try:
                response1=requests.get(url1.format(app_id,city))
                content1=response1.json()     
                lat=content1['coord']['lat']
                lon=content1['coord']['lon']
                
                city_weather={
                'city':city,
                'temperature':round(content1['main']['temp']-273.15,2),
                'description':content1['weather'][0]['description'],
                'icon':content1['weather'][0]['icon']
                }
                
                
                forcast_daliy=[]
                response2=requests.get(url2.format(lat,lon,app_id))
                content2=response2.json()
                
                for day in content2['daily'][1:7]:
                    forcast_daliy.append({
                        'day':datetime.datetime.fromtimestamp(day['dt']).strftime('%A'),
                        'temperature':round(day['temp']['day']-273.15,2),
                        'description':day['weather'][0]['description'],
                        'icon':day['weather'][0]['icon'],
                    })
                
                context={
                    'city_weather':city_weather,
                    'forcast_daily':forcast_daliy,
                }
            
            except KeyError:
                messages.info(request,'please enter city name...')
                return redirect("weather_api:weather")


        return render(request,self.template_name,context)


