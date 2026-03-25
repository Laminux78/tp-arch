class Student:
    def __init__(self, name, matter_1, matter_2, matter_3):
        self.name = name
        self.matter_1 = matter_1
        self.matter_2 = matter_2
        self.matter_3 = matter_3


class SchoolClass:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SchoolClass, cls).__new__(cls)
            cls._instance.students = []
        return cls._instance

    def add_student(self, student):
        self.students.append(student)


school_class_1 = SchoolClass()
school_class_2 = SchoolClass()

school_class_1.add_student(Student('J', 10, 12, 13))

print(school_class_1 is school_class_2)
print(len(school_class_2.students))
