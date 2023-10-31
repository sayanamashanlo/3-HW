import sqlite3

def create_student_db():
    connection = sqlite3.connect('student.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      hobby TEXT,
                      first_name TEXT,
                      last_name TEXT,
                      birth_year INTEGER,
                      homework_score INTEGER
                      )''')


    students_data = [
        ('Reading', 'John', 'Doe', 1998, 15),
        ('Swimming', 'Alice', 'Smithson', 1999, 8),
        ('Painting', 'Bob', 'Johnson', 2000, 12),
        ('Gaming', 'Alice', 'Smithson', 1998, 12),
        ('Traveling', 'Bob', 'Johnson', 1993, 15),
        ('Cooking', 'Eva', 'Brown', 1996, 7),
        ('Programming', 'Mike', 'Williams', 1997, 11),
        ('Painting', 'Linda', 'Miller', 1994, 6),
        ('Music', 'David', 'Vladislavov', 1992, 14),
        ('Sports', 'Sarah', 'Anderson', 1999, 9),

    ]

    cursor.executemany(
        'INSERT INTO students (hobby, first_name, last_name, birth_year, homework_score) VALUES (?, ?, ?, ?, ?)',
        students_data)

    connection.commit()
    connection.close()
def get_students_with_long_last_names():
    connection = sqlite3.connect('student.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM students WHERE LENGTH(last_name) > 10')
    students = cursor.fetchall()

    connection.close()
    return students
def update_students_names():
    connection = sqlite3.connect('student.db')
    cursor = connection.cursor()

    cursor.execute('UPDATE students SET first_name = "Genius" WHERE homework_score > 10')
    connection.commit()

    connection.close()
def get_genius_students():
    connection = sqlite3.connect('student.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM students WHERE first_name = "Genius"')
    genius_students = cursor.fetchall()

    connection.close()
    return genius_students
def delete_students_with_even_ids():
    connection = sqlite3.connect('student.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM students WHERE id % 2 = 0')
    connection.commit()

    connection.close()

create_student_db()
long_last_name_students = get_students_with_long_last_names()
update_students_names()
genius_students = get_genius_students()
delete_students_with_even_ids()

print("Студенты с фамилией более 10 символов:")
print(long_last_name_students)

print("\nСтуденты с именем Genius:")
print(genius_students)
