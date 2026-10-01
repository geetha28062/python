def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "Fail"

name = input("Enter student name: ")
mark = int(input("Enter mark: "))

result = grade(mark)

print("Student:", name)
print("Mark:", mark)
print("Grade:", result)