# Kyle Lee, Jessica Yu, Vedant Kothari, Will Nzeuton
# Team datTopherPack
# SoftDev
# p01
# 2024-12-07


import urllib.request
from urllib.request import Request
from urllib.request import urlopen
import json
import os




#Just use keys list to access api_key
#We can try to handle the responses with other functions, these just get the response
def FMP():
   url = f"https://financialmodelingprep.com/api/v3/search?query=AA&apikey="
   FMP = open("../keys/key_FMP.txt", "r");
   api_key = FMP.read();
   url = url + api_key
   try:
       a = urllib.request.urlopen(url)
       if a.getcode() == 200:
           return "Success"
       else:
           print(f'Failed to retrieve data {response.status_code}')
   except requests.exceptions.RequestException as e:
       return "Failed"

print(FMP())
