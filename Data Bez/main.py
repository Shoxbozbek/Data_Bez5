import sqlite3 as sql

connect = sql.connect('data.db')

cursor = connect.cursor()

cursor.execute( """
CREATE TABLE IF NOT EXISTS shop(
    name TEXT,
    last_name TEXT,
    age INTEGER


)


""")


cursor.execute("""
INSERT INTO shop VALUES
('car','motobike','bike')


""")

cursor.execute("SELECT *FROM shop")

natija = cursor.fetchall()
print()

cursor.execute( """
CREATE TABLE IF NOT EXISTS book(
    name TEXT,
    last_name TEXT,
    age INTEGER


)


""")


cursor.execute("""
INSERT INTO book VALUES
('otkan kunlar','ikki eshik orasi','mehrobdan chayon')


""")

cursor.execute("SELECT *FROM book")

natija1 = cursor.fetchall()
print()

cursor.execute( """
CREATE TABLE IF NOT EXISTS phone(
    name TEXT,
    last_name TEXT,
    age INTEGER


)


""")


cursor.execute("""
INSERT INTO phone VALUES
('samsung','redmi',52)


""")

cursor.execute("SELECT *FROM phone")

natija2 = cursor.fetchall()
print()


cursor.execute( """
CREATE TABLE IF NOT EXISTS fruit(
    name TEXT,
    last_name TEXT,
    age TEXT


)


""")


cursor.execute("""
INSERT INTO fruit VALUES
('olma','behi','nok')


""")

cursor.execute("SELECT *FROM fruit")

natija3 = cursor.fetchall()
print()




cursor.execute( """
CREATE TABLE IF NOT EXISTS school(
    name TEXT,
    last_name TEXT,
    age INTEGER


)


""")


cursor.execute("""
INSERT INTO school VALUES
('maktab','sinf','xona')


""")

cursor.execute("SELECT *FROM school")

natija4 = cursor.fetchall()
print()




wh = "ha"
while wh == "ha":
    sorov = input("Qidiruv: ").lower()
    if sorov == "shop":
        print(natija)
    if sorov == "book":
        print(natija1)
    if sorov == "phone":
        print(natija2)
    if sorov == "mevalar":
        print(natija3)
    if sorov == "school":
        print(natija4)
    else:
        wh = input("davom etishni hohlaysizmi: ")