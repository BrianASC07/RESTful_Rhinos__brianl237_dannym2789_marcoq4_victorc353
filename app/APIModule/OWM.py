import os
import urllib.request
import json

file = open("../keys/key_Open_Weather_Map.txt", "r")
api_key = file.read().strip()

def getTemp(location):
        if (location.find(' ') != -1):
            location = location[0: location.find(' ')] + '_' + location[locatio.find(' '):]
        with urllib.request.urlopen(f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=5&appid=" + api_key) as response:
            coords = json.loads(response.read()) #reads the page's source code and converts to python dictionary in the same line
            #print(data)
            latURL = coords[0]["lat"]
            lonURL = coords[0]["lon"]

        with urllib.request.urlopen(f"https://api.openweathermap.org/data/2.5/weather?lat={latURL}&lon={lonURL}&appid=" + api_key) as response:
            data = json.loads(response.read()) #reads the page's source code and converts to python dictionary in the same line
            return data["main"]["temp"]
            #print(data)
            #print(coords["lat"])
            #print(coords[0])

def getFeelsLike(location):
        if (location.find(' ') != -1):
            location = location[0: location.find(' ')] + '_' + location[locatio.find(' '):]
        with urllib.request.urlopen(f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=5&appid=" + api_key) as response:
            coords = json.loads(response.read()) #reads the page's source code and converts to python dictionary in the same line
            #print(data)
            latURL = coords[0]["lat"]
            lonURL = coords[0]["lon"]

        with urllib.request.urlopen(f"https://api.openweathermap.org/data/2.5/weather?lat={latURL}&lon={lonURL}&appid=" + api_key) as response:
            data = json.loads(response.read()) #reads the page's source code and converts to python dictionary in the same line
            return data["main"]["feels_like"]
            #print(data)
            #print(coords["lat"])
            #print(coords[0])

def getMain(location):
        if (location.find(' ') != -1):
            location = location[0: location.find(' ')] + '_' + location[locatio.find(' '):]
        with urllib.request.urlopen(f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=5&appid=" + api_key) as response:
            coords = json.loads(response.read()) #reads the page's source code and converts to python dictionary in the same line
            #print(data)
            latURL = coords[0]["lat"]
            lonURL = coords[0]["lon"]

        with urllib.request.urlopen(f"https://api.openweathermap.org/data/2.5/weather?lat={latURL}&lon={lonURL}&appid=" + api_key) as response:
            data = json.loads(response.read()) #reads the page's source code and converts to python dictionary in the same line
            return data["weather"]["main"]
            #print(data)
            #print(coords["lat"])
            #print(coords[0])

def getDescription(location):
        if (location.find(' ') != -1):
            location = location[0: location.find(' ')] + '_' + location[locatio.find(' '):]
        with urllib.request.urlopen(f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=5&appid=" + api_key) as response:
            coords = json.loads(response.read()) #reads the page's source code and converts to python dictionary in the same line
            #print(data)
            latURL = coords[0]["lat"]
            lonURL = coords[0]["lon"]

        with urllib.request.urlopen(f"https://api.openweathermap.org/data/2.5/weather?lat={latURL}&lon={lonURL}&appid=" + api_key) as response:
            data = json.loads(response.read()) #reads the page's source code and converts to python dictionary in the same line
            return data["weather"]["description"]
            #print(data)
            #print(coords["lat"])
            #print(coords[0])
