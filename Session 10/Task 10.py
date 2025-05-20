class Student:
    school_name = "SMA Maju Jaya Abadi"

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    # Class Method
    @classmethod
    def get_school_name(cls):
        return f"School Name: {cls.school_name}"

    # Static Method
    @staticmethod
    def is_passing(grade):
        return grade >= 60

student1 = Student("Ujang", 85)
student2 = Student("Mamat", 55)

# class method
print(Student.get_school_name())

# static method
print(f"{student1.name} is passing? {Student.is_passing(student1.grade)}")
print(f"{student2.name} is passing? {Student.is_passing(student2.grade)}")
