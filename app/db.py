import sqlite3, csv

# Create Tables
def createTables():
    db = sqlite3.connect("RESTables.db")#, check_same_thread = False)
    c = db.cursor()
    
    #User Info
    c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
    
    #Stocks Info
    c.execute('''
            CREATE TABLE IF NOT EXISTS stocks (
                id INTEGER PRIMARY KEY,
                stock1 INTEGER DEFAULT 0
            )
        ''')
    # will need to add all stocks later with API calls
    
    #Weather Regions Info
    c.execute('CREATE TABLE IF NOT EXISTS weather (id INTEGER PRIMARY KEY)')
    # will need to add all weather later with API calls
    
    #News Preferences Info
    c.execute('CREATE TABLE IF NOT EXISTS news (id INTEGER PRIMARY KEY)')
    # will need to add all news later with API calls
    
    #Holiday Regions Info
    c.execute('CREATE TABLE IF NOT EXISTS holidays (id INTEGER PRIMARY KEY)')
    # will need to add all holidays later with API calls
    
    db.commit()
    db.close()

createTables()

def setPref(table, item, value):
    db = sqlite3.connect("RESTables.db")#, check_same_thread = False)
    c = db.cursor()
    try:
        if (value == 0 or value == 1):
            c.execute('INSERT INTO (?) (?) VALUES (?)', (table, item, value))
        else:
            print("INVALID VALUE")
    except:
        print('INVALID TABLE OR ITEM FROM: ' + table + ' ' + item + ' call')

setPref("a","a", 1)