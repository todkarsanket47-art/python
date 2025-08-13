students = []
grades = []

def add_student(name, grade):
    students.append(name)
    grades.append(grade)
    print(f"Added {name} with grade {grade}.")

def update_grade(name, new_grade):
    if name in students:
        index = students.index(name)
        grades[index] = new_grade
        print(f"Updated {name}'s grade to {new_grade}.")
    else:
        print(f"Student {name} not found.")

def remove_student(name):
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print(f"Removed student {name}.")
    else:
        print(f"Student {name} not found.")

def average_grade():
    if grades:
        avg = sum(grades) / len(grades)
        print(f"Average grade: {avg:.2f}")
    else:
        print("No grades available.")

def highest_lowest():
    if grades:
        high = max(grades)
        low = min(grades)
        print(f"Highest grade: {high}")
        print(f"Lowest grade: {low}")
    else:
        print("No grades available.")

add_student("Pranav", 85)
add_student("Prathamesh", 92)
add_student("Soham", 78)

update_grade("Prathamesh", 95)
remove_student("Soham")

average_grade()
highest_lowest()
