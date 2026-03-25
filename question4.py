class Student:
    def __init__(self, name, matter_1, matter_2, matter_3):
        self.name = name
        self.matter_1 = matter_1
        self.matter_2 = matter_2
        self.matter_3 = matter_3


class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def rank_matter_2(self):
        ranked_students = sorted(self.students, key=lambda student: student.matter_2, reverse=True)

        for student in ranked_students:
            print(f"{student.name} : {student.matter_2}")

    def rank_matter_3(self):
        ranked_students = sorted(self.students, key=lambda student: student.matter_3, reverse=True)

        for student in ranked_students:
            print(f"{student.name} : {student.matter_3}")


school_class = SchoolClass()
school_class.add_student(Student('J', 10, 12, 13))
school_class.add_student(Student('A', 8, 2, 17))
school_class.add_student(Student('V', 9, 14, 14))

print("Classement matière 2 :")
school_class.rank_matter_2()

print("Classement matière 3 :")
school_class.rank_matter_3()
