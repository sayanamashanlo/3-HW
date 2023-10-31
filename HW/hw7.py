
import sqlite3

db = sqlite3.connect('student2.db')

cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students 
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  hobby TEXT, 
                  first_name TEXT, 
                  last_name TEXT, 
                  birth_year INTEGER, 
                  homework_score INTEGER)''')

cursor.execute('''INSERT INTO students VALUES
('Reading', 'John', 'Doe', 1995, 8),
('Gaming', 'Alice', 'Smithson', 1998, 12),
('Traveling', 'Bob', 'Johnson', 1993, 15),
('Cooking', 'Eva', 'Brown', 1996, 7),
('Programming', 'Mike', 'Williams', 1997, 11),
('Painting', 'Linda', 'Miller', 1994, 6),
('Music', 'David', 'Taylor', 1992, 14),
('Sports', 'Sarah', 'Anderson', 1999, 9),
('Dancing', 'Chris', 'Wilson', 1991, 13),
('Photography', 'Emma', 'Thompson', 2000, 10)
''')


cursor.execute('''SELECT * FROM students WHERE LENGTH(last_name) > 10''')
long_last_name_students = cursor.fetchall()
print("Students with last names longer than 10 characters:")
print(long_last_name_students)

cursor.execute('''UPDATE students SET first_name = "genius" WHERE homework_score > 10''')


cursor.execute('''SELECT * FROM student WHERE name ='genius' ''')

cursor.execute('''SELECT * FROM students WHERE first_name = "genius"''')
genius_students = cursor.fetchall()
print("Genius students:")
print(genius_students)

cursor.execute('''DELETE FROM students WHERE id % 2 = 0''')

db.commit()
db.close()


