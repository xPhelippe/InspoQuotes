import sqlite3
import requests
from datetime import date, timedelta


conn = sqlite3.Connection("test.db")
# print("connection made")

# # TODO add condition if file for db does not exist

# query = '''
#     create table if not exists Quotes
#     (id integer primary key autoincrement not null  ,
#     date            text not null,
#     quote           text not null,
#     author          text
#     );
#     '''

# conn.execute(query)
# print("table created")
    

# allInspoQuotes = requests.get("https://type.fit/api/quotes").json()

# c = 0
# for q in allInspoQuotes:
#     c = c + 1
#     if q['text'] == 'We can only learn to love by loving.':
#         break

# dayStart = date(year=2022,month=11,day=9) - timedelta(days=(c))

# print(dayStart)

# rows = []


# c = 0
# for q in allInspoQuotes:

#     query = "insert into Quotes (date, quote, author) Values (\"{}\", \"{}\", \"{}\");".format(
#         str(dayStart + timedelta(days=c)),
#         q['text'],
#         q['author']
#     )

#     print(query)

#     conn.execute(query)
#     c = c + 1

# conn.commit()

# print("Quotes added")

query = 'select * from Quotes'

res = conn.execute(query)

for row in res:
    print(row)

#     cur = {
#         "date": str(dayStart + timedelta(days=c)),
#         "quote": q['text'],
#         "author": q['author']
#     }

#     rows.append(cur)



# print(rows[10:20])

# conn.execute(
#     '''
#     Create Table Company
#     (id int primary key not null,
#     name            text not null,
#     age             int not null,
#     address         char(50),
#     salary          real);
#     '''
# )

# print("table made")

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (1, 'Paul', 32, 'California', 20000.00 )");

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

# conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
    
# conn.commit()

# print("records created successfully")

# query = "select * from Company"

# res = conn.execute(query)

# for row in res:
#     print(row)
