class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average = sum(self.marks) / len(self.marks)

        return average > 50

student1 = Student("Mateusz", [60, 80, 90])
student2 = Student("Damian", [20, 40, 50])

print(f"Student {student1.name}: {student1.is_passed()}")
print(f"Student {student2.name}: {student2.is_passed()}")