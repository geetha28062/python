name = input("Enter student name: ")
mark = int(input("Enter mark: "))

print("Student:", name)

if mark >= 90:
    print("Grade: A")
elif mark >= 80:
    print("Grade: B")
elif mark >= 70:
    print("Grade: C")
elif mark >= 50:
    print("Grade: D")
else:
    print("Grade: Fail")