# Python program to find current 
# weather details of any city 
# using openweathermap api 

# import required modules 
import requests, json 

# Enter your API key here 
api_key = "9d8ee2cbc7f94d51d3c7b65651ac3b72"

# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def weather(city_name):
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    response = requests.get(complete_url) 
    x = response.json() 
    if x["cod"] != "404": 
        y = x["main"] 
        current_temperature = y["temp"] 
        current_pressure = y["pressure"] 
        current_humidiy = y["humidity"] 
        z = x["weather"] 
        weather_description = z[0]["description"] 
        return (current_temperature,current_pressure,current_humidiy,weather_description)
    return (None,None,None,None)
