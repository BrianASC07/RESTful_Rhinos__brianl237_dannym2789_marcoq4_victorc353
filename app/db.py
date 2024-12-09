import sqlite3, csv

# Create Tables
def createTables():
    db = sqlite3.connect("RESTables.db")#, check_same_thread = False)
    c = db.cursor()
    
    #User Info
    c.execute('''
            CREATE TABLE IF NOT EXISTS users {
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            }
        ''')
    
    #Stocks Info
    c.execute('''
            CREATE TABLE IF NOT EXISTS stocks {
                id INTEGER PRIMARY KEY,
            }
        ''') # will need to add all stocks later with API calls
    
    #Weather Regions Info
    c.execute('''
            CREATE TABLE IF NOT EXISTS weather {
                id INTEGER PRIMARY KEY,
            }
        ''') # will need to add all weather later with API calls
    
    #News Preferences Info
    c.execute('''
            CREATE TABLE IF NOT EXISTS news {
                id INTEGER PRIMARY KEY,
            }
        ''') # will need to add all news later with API calls
    
    #Holiday Regions Info
    c.execute('''
            CREATE TABLE IF NOT EXISTS holidays {
                id INTEGER PRIMARY KEY,
            }
        ''') # will need to add all holidays later with API calls
    

    
    