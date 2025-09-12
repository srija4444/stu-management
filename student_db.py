import sqlite3

# Connect to SQLite DB
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    StudentID INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    Age INTEGER,
    Grade TEXT,
    Email TEXT
)
''')
conn.commit()

def add_student(student):
    cursor.execute("INSERT INTO Students VALUES (?, ?, ?, ?, ?, ?)", student)
    conn.commit()

def view_students():
    cursor.execute("SELECT * FROM Students")
    return cursor.fetchall()

def update_student(student_id, field, new_value):
    cursor.execute(f"UPDATE Students SET {field} = ? WHERE StudentID = ?", (new_value, student_id))
    conn.commit()

def delete_student(student_id):
    cursor.execute("DELETE FROM Students WHERE StudentID = ?", (student_id,))
    conn.commit()

def close_db():
    conn.close()


def add_student(student):
    # Check if StudentID already exists in the database
    cursor.execute("SELECT * FROM Students WHERE StudentID = ?", (student[0],))
    if cursor.fetchone():
        print(" Student ID already exists!")
    else:
        # Proceed with the insert if the StudentID is unique
        cursor.execute("INSERT INTO Students (StudentID, FirstName, LastName, Age, Grade, Email) VALUES (?, ?, ?, ?, ?, ?)", student)
        conn.commit()
        print(" Student added!")

