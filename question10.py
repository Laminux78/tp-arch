from collections.abc import Iterator


def add_matter_4(cls):
    original_init = cls.__init__

    def new_init(self, name, matter_1, matter_2, matter_3, matter_4=0):
        original_init(self, name, matter_1, matter_2, matter_3)
        self.matter_4 = matter_4

    cls.__init__ = new_init
    return cls


class Matter4Iterator(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda student: student.matter_4, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student


def add_matter_4_iterator(cls):
    def iter_matter_4(self):
        return Matter4Iterator(self.students)

    cls.iter_matter_4 = iter_matter_4
    return cls


@add_matter_4
class Student:
    def __init__(self, name, matter_1, matter_2, matter_3):
        self.name = name
        self.matter_1 = matter_1
        self.matter_2 = matter_2
        self.matter_3 = matter_3


@add_matter_4_iterator
class SchoolClass:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)


school_class = SchoolClass()
school_class.add_student(Student('J', 10, 12, 13, 16))
school_class.add_student(Student('A', 8, 2, 17, 11))
school_class.add_student(Student('V', 9, 14, 14, 15))

for student in school_class.iter_matter_4():
    print(f"{student.name} : {student.matter_4}")
