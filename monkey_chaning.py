'''
Monkey Chain -  It is a Dynamic replacement of attributes (variables, functions inside a class) at runtime
'''
class Test:
    def __init__(self, x):
        self.a = x
    def get_data(self):
        print("Code to fetch data from the DB")
    def f1(self):
        self.get_data()
    def f2(self):
        self.get_data()

t1 = Test(5)
# t1.f1()
# t1.f2()

def new_get_data(self):
    print("Some code to fetch data from test DB")

Test.get_data = new_get_data
print("After Monkey Patching")
t1.f1()
t1.f2()