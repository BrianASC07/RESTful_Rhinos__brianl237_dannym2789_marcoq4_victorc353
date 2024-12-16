import os
import json
import urllib.request
from flask import Flask, render_template, url_for, session, request, redirect
from APIModule import OWM, Calendarific, FMP, NYT
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
    #IF LOGGED IN
    if 'userID' in session:
        print("ALREADY LOGGED IN... USERID: " + str(session.get('userID')))
        #These are templates of what we info needs to be displayed on the home page.
        city_name = "Placeholder City" #If anyone knows how to call this, please change it
        state_name = "Placeholder State"
        today_weather = "Cloudy"
        temp = "15"

        stock_list = db.getUserStocks(session.get('userID'))
        stock_personal_dict = {}
        for i in stock_list:
            stock_personal_dict[db.getStockName(i)] = i

        news_list = {'From the screen': "Where's my crown that's my bling", 'To the ring': 'Always drama when I ring', 'To the pen': 'See I believe that if I see it in my heart', 'To the king': "Smash through the ceiling 'cus I'm reaching for the stars"}
        if(db.getUserCity(session.get('userID')) == ''):
            today_holiday = Calendarific.getHoliday("")
            holiday_info =  Calendarific.getHolidayInfo("")
        else:
            today_holiday = Calendarific.getHoliday(db.getCityDict()[db.getUserCity(session.get('userID'))])
            holiday_info =  Calendarific.getHoliday(db.getCityDict()[db.getUserCity(session.get('userID'))])
        if len(today_holiday) == 0:
            today_holiday = "There are no holidays today!"
        print("LOADED HOLIDAYS")
        print(stock_list)
        db.printData("stockPreferences")
        return render_template('home.html', loggedin=True, holiday_today = today_holiday, holiday_stuff=holiday_info, city = city_name, state = state_name, weather_main = today_weather, temp_info = temp, all_stocks = stock_personal_dict, all_news = news_list)

    print("NOT LOGGED IN\n")

    return render_template('home.html', loggedin=False)
##########################################
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("user")
        password = request.form.get("password")
        if ((db.getUserID(username) is not None) and (db.isPasswordCorrect(username, password))):
            session['userID'] = db.getUserID(username)
            print("LOGIN CORRECT... REDIRECTING TO HOME")
            return redirect(url_for('home'))
        else:
            print("LOGIN INCORRECT... REDIRECTING BACK TO LOGIN")
            return render_template('login.html', error = "Username or password is not correct")


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
        username = request.form.get("user")
        password = request.form.get("password")
        db.createUser(username, password)
        session['userID'] = db.getUserID(username)
        print("SIGNED UP SUCCESSFULLY... GOING HOME")
        return redirect(url_for('home'))


    print("ARRIVED AT SIGNUP PAGE")
    return render_template('signup.html')
##########################################
@app.route("/profile", methods=['GET', 'POST'])
def profile():
    city = ""
    stocks = []
    news = []
    if request.method == 'POST':
        id = session.get('userID')
        city = request.form.get('city_name')
        stockNames = request.form.getlist('stock_names')
        news = request.form.getlist('section_names')
        stockDict = db.getStockDict()
        for i in stockNames:
            stocks.append(stockDict[f"{i}"])
        print("ID: " + str(id))
        print("CITY: " + city)
        print("STOCKS: " + str(stocks))
        print("NEWS SECTIONS: " + str(news))
        db.addPrefs(id, city, stocks, news)
        print("ARRIVED AT PROFILE PAGE")
    user = db.getUsername(session.get('userID'))

    return render_template('profile.html', pref_city = city, pref_stocks = stocks, news_sections = news, username = user)
##########################################
@app.route("/preferences", methods=['GET', 'POST'])
def prefs():
    if request.method == 'POST':
        print("RECEIVING DATA")
    print("ARRIVED AT PREFERENCE CHANGE PAGE")
    stockList = list(db.getStockDict().keys())
    newsSectionList = db.getNewsSections()
    cityList = list(db.getCityDict().keys())
    user = db.getUsername(session.get('userID'))
    locationPrefs = db.getUserCity(session.get('userID'))
    newsSectionPrefs = db.getUserNewsSections(session.get('userID'))
    stockPrefs = db.getUserStocks(session.get('userID'))
    print("printing db")
    db.printData("userData")
    return render_template('prefs.html', cities = cityList, stocks = stockList, sections = newsSectionList, username = user, userlocation = locationPrefs, usernews = newsSectionPrefs, userstocks = stockPrefs)
##########################################
@app.route("/logout")
def logout():
    session.pop("userID")
    return redirect(url_for('home'))
##########################################
if __name__ == "__main__":
    app.debug = True
    app.run()#use_reloader=False, debug=False
