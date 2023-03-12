import sqlite3


conn = sqlite3.connect('example.db')


conn.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)''')

conn.execute("INSERT INTO users (name, age) VALUES ('Аня', 25)")
conn.execute("INSERT INTO users (name, age) VALUES ('Олег', 30)")
conn.execute("INSERT INTO users (name, age) VALUES ('Оля', 40)")


conn.commit()
conn.close()


conn = sqlite3.connect('example.db')


cursor = conn.execute("Виберіть id, ім'я, вік від користувачів")
for row in cursor:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")


conn.close()
