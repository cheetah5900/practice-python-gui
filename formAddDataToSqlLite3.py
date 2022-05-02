import sqlite3  # import sqllite

conn = sqlite3.connect('expense.sqlite3')  # create Database

c = conn.cursor()  # create operator for doing anything

'''
create table
'ID' => transaction_id TEXT,
'วัน-เวลา' => date_time TEXT,
'รายการ' => title TEXT,
'ค่าใช้จ่าย' => price REAL,
'จำนวน' => quantity INTEGER
'''
c.execute(""" CREATE TABLE IF NOT EXISTS expenselist(
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        transaction_id TEXT,
                        date_time TEXT,
                        title TEXT,
                        price REAL,
                        quantity INTEGER
                        )
                """)


def insertSqlData(transaction_id, date_time, title, price, quantity):  # insert data funciton
    ID = None  # id auto increasement doesn't need to add data
    with conn:  # open db without exit database
        c.execute("""INSERT INTO expenselist VALUES (?,?,?,?,?,?)""",
                  (ID, transaction_id, date_time, title, price, quantity))  # insert command
    conn.commit()
# insertSqlData(1234567, "เสาร์ 30-04-22", "Title นะครับ", 10, 69)


def showSqlData():  # function show data
    with conn:  # open db without exit database
        c.execute("""SELECT * FROM expenselist""")  # get all data
        result = c.fetchall()  # get value in c variable
    return result


def updateSqlData(transaction_id, title, price, quantity):  # update sql data
    with conn:  # open db without exit database
        c.execute("""UPDATE expenselist SET title=?, price=?, quantity=? WHERE transaction_id=?""", ([
                  title, price, quantity, transaction_id]))  # sql command to update database
    conn.commit()  # save
# updateSqlData('202204291641903757',5,5,5)


def deleteSqlData(transaction_id):
    with conn:
        c.execute("""DELETE FROM expenlist WHERE transaction_id=?""",
                  ([transaction_id]))
    c.commit()
