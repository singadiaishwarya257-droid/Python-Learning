
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Student Course:", self.course)


# Creating an object
s1 = Student("Aishwarya", 21, "BCA")

# Calling the method
s1.display()
