def grade_analyzer(name, mark):
    print("Student:", name)
    print("Mark:", mark)

    if mark >= 90:
        grade = "A"
    elif mark >= 75:
        grade = "B"
    elif mark >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print("Grade:", grade)

name = input("Enter student name: ")
mark = int(input("Enter mark: "))

grade_analyzer(name, mark)