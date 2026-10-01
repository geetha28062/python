name = input("Enter student name: ")

m1 = int(input("Enter Tamil mark: "))
m2 = int(input("Enter English mark: "))
m3 = int(input("Enter Maths mark: "))

total = m1 + m2 + m3
average = total / 3

print("Name:", name)
print("Total:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")