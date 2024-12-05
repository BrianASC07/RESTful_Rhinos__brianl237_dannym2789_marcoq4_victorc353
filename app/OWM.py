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
        '''html = response.read() #reads the page's source code
        print(html)
        data = json.loads(html) #converts the page's source code into a python dictionary'''
        coords = json.loads(response.read()) #reads the page's source code and converts to python dictionary in the same line
        #print(data)
    with urllib.request.urlopen(f"https://api.openweathermap.org/data/2.5/weather?{coords["lat"]}=&{coords["lon"]}=&appid=" + api_key) as response:
        '''html = response.read() #reads the page's source code
        print(html)
        data = json.loads(html) #converts the page's source code into a python dictionary'''
        data = json.loads(response.read()) #reads the page's source code and converts to python dictionary in the same line
        #print(data)
    return render_template('main.html', url=data["hdurl"], explanation=data["explanation"])

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
