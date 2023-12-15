# Method Overloading
class Calculator:
    def add(self, a, b=0):
        return a + b

calc = Calculator()
print(calc.add(5))
print(calc.add(2, 3))



class Calculator:
    def add(self, *args):
        result = 0
        for num in args:
            result += num
        return result

calc = Calculator()
print(calc.add(5))
print(calc.add(2, 3, 4))


class Calculator:
    def add(self, a, b):
        return a + b

    def add_three(self, a, b, c):
        return self.add(a, self.add(b, c))

calc = Calculator()
result1 = calc.add(2, 3)
result2 = calc.add_three(2, 3, 4)








# Operator Overloading

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}j"

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

# Create complex numbers
c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(3, 4)

result = c1 + c2    # Overloaded addition
print(result)  # Output: 4 + 6j

# Overloaded equality
print(c1 == c2)  # Output: False
# Overloaded string representation
print(str(c1))  # Output: 1 + 2j




class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return iter(self.data)

my_data = MyIterable([1, 2, 3])
for item in my_data:
    print(item)



class JSONSerializable:
    def to_json(self):
        """Convert the object to a JSON representation."""
        raise NotImplementedError("Subclasses must implement to_json method.")

class Person(JSONSerializable):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_json(self):
        return {"name": self.name, "age": self.age}


MyClass = type("MyClass", (), {"x": 1, "y": 2})

obj = MyClass()
print(obj.x)  # Output: 1
print(obj.y)  # Output: 2



def create_class(class_name, base_class):
    class NewClass(base_class):
        def __init__(self, value):
            self.value = value
    NewClass.__name__ = class_name
    return NewClass

DynamicClass = create_class("DynamicClass", object)
obj = DynamicClass("Hello")
print(obj.value)  # Output: Hello




class Person:
    def __init__(self, name):
        self.name = name

person = Person("Alice")
setattr(person, "age", 30)

print("Person Name is : ", person.name)  # Output: Alice
print("Person Age is : ", person.age)   # Output: 30



class Dog:
    def __init__(self, name):
        self.name = name

dog = Dog("Rex")
dog.__dict__["breed"] = "Golden Retriever"
print(dog.name)  # Output: Rex
print(dog.breed) # Output: Golden Retriever


class MyClass:
    pass
obj = MyClass()
attribute_name = "dynamic_attribute"
setattr(obj, attribute_name, 42)

print(getattr(obj, attribute_name))  # Output: 42



