"""

Write a program to find the result of the Student. Here is a criteria:

Below 26 - Failed (26 excluded)
26-35 - D division
36-50 - C division
51-60 - B division
61-75 - A division
76-85 - A+ division
86-100 - Extra Ordinary Student

"""

def StudentResult(marks):
    if marks>=86:
        print("This Student is Extra Ordinary")
    elif marks<86 and marks>=76:
        print("A+ Division")
    elif marks<76 and marks>=61:
        print("A Division")
    elif marks<61 and marks>=51:
        print("B Division")
    elif marks<51 and marks>=36:
        print("C Division")
    elif marks<36 and marks>=26:
        print("D Division")
    else:
        print("Failed")


# Input a percentage
percentage_input = input("Enter marks as a percentage to find the result : ")
# Remove the percentage symbol and convert to an integer
marks = int(percentage_input.rstrip('%'))

# marks = int(input("Enter a marks to find the result : "))


StudentResult(marks)











"""
*********************************************************** System Design *********************************************************


School Management System:

HLD:

1. System Architecture - client-server architecture. In client side, interfaces for students, teachers, and administrators while in
    server side, databases, authentication, and core functionalities
    
2. Data flow - In client side, Data flows from student enrollment and attendance tracking while in
    server side, grade calculation and report generation
    
3. Database Design - tables for students, teachers, classes, attendance, grades, and administrative information with relationships

4. Interface Design - For students, attendance tracking and grade viewing while Teachers, entering grades and managing attendance.
    Administrators have all the access.

5. Security Design - 

6. Hardware and Software Infrastructure

7. Concurrency and Parallelism

8. Scalability and Performance

9. User Interface Design

LLD:

Module Specification
Data Structure Design
Algorithm Design
Database Schema
Interface Details
Error Handling Mechanisms
Concurrency Control
I/O Design
Security Measures
Code Optimization Techniques
Detailed User Interface Design
Testing Plans
Documentation
Implementation Details
Dependencies




******************************************** With some Physical and Technological components *******************************************




High-Level Design (HLD) Components:
**********************************


System Architecture:

Technology: Client-server architecture using web technologies.
Physical Component: Web server, database server.

Data Flow:

Technology: RESTFul APIs for data exchange.
Physical Component: API endpoints, data pipelines.

Database Design:

Technology: Relational Database Management System (RDBMS) like MySQL or PostgreSQL.
Physical Component: Database server.

Interface Design:

Technology: Web interfaces using HTML, CSS, and JavaScript.
Physical Component: User devices (computers, tablets, smartphones).

Security Design:

Technology: HTTPS for secure communication, user authentication using tokens or sessions.
Physical Component: Secure sockets, authentication server.

Hardware and Software Infrastructure:

Technology: Web server technologies (e.g., Apache, Nginx), programming languages (e.g., PHP, Python).
Physical Component: Server hardware, hosting environment.

Concurrency and Parallelism:

Technology: Multi-threading or asynchronous programming.
Physical Component: Server resources (CPU, memory).

Scalability and Performance:

Technology: Load balancing, caching mechanisms.
Physical Component: Load balancer, cache server.

User Interface Design:

Technology: Frontend frameworks (e.g., React, Angular).
Physical Component: User devices.



Low-Level Design (LLD) Components:
**********************************

Module Specification:

Technology: Object-oriented programming languages (e.g., Java, C#).
Physical Component: Code modules, classes.

Data Structure Design:

Technology: Data structures like arrays, lists, and maps.
Physical Component: Memory.

Algorithm Design:

Technology: Algorithms for data processing, sorting, and searching.
Physical Component: CPU.

Database Schema:

Technology: Database schema definition using SQL.
Physical Component: Database tables, relationships.

Interface Details:

Technology: API specifications (e.g., OpenAPI, Swagger).
Physical Component: API endpoints.

Error Handling Mechanisms:

Technology: Exception handling in programming languages.
Physical Component: Code logic for error handling.

Concurrency Control:

Technology: Locking mechanisms, transaction management.
Physical Component: Database locks.

I/O Design:

Technology: File I/O, network communication.
Physical Component: File systems, network connections.

Security Measures:

Technology: Encryption algorithms, access control lists (ACLs).
Physical Component: Encryption libraries, authentication server.

Code Optimization Techniques:

Technology: Compiler optimizations, code profiling tools.
Physical Component: Compilation process.

Detailed User Interface Design:

Technology: Frontend code specifying UI components and interactions.
Physical Component: User devices.

Testing Plans:

Technology: Testing frameworks (e.g., JUnit, Selenium).
Physical Component: Test environments, testing tools.

Documentation:

Technology: Documentation tools (e.g., Javadoc, Doxygen).
Physical Component: Documentation files.

Implementation Details:

Technology: Version control systems (e.g., Git), Integrated Development Environments (IDEs).
Physical Component: Code repositories, development machines.

Dependencies:

Technology: Dependency management tools (e.g., Maven, npm).
Physical Component: Dependency repositories.







"""