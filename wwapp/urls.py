from django.urls import path

from . import views

urlpatterns = [
    path('', views.today, name="today"),
    path("clouds",views.clouds,name="clouds"),
    path("radar",views.radar,name="radar"),
    path("weekend",views.weekend,name="weekend"),
    path("weekly",views.weekly,name="weekly")
]