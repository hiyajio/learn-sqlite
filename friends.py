import sqlite3
conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()
# execute some sql
# c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")

# insert_query = '''INSERT INTO friends
#                       VALUES ('Merriwether', 'Lewis', 7)'''
# c.execute(insert_query)

# data = ("Steve", "Irwin", 9)
# query = f"INSERT INTO friends VALUES (?, ?, ?)"

# people = [
#     ("Ronald", "McDonald", 5),
#     ("Burger", "King", 8),
#     ("Jolli", "Bee", 9),
#     ("Wen", "Dys", 6),
#     ("Pop", "Eyes", 7)
# ]

# c.executemany("INSERT INTO friends VALUES (?, ?, ?)", people)

# average = 0
# for person in people:
#     c.execute("INSERT INTO friends VALUES (?, ?, ?)", person)
#     print("INSERTING NOW!!")
#     average += person[2]
# print(average/len(people))

# c.execute(query, data)

# c.execute("SELECT * FROM friends WHERE first_name IS 'Burger'")
c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")

# for result in c:
#     print(result)

print(c.fetchall())
# print(c.fetchone())

# commit changes
conn.commit()

conn.close()