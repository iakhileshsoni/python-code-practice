"""

Create a class called SavingsAccount that represents an actual savings account in a bank.
It has two properties: funds and rate_of_interest.
The class should also have a method called debit() that decreases the funds by the specified amount and
a method called credit() that adds to the existing balance.
Also, define a third method to transfer the interest amount to the savings account.

"""



# class SavingsAccount:
#     def __init__(self, funds, rate_of_interest):
#         self.funds = funds
#         self.rate_of_interest = rate_of_interest
#
#     def debit(self, funds):
#         self.funds -= funds
#         return self.funds
#
#     def credit(self, funds):
#         self.funds += funds
#         return self.funds
#
#     def TransferInterestAmount(self, rate_of_interest):
#         self.rate_of_interest *= 1 + rate_of_interest
#         return self.rate_of_interest
#
#
# obj = SavingsAccount(2000, 10)
# obj.debit()
# obj.credit()
# obj.TransferInterestAmount()




"""
Create a class called Product that has two properties: name and price. The class should also have a method called 
get_total_cost() that returns the total cost (1.5 times the price) of the product, including tax.

"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_total_cost(self):
        total_cost = int(self.price * 1.5)
        return total_cost

obj = Product("Mobile", 10000)
print("Total cost is : ", obj.get_total_cost())



"""
Define a class called ShoppingCart that has a list of products. The class should also have a method called add_product()
that adds a product to the shopping cart and a method called get_total_cost() that returns the total cost of all the 
products in the shopping cart.

"""

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_total_cost(self):
        total_cost = 0
        for product in self.products:
            total_cost += product.get_total_cost()
        return total_cost



"""
Create a class called Employee that has three properties: name, age, and salary. The class should also have a method 
called get_annual_salary() that returns the employee’s annual salary.

"""
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_annual_salary(self):
        return self.salary * 12



"""
Implement a class called Company that has a list of employees. The class should also have a method called 
get_total_salary() that returns the total salary of all the employees in the company
"""


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_total_salary(self):
        total_salary = 0
        for employee in self.employees:
            total_salary += employee.get_annual_salary()
        return total_salary






