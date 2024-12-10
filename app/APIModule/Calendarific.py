import urllib.request
import json
import os

def getInfo(curr_year, curr_month, country, state):
    try:
        file = open("../keys/key_Calendarific.txt", "r")
        api_key = file.read().strip()

        url=f"https://calendarific.com/api/v2/holidays?&api_key={api_key}&country={country}&year={curr_year}&location={country}-{state}&curr_month={curr_month}"

            #weird security thing in calendarific only authorizes requests from a browser for some reason i think??? workaround below
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} #from https://stackoverflow.com/questions/65389552/python-requests-not-working-for-a-website-api-but-works-in-browser-chrome
        requesturl = urllib.request.Request(url=url, headers=headers) # from https://www.zenrows.com/blog/urllib-headers#add-headers

        with urllib.request.urlopen(requesturl) as response:
            data = json.loads(response.read()) #reads the page's source code and converts to python dictionary in the same line
            if data.get("meta").get("code") == 200: #checks if the api response code is 200 (everything works)
                list = []
                for holiday in data.get("response").get("holidays"):
                    list.append(holiday.get("name"))
                return list
            else: #fallback for if the response code isn't 200
                return "Sorry, the API is currently unavailable"
    except: # catches all other errors
        return "Sorry, an error occured"
