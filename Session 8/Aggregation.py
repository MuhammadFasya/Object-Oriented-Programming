class Department:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

dept = Department("Management")
emp = Employee("Markus", dept)
print(emp.department.name)  # Output: IT
