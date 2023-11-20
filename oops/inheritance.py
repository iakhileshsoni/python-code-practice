class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee():
    def profession(self):
        # print("My name is :  {}, and my age is : {}", format(self.name, self.age))
        # super().__init__()
        print("this is the Employee class material")


emp = Employee('Vijay', '23')
print(emp.name)
print(emp.age)