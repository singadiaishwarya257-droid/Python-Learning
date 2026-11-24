
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * self.radius * self.radius
        print("Area of Circle:", area)


radius = float(input("Enter the radius: "))

c = Circle(radius)
c.calculate_area()
