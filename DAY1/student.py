name = input("Enter student's name: ")
student_class = input("Enter student's class: ")
section = input("Enter student's section: ")

marks = []
for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)
total_marks = sum(marks)
percentage = ((total_marks / 500) * 100  )


print(f"\nStudent Name: {name}")
print(f"Class: {student_class}")
print(f"Section: {section}")
print(f"Percentage: {percentage:.2f}%")
