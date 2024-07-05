from django.urls import path
from . import views

app_name='weather_api'

urlpatterns = [
    path('',views.Weather.as_view(),name='weather'),
]
