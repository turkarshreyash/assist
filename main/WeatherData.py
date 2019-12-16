import requests, json 
from django.contrib.gis.geoip2 import GeoIP2

g = GeoIP2()
api_key = "9d8ee2cbc7f94d51d3c7b65651ac3b72"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

def getLocation(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR') 
    location = dict()
    try:
        location["country"] = g.country(ip)["country_name"]
        location["country_code"] = g.country(ip)["country_code"].lower()
    except:
        location["country"] = None
        location["country_code"] = None
    try:
        location["city"] = g.city(ip)["city"]
    except:
        location["city"] = None
    return location

def weather(location):
    weather = None
    if location["city"] == None:
        return weather
    complete_url = base_url + "appid=" + api_key + "&q=" + location["city"] 
    response = requests.get(complete_url) 
    x = response.json() 
    weather = dict()
    if x["cod"] != "404": 
        weather = dict()
        y = x["main"] 
        weather["temp"] = y["temp"] 
        weather["pressure"] = y["pressure"] 
        weather["humidity"] = y["humidity"]
        weather["weather"]= x["weather"] 
        weather["description"] = x["weather"][0]["description"] 
        return weather
    return weather
