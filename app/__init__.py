import os
import json
import urllib.request
from flask import Flask, render_template, url_for, session, request, redirect
from APIModule import OWM, FMP, Calendarific
#KEY TESTING
keys_missing = False
FMP_key = ""
Open_Weather_Map_key = ""
NYT_key = ""
Calendarific_key = ""
try:
    Financial = open("../keys/key_FMP.txt", "r")
    FMP_key = Financial.read()
    print("FMP KEY LOADED")

    New_York_Times = open("../keys/key_NYT.txt", "r")
    NYT_key = New_York_Times.read()
    print("NYT KEY LOADED")

    Calendar = open("../keys/key_Calendarific.txt", "r")
    Calendarific_key = Calendar.read()
    print("CALENDARIFIC KEY LOADED")

    Open_Weather_Map = open("../keys/key_Open_Weather_Map.txt", "r")
    Open_Weather_Map_key = Open_Weather_Map.read()
    print("OPEN WEATHER MAP LOADED \n")
except:
    print("API KEY FILES MISSING")
    keys_missing = True

if(FMP_key == "" or Open_Weather_Map_key == "" or NYT_key == "" or Calendarific_key == ""):
    print("API KEYS MISSING:")
    print("FMP: " + FMP_key)
    print("OWM: " + Open_Weather_Map_key)
    print("NYT: " + NYT_key)
    print("CAL: " + Calendarific_key)
    keys_missing = True

app = Flask(__name__)

app.secret_key = os.urandom(32)
##########################################
@app.route("/", methods=['GET', 'POST'])
def home():
    if(keys_missing): #do sm #update later for all the other APIs
        return render_template("wrong.html")
    if request.method == 'POST':
        type = request.form.get("type")
        if (type == "loginbutton"):
            return redirect(url_for('login'))
        elif (type == "signupbutton"):
            return redirect(url_for('signup'))
        elif (type == "logoutbutton"):
            session.pop('username')
            return redirect(url_for('home'))
        elif (type == "profilebutton"):
            return redirect(url_for('profile'))

    #IF LOGGED IN
    #These are templates of what we info needs to be displayed on the home page.
    today_holiday = f"Friday the 13th. OOOOOOOH SPOOOOOKY"
    holiday_info = "Friday the 13th falling on a December this year is kind of crazy."
    today_weather = "Cloudy"
    temp = "15"
    stock_name = "Doge Coin"
    stock_change = "+10000000%"
    news_title = "Breaking news # 1"
    news_description = "This is breaking news. The first."

    if 'username' in session:
        return render_template('home.html', loggedin=True, holiday_today = today_holiday, holiday_stuff = holiday_info, weather_main = today_weather, temp_info = temp, stock = stock_name, inc_dec = stock_change, title = news_title, description = news_description)
    return render_template('home.html', loggedin=False)
##########################################
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        type = request.form.get("type")
        #LOGIN BUTTON
        if (type == "loginenter"):
            #DB STUFF HERE
            if (True):
                session['username'] = ""
                return redirect(url_for('home'))
        #RETURN BACK HOME BUTTON
        if (type == "returnhome"):
            return redirect(url_for('home'))

    #IF LOGGED IN
    if 'username' in session:
        redirect(url_for('home'))
    return render_template('login.html')
##########################################
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    #IF LOGGED IN
    if 'username' in session:
        redirect(url_for('home'))
    if request.method == 'POST':
        type = request.form.get("type")
        #SIGN UP BUTTON
        if (type == "signupenter"):
            #DB STUFF HERE
            if (True):
                session['username'] = ""
                return redirect(url_for('home'))
        #RETURN BACK HOME BUTTON
        if (type == "returnhome"):
            return redirect(url_for('home'))
    return render_template('signup.html')
##########################################
@app.route("/profile", methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        type = request.form.get("type")
        if (type == "prefsbutton"):
            return redirect(url_for('prefs'))
        #RETURN BACK HOME BUTTON
        if (type == "returnhome"):
            return redirect(url_for('home'))
    return render_template('profile.html')
##########################################
@app.route("/preferences", methods=['GET', 'POST'])
def prefs():
    if request.method == 'POST':
        type = request.form.get("type")
        #RETURN BACK HOME BUTTON
        if (type == "returnhome"):
            return redirect(url_for('home'))
    return render_template('prefs.html')
##########################################
if __name__ == "__main__":
    app.debug = True
    app.run()
