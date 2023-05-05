import requests
from django.shortcuts import render

#NDZ039
#NDZ017
#The urls for the api and the header for the request.
url1 = 'https://api.weather.gov/gridpoints/FGF/100,55/forecast/'
url2 = 'https://api.weather.gov/gridpoints/FGF/100,55'
fireAlertsUrl = 'https://api.weather.gov/alerts/active/zone/NDZ039'
cassCountyAlertsUrl = 'https://api.weather.gov/alerts/active/zone/NDC017'
header = {
    'Content-Type':'application/geo+json',
    'Accept':'application/geo+json',
    'token':"Access Token",
    'User-Agent':'weatherApp',
}

#Some of the values are metric. This takes a temp in metric as an input and returns
#the temp in F rounded to the nearest degree
def unitConv(tempInC):
    return round((tempInC * 1.8) + 32)

#this function takes a url and header as input and returns a response from the url provided if the
#url returned code 200, otherwise it returns None.
def getResponse(url,h):
    print(url)
    response = requests.get(url,headers=h)
    if response.status_code == 200:
        #print("success")
        return response
    else:
        #print("failed with: " + str(response.status_code)) 
        return None

def today(request):
    response = getResponse(url2,header).json() #Pull data from url1 (forcast)
    response2 = getResponse(url1,header).json() #Pull data from url2 (Fargo Station)
    response3 = getResponse(cassCountyAlertsUrl,header).json()
    
    alerts = []

    for a in response3['features']:
        alerts.append((a['properties']['headline'],a['properties']['description']))

    data = {
        'dailyHigh':unitConv(response['properties']["maxTemperature"]['values'][0]['value']),
        'dailyLow':unitConv(response['properties']["minTemperature"]['values'][0]['value']),
        'dewPoint':unitConv(response['properties']['dewpoint']['values'][0]['value']),
        'humidity':response['properties']["relativeHumidity"]['values'][0]['value'],
        'feelsLike':unitConv(response['properties']["apparentTemperature"]['values'][0]['value']),
        'windChill': response['properties']["windChill"]['values'][0]['value'],
        'skyCover':response['properties']["skyCover"]['values'][0]['value'], #percent,
        'windDirection':response['properties']["windDirection"]['values'][0]['value'], #angle in degrees,
        'windSpeed':response['properties']["windSpeed"]['values'][0]['value'], #km/hr
        'windGusts':response['properties']["windGust"]['values'][0]['value'],
        'chanceOfPrecip':response['properties']["probabilityOfPrecipitation"]['values'][0]['value'], #percent
        'amountOfPrecip':response['properties']["quantitativePrecipitation"]['values'][0]['value'],
        'snowFallAmmount':response['properties']["snowfallAmount"]['values'][0]['value'],
        'currentTemp':response2['properties']['periods'][0]['temperature'],
        'shortF': response2['properties']['periods'][0]['shortForecast'],
        'detailF': response2['properties']['periods'][0]['detailedForecast'],
        'alerts' : alerts,
    }

    return render(request, 'wwapp/today2.html', context={'data':data})

def clouds(req):
    return render(req,'wwapp/clouds.html')

def radar(req):
    return render(req,'wwapp/radar.html')


def weekly(req):
    #API and weather code here

    return render(req,'wwapp/weekly.html')

def weekend(req):
    response = getResponse(url1,header).json()
    data = {}
    days = response["properties"]["periods"]

    friday = [ day for day in days if day["name"]=="Friday"]
    if len(friday)==0:
        friday = [ day for day in days if day["name"]=="Today"]
    if len(friday)==0:
        friday = [ day for day in days if day["name"]=="This Afternoon"]
    if len(friday)==0:
        friday = [ day for day in days if day["name"]=="Tonight"]
    friday = friday[0]  

    saturday = [ day for day in days if day["name"]=="Saturday"]
    if len(saturday)==0:
        saturday = [ day for day in days if day["name"]=="Today"]
    if len(saturday)==0:
        saturday = [ day for day in days if day["name"]=="This Afternoon"]
    if len(saturday)==0:
        saturday = [ day for day in days if day["name"]=="Tonight"]
    saturday = saturday[0]
    
    sunday = [ day for day in days if day["name"]=="Sunday"]
    if len(sunday)==0:
        sunday = [ day for day in days if day["name"]=="Today"]
    if len(sunday)==0:
        sunday = [ day for day in days if day["name"]=="This Afternoon"]
    if len(sunday)==0:
        sunday = [ day for day in days if day["name"]=="Tonight"]
    sunday = sunday[0]

    data["friday"] = {
        "temp":friday["temperature"],
        "wind":friday["windSpeed"]+" "+friday["windDirection"],
        "precipitation": friday["probabilityOfPrecipitation"]["value"] if friday["probabilityOfPrecipitation"]["value"]  else 0 ,
        "humidity": friday["relativeHumidity"]["value"],
        "icon": friday["icon"].split("?")[0]+ "?size=large",
        "forecast":friday["detailedForecast"]
    }
    
    data["saturday"] = {
        "temp":saturday["temperature"],
        "wind":saturday["windSpeed"]+" "+saturday["windDirection"],
        "precipitation": saturday["probabilityOfPrecipitation"]["value"] if saturday["probabilityOfPrecipitation"]["value"]  else 0 ,
        "humidity": saturday["relativeHumidity"]["value"],
        "icon": saturday["icon"].split("?")[0]+ "?size=large",
        "forecast":saturday["detailedForecast"]
    }

    data["sunday"] = {
        "temp":sunday["temperature"],
        "wind":sunday["windSpeed"]+" "+sunday["windDirection"],
        "precipitation": sunday["probabilityOfPrecipitation"]["value"] if sunday["probabilityOfPrecipitation"]["value"]  else 0 ,
        "humidity": sunday["relativeHumidity"]["value"],
        "icon": sunday["icon"].split("?")[0]+ "?size=large",
        "forecast":sunday["detailedForecast"]
    }



    return render(req,'wwapp/weekend.html', context={'data':data})