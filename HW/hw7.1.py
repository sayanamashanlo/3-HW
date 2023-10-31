import sqlite3

with sqlite3.connect('student3.db') as conn:
    cursor = conn.cursor()


    cursor.execute('''CREATE TABLE IF NOT EXISTS students
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       hobby TEXT,
                       first_name TEXT,
                       last_name TEXT,
                       birth_year INTEGER,
                       points INTEGER)''')

    students_data = [
        ('Reading', 'John', 'Doe', 1998, 15),
        ('Gaming', 'Alice', 'Johnson', 1999, 8),
        ('Traveling', 'Bob', 'Smithson', 2000, 12),
        ('Sports', 'Eva', 'Brown', 1997, 6),
        ('Drawing', 'Michael', 'White', 1998, 18),
        ('Music', 'Sophia', 'Taylor', 2001, 14),
        ('Coding', 'Oliver', 'Davis', 1999, 20),
        ('Cooking', 'Emma', 'Miller', 1996, 10),
        ('Dancing', 'Liam', 'Hall', 2002, 5),
        ('Photography', 'Ava', 'Clarkson', 1997, 13)
    ]

    cursor.executemany('INSERT INTO students (hobby, first_name, last_name, birth_year, points) VALUES (?, ?, ?, ?, ?)', students_data)
    cursor.execute('SELECT * FROM students WHERE LENGTH(last_name) > 10')
    long_last_name_students = cursor.fetchall()
    cursor.execute('UPDATE students SET first_name = "genius" WHERE points > 10')
    cursor.execute('SELECT * FROM students WHERE first_name = "genius"')
    genius_students = cursor.fetchall()
    cursor.execute('DELETE FROM students WHERE id % 2 = 0')

conn.commit()
conn.close()

print("Студенты с фамилией более 10 символов:")
print(long_last_name_students)
print("\nGenius студенты:")
print(genius_students)
