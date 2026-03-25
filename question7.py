from collections.abc import Iterable, Iterator


class Student:
    def __init__(self, name, matter_1, matter_2, matter_3):
        self.name = name
        self.matter_1 = matter_1
        self.matter_2 = matter_2
        self.matter_3 = matter_3


class Matter1Iterator(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda student: student.matter_1, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student


class Matter2Iterator(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda student: student.matter_2, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student


class Matter3Iterator(Iterator):
    def __init__(self, students):
        self.students = sorted(students, key=lambda student: student.matter_3, reverse=True)
        self.index = 0

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        student = self.students[self.index]
        self.index += 1
        return student


class SchoolClass(Iterable):
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __iter__(self):
        return Matter1Iterator(self.students)

    def iter_matter_2(self):
        return Matter2Iterator(self.students)

    def iter_matter_3(self):
        return Matter3Iterator(self.students)


school_class = SchoolClass()
school_class.add_student(Student('J', 10, 12, 13))
school_class.add_student(Student('A', 8, 2, 17))
school_class.add_student(Student('V', 9, 14, 14))

print("Classement matière 1 :")
for student in school_class:
    print(f"{student.name} : {student.matter_1}")

print("Classement matière 2 :")
for student in school_class.iter_matter_2():
    print(f"{student.name} : {student.matter_2}")

print("Classement matière 3 :")
for student in school_class.iter_matter_3():
    print(f"{student.name} : {student.matter_3}")
