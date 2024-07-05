from django.urls import path
from . import views

app_name='weather_api'

urlpatterns = [
    path('weather/',views.Weather.as_view(),name='weather'),
]
