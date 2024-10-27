class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1
        print(f"Student's Name: {self.name}")

    @classmethod
    def display_count(cls):
        print(f"Number of Student Names Displayed: {cls.count}")

student1 = Student("harivarshan")
student2 = Student("ks")
student3 = Student("vickram")

Student.display_count()
