from django.shortcuts import render

# Create your views here.
def today(req):
    #API and weather code here

    return render(req,'wwapp/today.html')

def clouds(req):
    #API and weather code here

    return render(req,'wwapp/clouds.html')

def radar(req):
    #API and weather code here

    return render(req,'wwapp/radar.html')

def monthly(req):
    #API and weather code here

    return render(req,'wwapp/monthly.html')

def weekly(req):
    #API and weather code here

    return render(req,'wwapp/weekly.html')

def weekend(req):
    #API and weather code here

    return render(req,'wwapp/weekend.html')