import sqllite3
conn = sqlite3.connect('homework.db')
my_cur = conn.cursor()
my_cur.execute("""CREATE TABLE IF NOT EXISTS
            orders(orderid INT PRIMARY KEY,date TEXT, userid TEXT, total TEXT);""")
conn.commit()
my_cur.execute("""INSERT INTO users(userid, fname, lname, gender)
VALUES('00001', 'Alex', 'Smith', 'male');""")
conn.commit()
my_cur.execute("""SELECT * FROM  users;""")
a=my_cur.execute("""SELECT * FROM  users;""")
print(a)

