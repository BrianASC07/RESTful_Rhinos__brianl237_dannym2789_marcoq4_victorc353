from flask import Flask, render_template
import os
import urllib.request
import json

app = Flask(__name__)    #create Flask object
app.secret_key = os.urandom(32)
file = open("../keys/key_Calendarific.txt", "r")

api_key = file.read().strip()
curr_year = "2024"
curr_month = "12"
country = "us"
state = "ny"

#weird security thing in calendarific only authorizes requests from a browser for some reason i think??? workaround below
url=f"https://calendarific.com/api/v2/holidays?&api_key={api_key}&country={country}&year={curr_year}&location={country}-{state}&curr_month={curr_month}"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} #from https://stackoverflow.com/questions/65389552/python-requests-not-working-for-a-website-api-but-works-in-browser-chrome
requesturl = urllib.request.Request(url=url, headers=headers) # from https://www.zenrows.com/blog/urllib-headers#add-headers

@app.route("/")
def main():
    try:
        with urllib.request.urlopen(requesturl) as response:
            if data.get("meta").get("code") == 200: #checks if the api response code is 200 (everything works)
                data = json.loads(response.read()) #reads the page's source code and converts to python dictionary in the same line
                list = []
                for holiday in data.get("response").get("holidays"):
                    list.append(holiday.get("name"))
                return render_template('Calendarific_test.html', list=list)
            else: #fallback for if the response code isn't 200
                return render_template('Calendarific_test.html', list="Sorry, the API is currently unavailable")

    except: # catches all other errors
        print("CALENDARIFIC API UNAVAILABLE")
        return render_template('Calendarific_test.html', list="Sorry, the API is currently unavailable")

if __name__ == "__main__": 
    app.debug = True
    app.run()
