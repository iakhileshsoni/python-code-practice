https://github.com/ishwar6
https://github.com/ishwar6/Django-Rest-Framework/blob/main

Python Design Patterns
https://github.com/topics/python-design-patterns

Python Request
https://github.com/psf/requests

Django
https://github.com/django/django

Real Python - Python Guide
https://github.com/realpython/python-guide/tree/master

Python Scipts
https://github.com/topics/python-scripts

Algorithms in Python
https://github.com/keon/algorithms
https://github.com/prakhar1989/Algorithms

Project based learning
https://github.com/practical-tutorials/project-based-learning

Python3
https://github.com/jerry-git/learn-python3

















Low-level design (LLD) is a component-level design process that follows a step-by-step refinement process. 
It is based on the high-level design (HLD) that describes the overall architecture and functionality of a system. 
LLD provides the internal logical design of the actual program code, such as the class diagrams, methods, relations, and 
specifications. It helps the programmer to directly code the program from the document, with minimal debugging and testing. 
LLD also ensures lower cost and easier maintenance of the software1

Some concepts involved in LLD are:

Object-oriented principles: The use of OOPS concepts such as inheritance, encapsulation, polymorphism, and abstraction to design the 
classes and objects that represent the entities and behaviors of the system2
Unified Modeling Language (UML) diagrams: The use of graphical notations such as use case diagrams, sequence diagrams, state diagrams, etc. 
to model the structure and behavior of the system and its components2
OOPS and SOLID principles: The use of best practices and design patterns to ensure that the code is readable, reusable, maintainable, 
and testable. Some of these principles are single responsibility, open-closed, Liskov substitution, interface segregation, and dependency 
inversion2




There are many concepts in programming, not just OOPs. OOPs stands for Object-Oriented Programming, which is a paradigm that uses objects and 
classes to model the real-world entities and behaviors. Some of the main concepts of OOPs are:

Class: A class is a blueprint or template that defines the common attributes and methods of a group of objects. For example, a class named Car 
can have attributes like color, model, speed, etc. and methods like start, stop, accelerate, etc1

Object: An object is an instance or a specific example of a class. It has its own state and behavior that may differ from other objects of the 
same class. For example, an object named myCar can be an instance of the class Car, with its own color, model, speed, etc. and can perform the 
methods defined in the class Car1

Inheritance: Inheritance is a mechanism that allows a class to acquire or inherit the properties and methods of another class. 
The class that inherits is called the subclass or child class, and the class that is inherited from is called the superclass or parent class. 
For example, a class named Truck can inherit from the class Car, and acquire its attributes and methods, as well as define its own specific 
attributes and methods1

Polymorphism: Polymorphism is the ability of an object to take different forms or behave differently depending on the context. 
It can be achieved by using method overloading or method overriding. Method overloading is when a class has multiple methods with the 
same name but different parameters. Method overriding is when a subclass redefines a method of its superclass with the same name and 
parameters. For example, a method named drive can be overloaded in the class Car with different parameters like speed, distance, direction, etc. 
and can be overridden in the subclass Truck with a different implementation1

Abstraction: Abstraction is the process of hiding the unnecessary or complex details and showing only the essential or relevant information. 
It helps to reduce complexity and increase efficiency. Abstraction can be achieved by using abstract classes or interfaces. An abstract 
class is a class that cannot be instantiated, but can have abstract methods that must be implemented by its subclasses. An interface is 
a collection of abstract methods that can be implemented by any class that implements the interface. For example, an abstract class named 
Vehicle can have an abstract method named drive, and an interface named Electric can have an abstract method named charge. 
A class named Tesla can inherit from the class Vehicle and implement the interface Electric, and provide the implementation for both the 
methods drive and charge1

Encapsulation: Encapsulation is the technique of wrapping or bundling the data and the methods that operate on the data together in a single 
unit, such as a class. It helps to protect the data from unauthorized access and modification, and to achieve data hiding and security. 

Encapsulation can be achieved by using access modifiers, such as public, private, protected, etc. that specify the visibility or 
accessibility of the data and the methods. For example, a class named BankAccount can have private data members like balance, accountNumber, 
etc. and public methods like deposit, withdraw, etc. that can access and manipulate the data members. The private data members can only be 
accessed by the methods of the same class, and not by any other class or object1

These are some of the basic concepts of OOPs, but there are more advanced concepts like association, aggregation, composition, coupling, 
cohesion, etc. that are also important to understand





OOPs is indeed one of the concepts used in LLD, but not the only one. There are other concepts that are also important to understand and 
apply in LLD, such as:

UML diagrams: UML stands for Unified Modeling Language, which is a standard way of visualizing the design of a system using different 
types of diagrams. UML diagrams can help to model the structure and behavior of the system and its components, such as classes, objects, 
relationships, interactions, states, etc. Some of the common UML diagrams used in LLD are:

Class diagram: A class diagram shows the classes and their attributes, methods, and associations. It can also show the inheritance, 
aggregation, composition, and dependency relationships between classes. A class diagram can help to define the data structures and 
operations of the system1

Sequence diagram: A sequence diagram shows the interactions between objects in a time-ordered sequence. It can also show the messages, 
lifelines, activation bars, and loops of the objects. A sequence diagram can help to illustrate the dynamic behavior and logic of the system1

State diagram: A state diagram shows the states and transitions of an object or a system. It can also show the events, actions, and guards 
that trigger the transitions. A state diagram can help to describe the stateful behavior and response of the system1

OOPS and SOLID principles: OOPS stands for Object-Oriented Programming System, which is a paradigm that uses objects and classes to model 
the real-world entities and behaviors. SOLID stands for Single responsibility, Open-closed, Liskov substitution, Interface segregation, 
and Dependency inversion, which are five design principles that help to achieve good OOPS design. These principles can help to ensure 
that the code is readable, reusable, maintainable, and testable. Some of the benefits of applying these principles are:

Single responsibility: A class or a method should have only one responsibility or reason to change. This can help to avoid coupling, 
increase cohesion, and improve modularity2

Open-closed: A class or a method should be open for extension, but closed for modification. This can help to avoid breaking changes, 
reduce bugs, and promote reusability2

Liskov substitution: A subclass should be substitutable for its superclass without affecting the functionality of the system. 
This can help to ensure behavioral correctness, avoid type errors, and support polymorphism2

Interface segregation: A class should not depend on methods that it does not use. This can help to reduce complexity, improve flexibility, 
and avoid unnecessary dependencies2

Dependency inversion: A class should depend on abstractions, not concretions. This can help to achieve loose coupling, high cohesion, 
and easy testing2






No, there are not only two concepts in LLD. I have also mentioned the OOPS and SOLID principles, which are also important to understand 
and apply in LLD. These principles can help to ensure that the code is readable, reusable, maintainable, and testable.

To complete the Low Level Design, you need to follow a step-by-step refinement process that is based on the High Level Design. 
You need to:

Identify the classes and objects that represent the entities and behaviors of the system.
Define the attributes and methods of each class and object, and specify their visibility and accessibility using access modifiers.
Establish the relationships and associations between the classes and objects, such as inheritance, aggregation, composition, dependency, etc.

Use OOPs concepts such as abstraction, encapsulation, polymorphism, etc. to design the classes and objects in a modular and flexible way.

Use SOLID principles such as single responsibility, open-closed, Liskov substitution, interface segregation, dependency inversion, etc. 
to achieve good OOPs design and avoid common pitfalls and bad practices.

Use UML diagrams such as class diagram, sequence diagram, state diagram, etc. to visualize the structure and behavior of the system and 
its components, and to communicate the design to other stakeholders.

Write the pseudocode or the actual code for the methods and operations of the classes and objects, using the appropriate programming language 
and syntax.

Test and debug the code to ensure that it meets the functional and non-functional requirements of the system, and that it is free of errors 
and bugs.




The difference between LLD and HLD is that LLD stands for Low-Level Design and HLD stands for High-Level Design. 
These are two types of design processes that are used to create software systems. LLD and HLD have different purposes, 
levels of detail, and participants.

LLD is a component-level design process that follows a step-by-step refinement process. 
It is based on the HLD that describes the overall architecture and functionality of the system. LLD provides the 
internal logical design of the actual program code, such as the class diagrams, methods, relations, and specifications. 
It helps the programmer to directly code the program from the document, with minimal debugging and testing. 
LLD also ensures lower cost and easier maintenance of the software. 
LLD is created by designers and developers, and it is also known as micro-level or detailed design1

HLD is a general system design process that refers to the overall system design. It describes the overall description or architecture 
of the application. It includes the description of system architecture, database design, brief description of systems, services, 
platforms, and relationships among modules. It is also known as macro-level or system design. 
It is created by solution architects, and it converts the business or client requirement into a high-level solution. 
HLD is created before LLD, and it is used as a basis for LLD1





