students = [
    {"name": "John", "age": 20},
    {"name": "Alice", "age": 18},
    {"name": "Bob", "age": 22},
    {"name": "Jane", "age": 19}
]
sort_field = input("Enter sort field (name or age): ")
sorted_students = sorted(students, key=lambda x: x[sort_field])
for students in sorted_students:
    print(students['name'], students['age'])