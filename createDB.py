import sqlite3
import requests
from datetime import date, timedelta

dbname="inspo.db"

def createQuotesTable():
    conn = sqlite3.Connection(dbname)
    print("db connection made")

    query = '''
    create table if not exists Quotes
    (id integer primary key autoincrement not null  ,
    date            text not null,
    quote           text not null,
    author          text
    );
    '''

    conn.execute(query)
    print("Quotes table created")

    allInspoQuotes = requests.get("https://type.fit/api/quotes").json()

    c = 0
    for q in allInspoQuotes:
        c = c + 1
        if q['text'] == 'We can only learn to love by loving.':
            break
    
    dayStart = date(year=2022,month=11,day=9) - timedelta(days=(c))
    
    c = 0
    for q in allInspoQuotes:

        query = "insert into Quotes (date, quote, author) Values (\"{}\", \"{}\", \"{}\");".format(
            str(dayStart + timedelta(days=c)),
            q['text'],
            q['author']
        )

        print(query)

        conn.execute(query)
        c = c + 1

    conn.commit()

    print("Quotes added to table")

    conn.close()
    print("Connection closed")


def createPhoneTable(initNums=[]):

    conn = sqlite3.Connection(dbname)
    print("db connection made")

    query = '''
    create table if not exists PhoneNumbers
    (id integer primary key autoincrement not null  ,
    phoneNumber            text not null,
    isStopped              integer not null
    );
    '''

    conn.execute(query)
    print("PhoneNumbers table created")

    for num in initNums:
        query = "insert into PhoneNumbers (phoneNumber,isStopped) values (\"{}\",0);".format(
            num,
        )

        conn.execute(query)

    conn.commit()

    print("Initial phone numbers added")

    conn.close()
    print("Connection closed")

