import os
import json
import urllib.request
from flask import Flask, render_template, url_for, session, request, redirect

from APIModule import OWM, Calendarific, FMP
import db

#KEY TESTING
keys_missing = False

FMP_key = ""
Open_Weather_Map_key = ""
NYT_key = ""
Calendarific_key = ""
try:
    FMP = open("../keys/key_FMP.txt", "r")
    FMP_key = FMP.read()
    print("\nFMP KEY LOADED")

    NYT = open("../keys/key_NYT.txt", "r")
    NYT_key = NYT.read()
    print("NYT KEY LOADED")

    Calendar = open("../keys/key_Calendarific.txt", "r")
    Calendarific_key = Calendar.read()
    print("CALENDARIFIC KEY LOADED")

    Open_Weather_Map = open("../keys/key_Open_Weather_Map.txt", "r")
    Open_Weather_Map_key = Open_Weather_Map.read()
    print("OPEN WEATHER MAP LOADED \n")
except:
    print("API KEY FILES MISSING\n")
    keys_missing = True

if(FMP_key == "" or Open_Weather_Map_key == "" or NYT_key == "" or Calendarific_key == ""):
    print("API KEYS MISSING:")
    print("FMP: " + FMP_key)
    print("OWM: " + Open_Weather_Map_key)
    print("NYT: " + NYT_key)
    print("CAL: " + Calendarific_key)
    keys_missing = True

#add check to make sure each key works

if os.path.exists("RESTables.db"):
  os.remove("RESTables.db")
  print("REMOVED DB FILE TO RECREATE IT FRESH \n")

db.createTables()


app = Flask(__name__)
app.secret_key = os.urandom(32)


##########################################
@app.route("/", methods=['GET', 'POST'])
def home():
    if(keys_missing):
        print("SOMETHING IS WRONG WITH KEYS!!!\n")
        return render_template("wrong.html")

    if request.method == 'POST':
        type = request.form.get("type")
        if (type == "loginbutton"):
            print("REDIRECTING TO LOGIN")
            return redirect(url_for('login'))
        elif (type == "signupbutton"):
            print("REDIRECTING TO SIGNUP")
            return redirect(url_for('signup'))
        elif (type == "logoutbutton"):
            print("LOGGING OUT... REDIRECTING TO HOME")
            session.pop('userID')
            return redirect(url_for('home'))
        elif (type == "profilebutton"):
            print("REDIRECTING TO PROFILE PAGE")
            return redirect(url_for('profile'))

    #IF LOGGED IN

    if 'userID' in session:
        print("ALREADY LOGGED IN... USERID: " + session.get('userID'))
        holidaylist = Calendarific.getInfo('us',db.getCityDict()[db.getUserCity()])
        print("LOADED HOLIDAYS")
        return render_template('home.html', loggedin=True, holidays=holidaylist)

    print("NOT LOGGED IN\n")
    return render_template('home.html', loggedin=False)
##########################################
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        type = request.form.get("type")
        #LOGIN BUTTON
        if (type == "loginenter"):
            username = request.form.get("user")
            password = request.form.get("password")
            if ((db.getUserID(username) is not None) and (db.isPasswordCorrect(username, password))):
                session['userID'] = db.getUserID(username)
                print("LOGIN CORRECT... REDIRECTING TO HOME")
                return redirect(url_for('home'))
            else:
                print("LOGIN INCORRECT... REDIRECTING BACK TO LOGIN")
                return render_template('login.html', error = "Username or password is not correct")
        #RETURN BACK HOME BUTTON
        if (type == "returnhome"):
            print("BACK TO HOME")
            return redirect(url_for('home'))

    #IF LOGGED IN
    if 'userID' in session:
        redirect(url_for('home'))

    print("ARRIVED AT LOGIN PAGE")
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
            username = request.form.get("user")
            password = request.form.get("password")
            session['userID'] = db.getUserID(username)
            db.createUser(username, password)
            print("SIGNED UP SUCCESSFULLY... GOING HOME")
            return redirect(url_for('home'))
        #RETURN BACK HOME BUTTON
        if (type == "returnhome"):
            print("BACK TO HOME")
            return redirect(url_for('home'))

    print("ARRIVED AT SIGNUP PAGE")
    return render_template('signup.html')
##########################################
@app.route("/profile", methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        type = request.form.get("type")
        if (type == "prefsbutton"):
            print("GOING TO CHANGE PREFS")
            return redirect(url_for('prefs'))
        #RETURN BACK HOME BUTTON
        if (type == "returnhome"):
            print("GOING BACK HOME")
            return redirect(url_for('home'))
    print("ARRIVED AT PROFILE PAGE")
    return render_template('profile.html')
##########################################
@app.route("/preferences", methods=['GET', 'POST'])
def prefs():
    if request.method == 'POST':
        type = request.form.get("type")
        #RETURN BACK HOME BUTTON
        if (type == "returnhome"):
            print("GOING BACK HOME")
            return redirect(url_for('home'))
    "ARRIVED AT PREFERENCE CHANGE PAGE"
    return render_template('prefs.html')
##########################################
if __name__ == "__main__":
    app.debug = True
    app.run(use_reloader=False)
