import json
import urllib.request
import os
import csv

def getPopular(type, period):
    input = ""
    urlTemp = f"https://api.nytimes.com/svc/mostpopular/v2"
    apikey = open("../keys/key_NYT.txt", "r").read().strip()

    if len(apikey) < 1: # Checks for blank API key
        print("No NYT API Key!")
        return
    
    if (period not in [1, 7, 30]): #NYT API only allows for the most popular pages within the past 1, 7, or 30 days to be checked
        print ("Invalid peroid for NYT.py getPopular")
        return
    
    # Checks for one of three popularity types: most emailed, most shared and most viewed
    if (type == "emailed"):
        input = f"/emailed/{period}.json"
        urlTemp += input
    
    elif (type == "shared"):
        input = f"/shared/{period}.json"
        urlTemp += input
        
    elif (type == "viewed"):
        input = f"/viewed/{period}.json"
        urlTemp += input
    
    else:
        print ("Inavlid type argument for NYT.py getPopular")
        return
    
    urlTemp += f"?api-key={apikey}"

    try:
        with urllib.request.urlopen(urlTemp) as response:
            if (response.getcode() == 200):
                data = json.loads(response.read())
                output = {"Links": [], "Article_Names": []}
                for i in data["results"]:
                    output["Links"].append(i["url"])
                    output["Article_Names"].append(i["title"])
                return output
                #temp = ""
                #for i in range(len(output["Links"])):
                #    temp += f"({output["Links"][i]}, {output["Article_Names"][i]})" + "\n"
                #return temp
                
            else:
                err = response.status_code
                print(f'API Status Error for NYT.py getPopular: {err}')
    except:
        print("API Error for NYT.py getPopular")


def getSection(section):
    input = ""
    urlTemp = "https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=section_name"
    apikey = open("../keys/key_NYT.txt", "r").read().strip()

    if len(apikey) < 1: # Checks for blank API key
        print("No NYT API Key!")
        return
    
    sectionList = []
    
    # Reads CSV file containing all Sections tags
    with open('APIModule/Sections.csv', 'r') as file:
        read = csv.reader(file)
        for i in read:
            sectionList.append(i[0])
    
    #print(sectionList)
    # Checks if the section parameter is in the sSections csv file
    if (section not in sectionList):
        print("invalid section")
        return
    
    urlTemp += f'("{section}")&api-key={apikey}'.replace(" ", "%20")
    #print(urlTemp)
    
    #try:
    with urllib.request.urlopen(urlTemp) as response:
        if (response.getcode() == 200):
            data = json.loads(response.read())
            output = {"Title": [], "Details": [], "URL":[]}
            for i in data["response"]["docs"]:
                output["Details"].append(i["snippet"])
                output["URL"].append(i["web_url"])
                output["Title"].append(i["headline"]["main"])
            return output
            #temp = ""
            #for i in range(len(output["Title"])):
            #    temp += f"({output["Title"][i]}, {output["Details"][i]}, {output["URL"][i]})" + "\n"
            #return temp
        else:
            err = response.status_code
            print(f'API Status Error for NYT.py getSection: {err}')
    #except:
    #    print("API Error for NYT.py getSection")

def getNewsDesk(nDesk):
    input = ""
    urlTemp = "https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=news_desk:"
    apikey = open("../keys/key_NYT.txt", "r").read().strip()

    if len(apikey) < 1: # Checks for blank API key
        print("No NYT API Key!")
        return
    
    newsList = []
    
    # Reads CSV file containing all NewsDesk tags
    with open('NewsDesk.csv', 'r') as file:
        read = csv.reader(file)
        for i in read:
            newsList.append(i[0])
    
    # Checks if the section parameter is in the NewsDesk csv file
    if (nDesk not in newsList):
        print("invalid section")
        return
    
    urlTemp += f'("{nDesk}")&api-key={apikey}'
    
    try:
        with urllib.request.urlopen(urlTemp) as response:
            if (response.getcode() == 200):
                data = json.loads(response.read())
                output = {"Links": [], "Article_Names": []}
                for i in data["response"]["docs"]:
                    output["Links"].append(i["web_url"])
                    output["Article_Names"].append(i["headline"]["main"])
                return output
                #temp = ""
                #for i in range(len(output["Links"])):
                #    temp += f"({output["Links"][i]}, {output["Article_Names"][i]})" + "\n"
                #return temp
            else:
                err = response.status_code
                print(f'API Status Error for NYT.py getNewsDesk: {err}')
    except:
        print("API Error for NYT.py getNewsDesk")


#print(getPopular("emailed", 1))
#print(getSection("Autos"))
#print(getNewsDesk("Sports"))