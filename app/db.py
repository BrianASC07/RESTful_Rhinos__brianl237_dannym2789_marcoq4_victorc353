import sqlite3, csv

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
    c.execute('CREATE TABLE IF NOT EXISTS newsContentPreferences (contentType TEXT UNIQUE NOT NULL)')


    db.commit()
    db.close()

createTables()


def createUser(username, password):
    db = sqlite3.connect("RESTables.db")
    c = db.cursor()
    query = "SELECT COUNT(1) FROM userData"
    c.execute(query)
    result = c.fetchone()
    row_count = result[0]
    try:
        c.execute('INSERT INTO userData VALUES (?, ?, ?, ?)', (row_count, username, password, ""))
        db.commit()
        db.close()
        return True
    except Exception as e:
        print(e)
        return False

def printData(table):
    db = sqlite3.connect("RESTables.db")
    c = db.cursor()
    c.execute(f"SELECT * FROM {table}")
    print(c.fetchall())
