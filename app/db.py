import sqlite3, csv, APIModule.FMP

def getNewsSections():
    return ["arts", "automobiles", "books", "business", "fashion", "food", "health", "home", "insider", "magazine", "movies", "nyregion",
        "obituaries", "opinion", "politics", "realestate", "science", "sports", "sundayreview", "technology", "theater", "travel", "upshot"
    "us", "world"] #to minimize api calls
def getStockList():
    return {
"American Electric Power Company, Inc.": "AEP",
"Coca-Cola Europacific Partners PLC": "CCEP",
"Comcast Corporation": "CMCSA",
"The Sherwin-Williams Company": "SHW",
"CDW Corporation": "CDW",
"Intuit Inc.": "INTU",
"Intuitive Surgical, Inc.": "ISRG",
"Copart, Inc.": "CPRT",
"AstraZeneca PLC": "AZN",
"Illumina, Inc.": "ILMN",
"The Trade Desk, Inc.": "TTD",
"Texas Instruments Incorporated": "TXN",
"Roper Technologies, Inc.": "ROP",
"Microsoft Corporation": "MSFT",
"Marvell Technology, Inc.": "MRVL",
"Meta Platforms, Inc.": "META",
"Palo Alto Networks, Inc.": "PANW",
"PACCAR Inc": "PCAR",
"Alphabet Inc.": "GOOG",
"Lululemon Athletica Inc.": "LULU",
"Booking Holdings Inc.": "BKNG",
"Cisco Systems, Inc.": "CSCO",
"ASML Holding N.V.": "ASML",
"Alphabet Inc.": "GOOGL",
"KLA Corporation": "KLAC",
"Atlassian Corporation": "TEAM",
"Costco Wholesale Corporation": "COST",
"Cadence Design Systems, Inc.": "CDNS",
"Warner Bros. Discovery, Inc.": "WBD",
"PepsiCo, Inc.": "PEP",
"Automatic Data Processing, Inc.": "ADP",
"Electronic Arts Inc.": "EA",
"DexCom, Inc.": "DXCM",
"Linde plc": "LIN",
"Exelon Corporation": "EXC",
"Zscaler, Inc.": "ZS",
"Johnson & Johnson": "JNJ",
"Tesla, Inc.": "TSLA",
"Charter Communications, Inc.": "CHTR",
"The Home Depot, Inc.": "HD",
"Mondelez International, Inc.": "MDLZ",
"DoorDash, Inc.": "DASH",
"Old Dominion Freight Line, Inc.": "ODFL",
"Regeneron Pharmaceuticals, Inc.": "REGN",
"Amgen Inc.": "AMGN",
"ANSYS, Inc.": "ANSS",
"Amazon.com, Inc.": "AMZN",
"Cognizant Technology Solutions Corporation": "CTSH",
"MercadoLibre, Inc.": "MELI",
"NXP Semiconductors N.V.": "NXPI",
"Fastenal Company": "FAST",
"The Procter & Gamble Company": "PG",
"Constellation Energy Corporation": "CEG",
"Chevron Corporation": "CVX",
"NVIDIA Corporation": "NVDA",
"PDD Holdings Inc.": "PDD",
"NIKE, Inc.": "NKE",
"Synopsys, Inc.": "SNPS",
"Salesforce, Inc.": "CRM",
"American Express Company": "AXP",
"The Travelers Companies, Inc.": "TRV",
"3M Company": "MMM",
"Netflix, Inc.": "NFLX",
"PayPal Holdings, Inc.": "PYPL",
"Vertex Pharmaceuticals Incorporated": "VRTX",
"Xcel Energy Inc.": "XEL",
"Merck & Co., Inc.": "MRK",
"Keurig Dr Pepper Inc.": "KDP",
"Take-Two Interactive Software, Inc.": "TTWO",
"Dollar Tree, Inc.": "DLTR",
"Airbnb, Inc.": "ABNB",
"Datadog, Inc.": "DDOG",
"Baker Hughes Company": "BKR",
"Analog Devices, Inc.": "ADI",
"Fortinet, Inc.": "FTNT",
"Workday, Inc.": "WDAY",
"Caterpillar Inc.": "CAT",
"The Kraft Heinz Company": "KHC",
"QUALCOMM Incorporated": "QCOM",
"Starbucks Corporation": "SBUX",
"Biogen Inc.": "BIIB",
"Paychex, Inc.": "PAYX",
"T-Mobile US, Inc.": "TMUS",
"Honeywell International Inc.": "HON",
"Visa Inc.": "V",
"The Goldman Sachs Group, Inc.": "GS",
"International Business Machines Corporation": "IBM",
"Walgreens Boots Alliance, Inc.": "WBA",
"UnitedHealth Group Incorporated": "UNH",
"CoStar Group, Inc.": "CSGP",
"Marriott International, Inc.": "MAR",
"Gilead Sciences, Inc.": "GILD",
"Ross Stores, Inc.": "ROST",
"McDonald's Corporation": "MCD",
"Microchip Technology Incorporated": "MCHP",
"GE HealthCare Technologies Inc.": "GEHC",
"The Coca-Cola Company": "KO",
"Adobe Inc.": "ADBE",
"Broadcom Inc.": "AVGO",
"The Boeing Company": "BA",
"Diamondback Energy, Inc.": "FANG",
"The Walt Disney Company": "DIS",
"Cintas Corporation": "CTAS",
"Applied Materials, Inc.": "AMAT",
"Apple Inc.": "AAPL",
"MongoDB, Inc.": "MDB",
"Micron Technology, Inc.": "MU",
"Arm Holdings plc American Depositary Shares": "ARM",
"CrowdStrike Holdings, Inc.": "CRWD",
"Monster Beverage Corporation": "MNST",
"Verizon Communications Inc.": "VZ",
"Autodesk, Inc.": "ADSK",
"Walmart Inc.": "WMT",
"CSX Corporation": "CSX",
"Verisk Analytics, Inc.": "VRSK",
"Advanced Micro Devices, Inc.": "AMD",
"Intel Corporation": "INTC",
"Moderna, Inc.": "MRNA",
"IDEXX Laboratories, Inc.": "IDXX",
"JPMorgan Chase & Co.": "JPM",
"GLOBALFOUNDRIES Inc.": "GFS",
"Lam Research Corporation": "LRCX",
}
def getCityDict(): #dict, key is city name, answer is state
    with open("APIModule/Cities.csv", "r") as citiesCSV:
        csvreader = csv.reader(citiesCSV)
        cities = {}
        for row in csvreader:
            cities[row[0]] = row[1]
        return cities
def createTables():
    print("CREATING TABLES... THIS TAKES A SECOND")
    db = sqlite3.connect("RESTables.db")
    c = db.cursor()

    #User Info
    c.execute('''
            CREATE TABLE IF NOT EXISTS userData (
                userID INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                city TEXT)
        ''') #note that city can be an empty string

    #Stocks Info
    c.execute('''
            CREATE TABLE IF NOT EXISTS basicStockInfo (
                stockname TEXT NOT NULL,
                stocksymbol UNIQUE NOT NULL
            )
        ''')#each stock is a row
    #News Preferences Info
    sections = getNewsSections()

    executable = "CREATE TABLE IF NOT EXISTS newsContentPreferences (userID INTEGER, "
    for i in sections:
        executable = executable + i + " INTEGER, " #0 if user doesnt care, 1 if user does (each user is a row)

    executable = executable[:-2] + ")"

    c.execute(executable)

    #Stock Preferences Info
    stocks = getStockList()

    for i in list(stocks.keys()):
        name = i
        symbol = stocks[f"{name}"]
        #print(str("\"" + name) + "\": \"" + symbol + "\",")
        c.execute(f"INSERT INTO basicStockInfo VALUES (?, ?)", (name, symbol))
    print("STOCKS POPULATED ")

    executable = "CREATE TABLE IF NOT EXISTS stockPreferences (userID INTEGER, "
    for i in stocks:
        executable = executable + stocks[f"{i}"] + " INTEGER, " #0 if user doesnt care, 1 if user does (each user is a row)
    executable = executable[:-2] + ")"

    c.execute(executable)

    db.commit()
    db.close()

    print("TABLES SUCCESSFULLY CREATED \n")
def createUser(username, password):
    db = sqlite3.connect("RESTables.db")
    c = db.cursor()

    query = "SELECT COUNT(1) FROM userData"
    c.execute(query)
    result = c.fetchone()
    userID = result[0] #row count

    query = "SELECT COUNT(*) FROM pragma_table_info('newsContentPreferences')"
    c.execute(query)
    result = c.fetchone()
    newsPref_column_count = result[0]

    query = "SELECT COUNT(*) FROM pragma_table_info('stockPreferences')"
    c.execute(query)
    result = c.fetchone()
    stockPref_column_count = result[0]

    try:
        c.execute('INSERT INTO userData VALUES (?, ?, ?, ?)', (userID, username, password, ""))

        executable = f"INSERT INTO newsContentPreferences VALUES ({userID}, "
        for i in range(newsPref_column_count - 1):
            executable = executable + "0, " #row of all zeros as no prefs have been put in yet

        executable = executable[:-2] + ")"
        c.execute(executable)

        executable = f"INSERT INTO stockPreferences VALUES ({userID}, "
        for i in range(stockPref_column_count - 1):
            executable = executable + "0, " #row of all zeros as no prefs have been put in yet

        executable = executable[:-2] + ")"
        c.execute(executable)

        db.commit()
        db.close()
        return True
    except Exception as e:
        print(e)
        return False
def addPrefs(userID, city, stockSymbols, newsSections): #stockSymbols, newsSections are lists of strings; if no city, pass "", if no stocks, sections, pass []
    db = sqlite3.connect("RESTables.db")
    c = db.cursor()
    query = f"UPDATE userData SET city = '{city}' WHERE userID = {userID}" #this is safe as city comes from a dropdown and not user text input
    c.execute(query)
    #print(query)


    query = "SELECT COUNT(*) FROM pragma_table_info('stockPreferences')"
    c.execute(query)
    result = c.fetchone()
    stockPref_column_count = result[0]

    c.execute(f"DELETE FROM stockPreferences WHERE userID = {userID}")

    executable = f"INSERT INTO stockPreferences VALUES ({userID}, "
    for i in range(stockPref_column_count - 1):
        executable = executable + "0, " #row of all zeros to reset prefs
    executable = executable[:-2] + ")"
    c.execute(executable)

    executable = "UPDATE stockPreferences SET "
    for i in stockSymbols:
        executable = executable + i + " = 1, "
    executable = executable[:-2] + f" WHERE userID = {userID}"
    #print(executable)
    c.execute(executable)


    query = "SELECT COUNT(*) FROM pragma_table_info('newsContentPreferences')"
    c.execute(query)
    result = c.fetchone()
    newsPref_column_count = result[0]

    c.execute(f"DELETE FROM newsContentPreferences WHERE userID = {userID}")

    executable = f"INSERT INTO neORLYwsContentPreferences VALUES ({userID}, "
    for i in range(newsPref_column_count - 1):
        executable = executable + "0, " #row of all zeros to reset prefs
    executable = executable[:-2] + ")"
    c.execute(executable)

    executable = "UPDATE newsContentPreferences SET "
    for i in newsSections:
        executable = executable + i + " = 1, "
    executable = executable[:-2] + f" WHERE userID = {userID}"
    #print(executable)
    c.execute(executable)

    db.commit()
    db.close()
def printData(tableName):
    db = sqlite3.connect("RESTables.db")
    c = db.cursor()
    c.execute(f"SELECT * FROM {tableName}")
    string = ""
    for column in c.description:
        string = string + column[0] + "  "
    print(string)
    for row in c:
        print(row)
def getUserCity(userID):
    db = sqlite3.connect("RESTables.db")
    c = db.cursor()
    c.execute(f"SELECT city FROM userData WHERE userID = {userID}")
    row = c.fetchone()
    db.close()
    return row[0]
def getUserStocks(userID):
    db = sqlite3.connect("RESTables.db")
    c = db.cursor()
    c.execute(f"SELECT * FROM stockPreferences WHERE userID = {userID}")
    row = c.fetchone() #1st element is uid
    stocks = getStockList()
    returner = []
    for i in range(len(stocks)):
        if(row[i+1] == 1):
            returner.append(stocks[i])
    db.close()
    return returner
def getUserNewsSections(userID):
    db = sqlite3.connect("RESTables.db")
    c = db.cursor()
    c.execute(f"SELECT * FROM newsContentPreferences WHERE userID = {userID}")
    row = c.fetchone() #1st element is uid
    sections = getNewsSections()
    returner = []
    for i in range(len(sections)):
        if(row[i+1] == 1):
            returner.append(sections[i])
    db.close()
    return returner
def isPasswordCorrect(username, password):
    db = sqlite3.connect("RESTables.db")
    c = db.cursor()
    c.execute(f"SELECT password FROM userData WHERE username = '{username}'")
    row = c.fetchone()
    db.close()
    return password == row[0]
def getUserID(username):
    db = sqlite3.connect("RESTables.db")
    c = db.cursor()
    c.execute(f"SELECT userID FROM userData WHERE username = '{username}'")
    row = c.fetchone()
    db.close()
    if row == None:
        return None
    return row[0]
def getUsername(userID):
    db = sqlite3.connect("RESTables.db")
    c = db.cursor()
    c.execute(f"SELECT username FROM userData WHERE userID = '{userID}'")
    row = c.fetchone()
    db.close()
    if row == None:
        return None
    return row[0]

createTables()
'''
createTables()
createUser("victor", "casado")
createUser("brian", "liu")
addPrefs(1, "NYC", ["AAPL"], ["travel", "books"])
addPrefs(1, "NYC", ["AAPL", "NVDA"], ["health" ,"books"])
print(getUserCity(1))
print(getUserStocks(1))
print(getUserNewsSections(1))
print(isPasswordCorrect("victor", "casado"))
print(isPasswordCorrect("brian", "casado"))
print(getUserID("brian"))
'''
