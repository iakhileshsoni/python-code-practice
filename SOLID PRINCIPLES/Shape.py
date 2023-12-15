from abc import ABC, abstractmethod
import math

# Single Responsibility Principle (SRP)
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Open/Closed Principle (OCP)
class AreaCalculator:
    def calculate_area(self, shape):
        return shape.area()

# Liskov Substitution Principle (LSP)
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Interface Segregation Principle (ISP)
class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class ShapeDrawer(Drawable):
    def __init__(self, shape):
        self.shape = shape

    def draw(self):
        return f"Drawing {self.shape.__class__.__name__} with details: {self.shape}"

# Dependency Inversion Principle (DIP)
class AreaCalculator:
    def calculate_area(self, shape):
        return shape.calculate_area()

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# Example usage
if __name__ == "__main__":
    rectangle = Rectangle(width=5, height=10)
    circle = Circle(radius=7)

    area_calculator = AreaCalculator()
    rectangle_drawer = ShapeDrawer(rectangle)
    circle_drawer = ShapeDrawer(circle)

    # Calculate and print areas
    print(f"Rectangle Area: {area_calculator.calculate_area(rectangle)}")
    print(f"Circle Area: {area_calculator.calculate_area(circle)}")

    # Draw shapes
    print(rectangle_drawer.draw())
    print(circle_drawer.draw())






from abc import ABC, abstractmethod
import math

# Single Responsibility Principle (SRP)
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

# Open/Closed Principle (OCP)
class AreaAndDrawingCalculator:
    def calculate_area(self, shape):
        return shape.area()

    def draw_shape(self, shape):
        return f"Drawing {shape.__class__.__name__} with details: {shape}"

# Liskov Substitution Principle (LSP)
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def draw(self):
        return f"Drawing Rectangle with width {self.width} and height {self.height}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def draw(self):
        return f"Drawing Circle with radius {self.radius}"

# Example usage
if __name__ == "__main__":
    rectangle = Rectangle(width=5, height=10)
    circle = Circle(radius=7)

    calculator = AreaAndDrawingCalculator()

    # Calculate and print areas
    print(f"Rectangle Area: {calculator.calculate_area(rectangle)}")
    print(f"Circle Area: {calculator.calculate_area(circle)}")

    # Draw shapes
    print(calculator.draw_shape(rectangle))
    print(calculator.draw_shape(circle))
