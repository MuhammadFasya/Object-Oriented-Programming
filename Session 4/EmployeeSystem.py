class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.salary = 2500  # Base salary

    def calculate_salary(self):
        return self.salary  # Return base salary

    def show_details(self):
        print(f"{self.name} (ID: {self.id}) Salary: ${self.calculate_salary()}")

class Manager(Employee):
    def calculate_salary(self):
        return self.salary + (self.salary * 0.2)  # 20% bonus

class Engineer(Employee):
    def calculate_salary(self):
        return self.salary + (self.salary * 0.1)  # 10% performance bonus

class Intern(Employee):
    def __init__(self, name, id, stipend=1000):
        super().__init__(name, id)
        self.salary = stipend  # Fixed stipend for interns

employees = [
    Manager("Bob", "1"),
    Engineer("Jul", "2"),
    Intern("Alice", "3")
]

print("\nEmployee Salary Details:")
for emp in employees:
    emp.show_details()
