import os
import urllib.request
import json


def getInfo(location):
        with urllib.request.urlopen("http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid=" + api_key) as response:
            if response.get(code)==200:
                coords = json.loads(response.read()) #reads the page's source code and converts to python dictionary in the same line
                #print(data)
                latURL = coords[0]["lat"]
                lonURL = coords[0]["lon"]
            else:
                print("Response code not 200 for Geocoding API")
                return "Geocoding API unavailable"
    #except:
        #print("URL request failure")
        #return render_template('OWM_error_page.html', errorMessage = "Geocoding API unavailable")
    #print(f"https://api.openweathermap.org/data/2.5/weather?lat={latURL}&lon={lonURL}&appid=" + api_key)
    #try:
        with urllib.request.urlopen(f"https://api.openweathermap.org/data/2.5/weather?lat={latURL}&lon={lonURL}&appid=" + api_key) as response:
            if response.get(code)==200:
                data = json.loads(response.read()) #reads the page's source code and converts to python dictionary in the same line
                return "whatever this is supposed to return"
                #return render_template('OWM_test.html', lat=coords[0]["lat"], lon=coords[0]["lon"], country=coords[0]["country"], state = coords[0]["state"], temp = data["main"]["temp"], main = data["weather"][0]["main"], description = data["weather"][0]["description"])
            #print(data)
            #print(coords["lat"])
            #print(coords[0])
            else:
                print("Response code not 200 for OWM API")
                return "Open Weather Map API unavailable"
