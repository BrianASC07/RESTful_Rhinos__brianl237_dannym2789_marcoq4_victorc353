import urllib.request
from urllib.request import Request
from urllib.request import urlopen
import json
import datetime
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import datetime

def getName(stockSymbol): #called in createtables
    url = f"https://financialmodelingprep.com/api/v3/profile/{stockSymbol}?apikey="
    FMP = open("../keys/key_FMP.txt", "r");
    api_key = FMP.read();
    try:
       with urllib.request.urlopen(url + api_key) as response:
          if response.getcode() == 200:
              html = response.read()
              str = html.decode('utf-8')
              data = json.loads(str)
              returner = []
              for i in data:
                  returner.append(i['companyName'])
              return returner
          else:
              print(f'Failed to retrieve data {response.status_code}')
    except Exception as e:
       return "Failed"
def getHistoricalStockData(stockSymbol): #maybe expand to diff time frames in future?
    current_time = datetime.datetime.now()
    url = f"https://financialmodelingprep.com/api/v3/historical-chart/1day/{stockSymbol}?from={current_time.year - 1}-{current_time.month}-{current_time.day}&to={current_time.year}-{current_time.month}-{current_time.day}&apikey="
    FMP = open("../keys/key_FMP.txt", "r");
    api_key = FMP.read();
    try:
       with urllib.request.urlopen(url + api_key) as response:
          if response.getcode() == 200:
              html = response.read()
              str = html.decode('utf-8')
              data = json.loads(str)
              returner = []
              for i in data:
                  returner.append([i['date'], i['open'], i['close']])
              return returner
          else:
              print(f'Failed to retrieve data {response.status_code}')
    except Exception as e:
       return "Failed"
def getNasdaqList(): #api does not allow s&p 500 list, so will add dow jones and nasdaq lists do not call tho!!!
   url = f"https://financialmodelingprep.com/api/v3/nasdaq_constituent?apikey="
   FMP = open("../keys/key_FMP.txt", "r");
   api_key = FMP.read();
   try:
       with urllib.request.urlopen(url + api_key) as response:
          if response.getcode() == 200:
              html = response.read()
              str = html.decode('utf-8')
              data = json.loads(str)
              returner = {"a", "b"}
              returner.remove("a")
              returner.remove("b")
              for i in data:
                  returner.add(i['name'])
              return returner
          else:
              print(f'Failed to retrieve data {response.status_code}')
   except Exception as e:
       return "Failed"
def getDowJonesList(): #api does not allow s&p 500 list, so will add dow jones and nasdaq lists do not call tho!!!
   url = f"https://financialmodelingprep.com/api/v3/dowjones_constituent?apikey="
   FMP = open("../keys/key_FMP.txt", "r");
   api_key = FMP.read();
   try:
       with urllib.request.urlopen(url + api_key) as response:
          if response.getcode() == 200:
              html = response.read()
              str = html.decode('utf-8')
              data = json.loads(str)
              returner = {"a", "b"}
              returner.remove("a")
              returner.remove("b")
              for i in data:
                  returner.add(i['name'])
              return returner
          else:
              print(f'Failed to retrieve data {response.status_code}')
   except Exception as e:
       return "Failed"
def getCompanySymbolList(): #do not call
    return getNasdaqList().union(getDowJonesList()) #NOTICE that this returns a set, not a list
def getStockPlot(stockSymbol, route):
    data = getHistoricalStockData(stockSymbol)
    dates = []
    values = []
    for i in data:
        dates.append(datetime.datetime.strptime(i[0][:-9], '%Y-%m-%d'))
        values.append(i[1])
    plt.plot(dates, values, 'g')
    plt.xticks(rotation=70)
    plt.subplots_adjust(bottom=0.15)
    plt.savefig('static/img.png')
    plt.clf()
#print(getPlot("AAPL"))
#print(getNasdaqList())
#print(getDowJonesList())
#print(getCompanySymbolList())
