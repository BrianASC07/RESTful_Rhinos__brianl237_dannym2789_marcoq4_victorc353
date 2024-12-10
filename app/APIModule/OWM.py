import os
import urllib.request
import json


def getInfo(location):
    try:
        file = open("../keys/key_Open_Weather_Map.txt", "r")
        api_key = file.read().strip()
        with urllib.request.urlopen(f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=5&appid=" + api_key) as response:
            coords = json.loads(response.read()) #reads the page's source code and converts to python dictionary in the same line
            #print(data)
            latURL = coords[0]["lat"]
            lonURL = coords[0]["lon"]
        with urllib.request.urlopen(f"https://api.openweathermap.org/data/2.5/weather?{latURL}=&{lonURL}=&appid=" + api_key) as response:
            data = json.loads(response.read()) #reads the page's source code and converts to python dictionary in the same line
        return "idk what this is supposed to return"
    
    except: # catches all other errors
        return "Sorry, an error occured"
