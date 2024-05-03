import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
            self.diameter = 2 * radius
        elif diameter is not None:
            self.diameter = diameter
            self.radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be provided.")

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius: {self.radius}, diameter: {self.diameter}"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        else:
            raise TypeError("Unsupported operand type for +")

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        else:
            raise TypeError("Unsupported operand type for >")

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        else:
            raise TypeError("Unsupported operand type for ==")

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        else:
            raise TypeError("Unsupported operand type for <")

circles = [Circle(radius=3), Circle(radius=2), Circle(radius=5)]
sorted_circles = sorted(circles)
print(sorted_circles)
# Output: [Circle with radius: 2, diameter: 4, Circle with radius: 3, diameter: 6, Circle with radius: 5, diameter:]
