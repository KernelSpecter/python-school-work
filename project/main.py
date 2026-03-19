import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin123",
    database="school"
)

cursor = conn.cursor()

print("Connected to the database successfully!")
print("1. Add student \n2. View students \n3. Update marks \n4. Delete student")
choice = int(input("Enter your choice: "))
if choice == 1:
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    cursor.execute("INSERT INTO students (name, marks) VALUES (%s, %s)", (name, marks))
    conn.commit()
    print("Student added successfully!")
elif choice == 2:
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    for student in students:
        print(student)
elif choice == 3:
    student_id = int(input("Enter student ID to update marks: "))
    new_marks = int(input("Enter new marks: "))
    cursor.execute("UPDATE students SET marks = %s WHERE id = %s", (new_marks, student_id))
    conn.commit()
    print("Marks updated successfully!")
elif choice == 4:
    student_id = int(input("Enter student ID to delete: "))
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    print("Student deleted successfully!")
else:
    print("Invalid choice!")
