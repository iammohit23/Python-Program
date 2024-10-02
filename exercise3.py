# Write a python program to count number of students with A grade by using following operations using tuple:

# 1. Create a tuple of student

# 2. repeat operation using operators

# 3. create tuple using range function

# 4. get middle element of tuple using slicing method.

# 5. convert entire tuple into dictionary.

# 1. Create a tuple of students with their names and grades
students = (
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "A"),
    ("David", "C"),
    ("Eva", "A"),
    ("Frank", "B"),
    ("Grace", "A"),
    ("Hannah", "C"),
    ("Ian", "B"),
    ("Jack", "A")
)

# 2. Repeat operation using operators (e.g., repeating the tuple)
repeated_students = students * 2  # Repeat the tuple
print("Repeated Tuple of Students:")
print(repeated_students)

# 3. Create a tuple using range function (for example, student IDs)
student_ids = tuple(range(1, len(students) + 1))
print("\nTuple of Student IDs:")
print(student_ids)

# 4. Get the middle element of the tuple using slicing method
middle_index = len(students) // 2
middle_student = students[middle_index]
print("\nMiddle Student (using slicing):")
print(middle_student)

# 5. Convert entire tuple into dictionary
students_dict = {name: grade for name, grade in students}
print("\nConverted Tuple to Dictionary:")
print(students_dict)

# Count the number of students with 'A' grade
a_grade_count = sum(1 for _, grade in students if grade == 'A')
print("\nNumber of Students with 'A' Grade:", a_grade_count)
