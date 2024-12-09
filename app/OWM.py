from flask import Flask, render_template
import os
import urllib.request
import json

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32)
file = open("../keys/key_Open_Weather_Map.txt", "r")
api_key = file.read().strip()

@app.route("/")
def main():
    with urllib.request.urlopen("http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid=" + api_key) as response:
        coords = json.loads(response.read()) #reads the page's source code and converts to python dictionary in the same line
        #print(data)
    latURL = coords[0]["lat"]
    lonURL = coords[0]["lon"]
    print(f"https://api.openweathermap.org/data/2.5/weather?lat={latURL}&lon={lonURL}&appid=" + api_key)
    with urllib.request.urlopen(f"https://api.openweathermap.org/data/2.5/weather?lat={latURL}&lon={lonURL}&appid=" + api_key) as response:
        data = json.loads(response.read()) #reads the page's source code and converts to python dictionary in the same line
        #print(data)
    #print(coords["lat"])
    #print(coords[0])
    return render_template('OWM_test.html', lat=coords[0]["lat"], lon=coords[0]["lon"], country=coords[0]["country"], state = coords[0]["state"], temp = data["main"]["temp"], main = data["weather"][0]["main"], description = data["weather"][0]["description"])

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
