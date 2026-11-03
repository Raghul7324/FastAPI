
import pandas as pd


#students marks in different subjects
def add_student():
    students = {}
    while True:
        name = input("Enter student name (or 'quit' to exit): ")
        if name.lower() == 'quit':
            break
        marks = int(input("Enter marks: "))
        students[name]= {"Mark": marks}

    return students
        

def get_grade(marks):
    try:
        if marks < 0 or marks > 100:
            raise ValueError("Marks should be between 0 and 100.")
    except Exception as e:
        print(f"Error: {e}")
        return None
    if marks >= 90 and marks <= 100:
        return "A"
    elif marks >= 80 and marks < 90:
        return "B"
    elif marks >= 70 and marks < 80:
        return "C"
    elif marks >= 60 and marks < 70 :
        return "D"
    else:
        return "E"

# Output should have table with name, mark and grade for each student in each subject.
# show class average, the highest and lowest marks
# Offer a menu loop (add, show, quit) and never crash on bad input.


def show_students(students):
    rows=[]

    for name, info in students.items():
        mark = info["Mark"]
        rows.append({"Name": name, "Mark": mark, "Grade": get_grade(mark)})

    return rows

students = add_student()
df = pd.DataFrame(show_students(students))
print(df)