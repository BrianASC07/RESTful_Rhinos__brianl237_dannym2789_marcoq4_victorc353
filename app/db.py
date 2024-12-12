import sqlite3, csv, APIModule.FMP

def getNewsSections():
    return ["arts", "automobiles", "books", "business", "fashion", "food", "health", "home", "insider", "magazine", "movies", "nyregion",
        "obituaries", "opinion", "politics", "realestate", "science", "sports", "sundayreview", "technology", "theater", "travel", "upshot"
    "us", "world"] #to minimize api calls
def getStockList():
    ['AEP', 'CCEP', 'CMCSA', 'SHW', 'CDW', 'INTU', 'ISRG', 'CPRT', 'AZN', 'ILMN', 'TTD', 'TXN', 'ROP', 'MSFT', 'MRVL', 'META', 'PANW', 'PCAR', 'GOOG', 'LULU', 'BKNG', 'CSCO', 'ASML', 'GOOGL', 'KLAC', 'TEAM', 'COST', 'CDNS', 'WBD', 'PEP', 'ADP', 'EA', 'DXCM', 'LIN', 'EXC', 'ZS', 'JNJ', 'TSLA', 'CHTR', 'HD', 'MDLZ', 'DASH', 'ODFL', 'REGN', 'AMGN', 'ANSS', 'AMZN', 'CTSH', 'MELI', 'NXPI', 'FAST', 'PG', 'CEG', 'CVX', 'NVDA', 'PDD', 'NKE', 'SNPS', 'CRM', 'AXP', 'TRV', 'MMM', 'NFLX', 'PYPL', 'VRTX', 'XEL', 'MRK', 'KDP', 'TTWO', 'DLTR', 'ABNB', 'DDOG', 'ORLY', 'BKR', 'ADI', 'FTNT', 'WDAY', 'CAT', 'KHC', 'QCOM', 'SBUX', 'BIIB', 'PAYX', 'TMUS', 'HON', 'V', 'GS', 'IBM', 'WBA', 'UNH', 'CSGP', 'MAR', 'GILD', 'ROST', 'MCD', 'MCHP', 'GEHC', 'KO', 'ADBE', 'AVGO', 'BA', 'FANG', 'DIS', 'CTAS', 'AMAT', 'AAPL', 'MDB', 'MU', 'ARM', 'CRWD', 'ON', 'MNST', 'VZ', 'ADSK', 'WMT', 'CSX', 'VRSK', 'AMD', 'INTC', 'MRNA', 'IDXX', 'JPM', 'GFS', 'LRCX'] #to minimize api calls
def createTables():
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

    executable = "CREATE TABLE IF NOT EXISTS stockPreferences (userID INTEGER, "
    for i in stocks:
        if(not (i == "ON")): #reserved sqlite word
            executable = executable + str(i) + " INTEGER, " #0 if user doesnt care, 1 if user does (each user is a row)

    executable = executable[:-2] + ")"

    c.execute(executable)

    db.commit()
    db.close()
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

    executable = f"INSERT INTO newsContentPreferences VALUES ({userID}, "
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
print(APIModule.FMP.getCompanySymbolList())

createTables()
createUser("victor", "casado")
createUser("brian", "liu")
addPrefs(0, "NYC", ["AAPL"], ["travel", "books"])
addPrefs(0, "NYC", ["AAPL"], ["health" ,"books"])

print()
printData("userData")
print()
printData("basicStockInfo")
print()
printData("newsContentPreferences")
print()
printData("stockPreferences")
