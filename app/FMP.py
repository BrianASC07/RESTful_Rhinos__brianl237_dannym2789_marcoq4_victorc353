import urllib.request
from urllib.request import Request
from urllib.request import urlopen
import json
import datetime
import os

def getHistoricalStockData(stockSymbol): #maybe expand to diff time frames in future?
    current_time = datetime.datetime.now()
    url = f"https://financialmodelingprep.com/api/v3/historical-chart/1day/AAPL?from={current_time.year - 1}-{current_time.month}-{current_time.day}&to={current_time.year}-{current_time.month}-{current_time.day}&apikey="
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

print(getHistoricalStockData('AAPL'))

def getNasdaqList(): #api does not allow s&p 500 list, so will add dow jones and nasdaq lists
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
                  returner.add(i['symbol'])
              return returner
          else:
              print(f'Failed to retrieve data {response.status_code}')
   except Exception as e:
       return "Failed"

def getDowJonesList(): #api does not allow s&p 500 list, so will add dow jones and nasdaq lists
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
                  returner.add(i['symbol'])
              return returner
          else:
              print(f'Failed to retrieve data {response.status_code}')
   except Exception as e:
       return "Failed"

def getCompanySymbolList():
    #only function that should be called be app
    return getNasdaqList().union(getDowJonesList()) #NOTICE that this returns a set, not a list

#print(getNasdaqList())
#print(getDowJonesList())
#print(getCompanySymbolList())
