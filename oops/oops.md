extends
<h1 style="color: red;">Object Oriented Programming in Python</h1>

<h3 style="color: blue;"> What is OOPs in Programming? </h3>

Object-oriented programming is a programming paradigm that provides a means of structuring programs so that 
<b> properties and behaviors </b> are bundled into individual objects 
<br>
For example, an object could represent a person with properties like a name, age, and address and behaviors such as 
walking, talking, breathing, and running.



<h3 style="color: blue;"> Features of OOPs </h3>

Code re-usability

allows developer to model real-world concepts and entities using classes and objects, 
encapsulates data, re-use code through inheritance, and write more flexible code through polymorphism


<h3 style="color: blue;"> What is Class and Object in Python? </h3>

<h3 style="color: green;"> Class </h3>
A class is a blueprint or prototype from which the objects are created. <br>
In other words a class is a collection of objects. <br>
It is a logical entity that contains some <b> attributes or properties & methods </b> . <br>
Properties are the data or state of an object, and methods are the actions or behaviors than an object can perform
<br><br>


<b> Sytnax: </b>

    class Employee:
        def __init__(self, name, age):
            self.name =  name
            self.age = age


<h3 style="color: red;"> Note </h3>
1. Classes are created by using keyword class <br>
2. Attributes are the variables that belong to a class <br>
3. Attributes are always public & can be accessed using a dot (.) operator. For ex. :

    emp = Employee("akhilesh", 32) <br>
    print(emp.name)



<h3 style="color: green;"> Object </h3>

An object is an instance of a class, or we can say it is an entity that has a state & behaviour associated with it 
which is used to access the properties of the class. <br>
When a class is defined, no memory is allocated but the moment we create an object then memory is allocated


<b style="color: green;"> Creating an Object </b>

    obj = Employee()

<b style="color: green;"> Object's property: </b>

Let's take an example of dog then it will have: 

Identity - name of dog <br>
State/Attribute - Breed, Color <br>
Behaviour - Bark, Sleep, Eat <br>



