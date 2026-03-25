def add_matter_4(cls):
    original_init = cls.__init__

    def new_init(self, name, matter_1, matter_2, matter_3, matter_4=0):
        original_init(self, name, matter_1, matter_2, matter_3)
        self.matter_4 = matter_4

    cls.__init__ = new_init
    return cls


@add_matter_4
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


school_class = SchoolClass()
school_class.add_student(Student('J', 10, 12, 13, 16))
school_class.add_student(Student('A', 8, 2, 17, 11))
school_class.add_student(Student('V', 9, 14, 14, 15))

for student in school_class.students:
    print(f"{student.name} : matière 4 = {student.matter_4}")
