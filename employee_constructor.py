class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


# Creating an object
emp1 = Employee("Aishwarya", 101, 25000)

# Displaying employee details
emp1.display_details()
