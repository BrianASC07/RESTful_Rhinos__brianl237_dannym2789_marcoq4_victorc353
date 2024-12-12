import sqlite3, csv, APIModule.FMP

# Create Tables
def createTables():
    db = sqlite3.connect("RESTables.db")#, check_same_thread = False)
    c = db.cursor()

    #User Info
    c.execute('''
            CREATE TABLE IF NOT EXISTS userData (
                userid INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                city TEXT)
        ''') #note that city can be an empty string

    #Stocks Info
    c.execute('''
            CREATE TABLE IF NOT EXISTS basicStockInfo (
                stockid INTEGER PRIMARY KEY,
                stockname TEXT NOT NULL,
                stocksymbol UNIQUE NOT NULL
            )
        ''')#each stock is a row


    #News Preferences Info
    sections = ["arts", "automobiles", "books", "business", "fashion", "food", "health", "home", "insider", "magazine", "movies", "nyregion",
        "obituaries", "opinion", "politics", "realestate", "science", "sports", "sundayreview", "technology", "theater", "travel", "upshot"
    "us", "world"]

    executable = "CREATE TABLE IF NOT EXISTS newsContentPreferences (userID INTEGER, "
    for i in sections:
        executable = executable + i + " INTEGER, " #0 if user doesnt care, 1 if user does (each user is a row)

    executable = executable[:-2] + ")"

    c.execute(executable)

    #Stock Preferences Info
    stocks = APIModule.FMP.getCompanySymbolList()

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

#def addPrefs(userID, city, ):


def printData(table):
    db = sqlite3.connect("RESTables.db")
    c = db.cursor()
    c.execute(f"SELECT * FROM {table}")
    print(c.fetchall())

createTables()
createUser("victor", "casado")
createUser("brian", "liu")
printData("userData")
printData("basicStockInfo")
printData("newsContentPreferences")
printData("stockPreferences")
