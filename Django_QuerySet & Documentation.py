"""***************************************   Performing Query using Django ORM  ***************************************"""

""" Official Reference from :  https://docs.djangoproject.com/en/3.2/ref/models/querysets  for "Perform Queries in SQL & Django both"

                         

https://www.youtube.com/watch?v=c0x_AaPjNCY


*****************************     DJANGO DOCUMENTATION -  https://docs.djangoproject.com/en/4.2/contents/     ***************************
                                            



******************************************************************************************************************************************
                        
                        1. Getting Started              https://docs.djangoproject.com/en/4.2/intro/
                        
******************************************************************************************************************************************


	1.a) Django at a glance					        https://docs.djangoproject.com/en/4.2/intro/overview/
		Design your model
		Design your URLs
		Write your views
		Design your templates

	1.b) Quick install guide					    https://docs.djangoproject.com/en/4.2/intro/install/
		Set up a database
		
	1.c) Writing your first Django app, part 1		https://docs.djangoproject.com/en/4.2/intro/tutorial01/
		Creating a project	
		The development server
		Creating the Polls app
		Write your first view

	1.d) Writing your first Django app, part 2		https://docs.djangoproject.com/en/4.2/intro/tutorial02/
		Database setup
		Creating models
		Activating models
		Playing with the API
		Introducing the Django Admin

	1.e) Writing your first Django app, part 3		https://docs.djangoproject.com/en/4.2/intro/tutorial03/
		Writing more views
		Write views that actually do something
		Raising a 404 error
		Removing hardcoded URLs in templates
		Namespacing URL names

	1.f) Writing your first Django app, part 4		https://docs.djangoproject.com/en/4.2/intro/tutorial04/
		Use generic views: Less code is better

	1.g) Writing your first Django app, part 5		https://docs.djangoproject.com/en/4.2/intro/tutorial05/
		Introducing automated testing
		Writing our first test
		Test a view

	1.h) Writing your first Django app, part 6		https://docs.djangoproject.com/en/4.2/intro/tutorial06/
		

	1.i) Writing your first Django app, part 7		https://docs.djangoproject.com/en/4.2/intro/tutorial07/
		Customize the admin form
		

	1.j) Writing your first Django app, part 8		https://docs.djangoproject.com/en/4.2/intro/tutorial08/
		Installing Django Debug Toolbar

	1.k) Advanced tutorial: How to write reusable apps		https://docs.djangoproject.com/en/4.2/intro/reusable-apps/
		Your project and your reusable app
		Installing some prerequisites
		Using your own package
		Publishing your app
		Installing Python packages with a virtual environment
		
	1.l) Writing your first patch for Django			https://docs.djangoproject.com/en/4.2/intro/contributing/
		
	



******************************************************************************************************************************************
                            
                            2. Using Django		https://docs.djangoproject.com/en/4.2/topics/
                            
******************************************************************************************************************************************


	2.a) How to install Django      https://docs.djangoproject.com/en/4.2/topics/install/
		Install Apache and mod_wsgi
		Get your database running
		Install the Django code


***	2.b) Models and databases		    https://docs.djangoproject.com/en/4.2/topics/db/
	 ***Models                          https://docs.djangoproject.com/en/4.2/topics/db/models/
     ***Making queries                  https://docs.djangoproject.com/en/4.2/topics/db/queries/
     ***Aggregation                     https://docs.djangoproject.com/en/4.2/topics/db/aggregation/
        Search                          https://docs.djangoproject.com/en/4.2/topics/db/search/
     ***Managers                        https://docs.djangoproject.com/en/4.2/topics/db/managers/
        Performing raw SQL queries      https://docs.djangoproject.com/en/4.2/topics/db/sql/
        Database transactions           https://docs.djangoproject.com/en/4.2/topics/db/transactions/
        Multiple databases              https://docs.djangoproject.com/en/4.2/topics/db/multi-db/
        Tablespaces                     https://docs.djangoproject.com/en/4.2/topics/db/tablespaces/
        Database access optimization    https://docs.djangoproject.com/en/4.2/topics/db/optimization/
        Database instrumentation        https://docs.djangoproject.com/en/4.2/topics/db/instrumentation/
        Fixtures                        https://docs.djangoproject.com/en/4.2/topics/db/fixtures/
        Examples of model relationship API usage    https://docs.djangoproject.com/en/4.2/topics/db/examples/


	2.c) Handling HTTP requests		https://docs.djangoproject.com/en/4.2/topics/http/
	    URL dispatcher
        Writing views
        View decorators
        File Uploads
        Django shortcut functions
        Generic views
        Middleware
        How to use sessions


	2.d) Working with forms		        https://docs.djangoproject.com/en/4.2/topics/forms/
        HTML forms
        Django’s role in forms
        Forms in Django
        Building a form
        More about Django Form classes
        Working with form templates
        
        
	2.e) Templates				        https://docs.djangoproject.com/en/4.2/topics/templates/
        
        
	2.f) Class-based views			    https://docs.djangoproject.com/en/4.2/topics/class-based-views/
        Introduction to class-based views
        Built-in class-based generic views
        Form handling with class-based views
        Using mixins with class-based views
        Usage in your URLconf
        Subclassing generic views
        Asynchronous class-based views


	2.g) Migrations				    https://docs.djangoproject.com/en/4.2/topics/migrations/
        The Commands
        Transactions
        Dependencies
        Migration files
        Adding migrations to apps
        Reversing migrations
        Considerations when removing model fields
        Data Migrations
        Serializing values
        
        
	2.h) Managing files			    https://docs.djangoproject.com/en/4.2/topics/files/
        
	2.i) Testing in Django			https://docs.djangoproject.com/en/4.2/topics/testing/
        
        
***	2.j) User authentication in Django		https://docs.djangoproject.com/en/4.2/topics/auth/
        
        
	2.k) Django’s cache framework	https://docs.djangoproject.com/en/4.2/topics/cache/
        
	2.l) Conditional View Processing	https://docs.djangoproject.com/en/4.2/topics/conditional-view-processing/
        
	2.m) Cryptographic signing		https://docs.djangoproject.com/en/4.2/topics/signing/
        
	2.n) Sending email			    https://docs.djangoproject.com/en/4.2/topics/email/
        
	2.o) Internationalization and localization	https://docs.djangoproject.com/en/4.2/topics/i18n/
        
	2.p) Logging 				    https://docs.djangoproject.com/en/4.2/topics/logging/
        
	2.q) Pagination				    https://docs.djangoproject.com/en/4.2/topics/pagination/
        The Paginator class
        Paginating a ListView
        Using Paginator in a view function

	2.r) Security in Django		    https://docs.djangoproject.com/en/4.2/topics/security/
        Cross site scripting (XSS) protection
        Cross site request forgery (CSRF) protection
        SQL injection protection
        Clickjacking protection
        SSL/HTTPS
        Host header validation
        Session security
        User-uploaded content
    
	2.s) Performance and optimization	https://docs.djangoproject.com/en/4.2/topics/performance/
        General approaches
        Caching
        Understanding laziness
        Databases
        HTTP performance
        Template performance

	2.t) Serializing Django objects	https://docs.djangoproject.com/en/4.2/topics/serialization/
        Serializing data
        Deserializing data
        Serialization formats
        Natural keys
    
	2.u) Django settings			https://docs.djangoproject.com/en/4.2/topics/settings/
        Security
        Creating your own settings
        Using settings without setting DJANGO_SETTINGS_MODULE

	2.v) Signals				https://docs.djangoproject.com/en/4.2/topics/signals/
        Listening to signals
        Defining and sending signals
        Disconnecting signals

	2.w) System check framework	https://docs.djangoproject.com/en/4.2/topics/checks/
        
	2.x) External packages			https://docs.djangoproject.com/en/4.2/topics/external-packages/
        
	2.y) Asynchronous support		https://docs.djangoproject.com/en/4.2/topics/async/
        Async views
        Async safety
        Async adapter functions



******************************************************************************************************************************************
                            
                            3. "How-to"  		https://docs.djangoproject.com/en/4.2/howto/
                            
******************************************************************************************************************************************


	3.a) How to authenticate using REMOTE_USER  -   https://docs.djangoproject.com/en/4.2/howto/auth-remote-user/
	
	3.b) How to use Django’s CSRF protection    -   https://docs.djangoproject.com/en/4.2/howto/csrf/
	
	3.c) How to create custom django-admin commands -   
	
	3.d) How to create custom model fields      -   https://docs.djangoproject.com/en/4.2/howto/custom-model-fields/
	
	3.e) How to write custom lookups            -   https://docs.djangoproject.com/en/4.2/howto/custom-lookups/
	
	3.f) How to implement a custom template backend -   https://docs.djangoproject.com/en/4.2/howto/custom-template-tags/
	
	3.g) How to write a custom storage class    -   https://docs.djangoproject.com/en/4.2/howto/custom-file-storage/

    3.h) How to deploy Django       -   https://docs.djangoproject.com/en/4.2/howto/deployment/
	
	3.i) How to upgrade Django to a newer version   -   https://docs.djangoproject.com/en/4.2/howto/upgrade-version/
	
	3.j) How to provide initial data for models     -   https://docs.djangoproject.com/en/4.2/howto/initial-data/
	
	3.k) How to integrate Django with a legacy database -   https://docs.djangoproject.com/en/4.2/howto/legacy-databases/
	
	3.l) How to configure and use logging           -   https://docs.djangoproject.com/en/4.2/howto/logging/
	
	3.m) How to create CSV output       -   https://docs.djangoproject.com/en/4.2/howto/outputting-csv/
	
	3.n) How to create PDF files        -   https://docs.djangoproject.com/en/4.2/howto/outputting-pdf/
	
	3.o) How to override templates      -   https://docs.djangoproject.com/en/4.2/howto/overriding-templates/
	
	3.p) How to manage static files (e.g. images, Js, CSS)  -   https://docs.djangoproject.com/en/4.2/howto/static-files/
	
	3.q) How to deploy static files     -   https://docs.djangoproject.com/en/4.2/howto/static-files/deployment/
	
	3.r) How to create database migrations  -   https://docs.djangoproject.com/en/4.2/howto/writing-migrations/
	
	
	
	
		
		






***********************************************************************************************************************************************




class Person(models.Model):
    name = models.CharField(max_length=50, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, blank=True)




*********************************************    Perform Queries in SQL & Django both     ********************************************


1. GET / SELECT / FETCH Query
*****************************


1. FETCH ALL ROW

SQL
SELECT * FROM Person;
ORM
persons = Person.objects.all()


2. FETCH SPECIFIC COLUMNS

SQL
SELECT name, age FROM Person;
ORM
Person.objects.only('name', 'age')


3. FETCH DISTINCT ROWS

SQL
SELECT DISTINCT name, age FROM Person;
ORM
Person.objects.values('name', 'age').distinct()


4. FETCH SPECIFIC NUMBER OF ROWS

SQL
SELECT * FROM Person LIMIT 10;
ORM
Person.objects.all()[:10]


5. LIMIT AND OFFSET KEYWORDS

SQL
SELECT * FROM Person OFFSET 5 LIMIT 5;
ORM
Person.objects.all()[5:10]


6. FILTER BY SINGLE COLUMN

SQL
SELECT * FROM Person WHERE id = 1;
ORM
Person.objects.filter(id=1)


7. FILTER BY COMPARISON OPERATORS

SQL
SELECT * from Person WHERE age > 18;
SELECT * from Person WHERE age >= 18;
SELECT * from Person WHERE age < 18;
SELECT * from Person WHERE age <= 18;
SELECT * from Person WHERE age != 18;

ORM
Person.objects.filter(age__gt=18)
Person.objects.filter(age__gte=18)
Person.objects.filter(age__lt=18)
Person.objects.filter(age__lte=18)
Person.objects.exclude(age=18)


8. BETWEEN 

SQL
SELECT * FROM Person WHERE age BETWEEN 10 AND 20;
ORM
Person.objects.filter(age__range=(10, 20))


9. LIKE OPERATOR

SQL
SELECT * from Person WHERE name like '%A%';
SELECT * from Person WHERE name like 'A%';
SELECT * from Person WHERE name like '%A';

ORM
Person.objects.filter(name__icontains='A')
Person.objects.filter(name__istartswith='A')
Person.objects.filter(name__iendswith='A')


10. IN Operator

SQL
SELECT * from Person WHERE id in (1, 2);
ORM
Person.objects.filter(id__in=[1, 2])]


11. AND 

SQL
SELECT * FROM Person WHERE gender='male' AND age > 25;
ORM
Person.objects.filter(gender='male', age__gt=25)


12. OR 

SQL
SELECT * FROM Person WHERE gender='male' OR age > 25;
ORM
from django.db.models import Q
Person.objects.filter(Q(gender='male') | Q(age__gt=25)))


13. NOT

SQL
SELECT * FROM Person WHERE NOT gender='male';
ORM
Person.objects.exclude(gender='male')


14. NULL 

SQL
SELECT * FROM Person WHERE age is NULL;
ORM
Person.objects.filter(age__isnull=True)

# Alternate approach
Person.objects.filter(age=None)


15. NOT Null

SQL
SELECT * FROM Person WHERE age is NOT NULL;
ORM
Person.objects.filter(age__isnull=False)

# Alternate approach
Person.objects.exclude(age=None)


16. ASCENDING ORDER

SQL
SELECT * FROM Person order by age;
ORM
Person.objects.order_by('age')


17. DESCENDING ORDER

SQL
SELECT * FROM Person ORDER BY age DESC;
ORM
Person.objects.order_by('-age')




2. CREATE / INSERT Query
************************


18. INSERT INTO

SQL
INSERT INTO Person VALUES ('Jack', '23', 'male');
ORM
Person.objects.create(name='jack', age=23, gender='male)


Bulk Insert using bulk_create
Person.objects.bulk_create([Person(name="Poonam", age=20, gender="Female"), Person(name="Jaanvi", age=23, gender="Female")])



3.  UPDATE / MODIFY QUERY
*************************


19. UPDATE SINGLE ROW

SQL
UPDATE Person SET age = 20 WHERE id = 1;
ORM
person = Person.objects.get(id=1)
person.age = 20
person.save()


20. UPDATE MULTIPLE ROWS

SQL
UPDATE Person SET age = age * 1.5;
ORM
from django.db.models import F
# it will be applied in all the row of age columns
Person.objects.update(age=F('age')+2.5) 
Person.objects.update(age=F('age')-2.5)
Person.objects.update(age=F('age')*1.5)



4. DELETE QUERY
***************


21. DELETE ALL ROWS

SQL
DELETE FROM Person;
ORM
Person.objects.all().delete()


22. DELETE SPECIFIC ROWS

SQL
DELETE FROM Person WHERE age < 10;
ORM
Person.objects.filter(age__lt=10).delete()


Aggregation -->  

23. MIN FUNCTION

SQL
SELECT MIN(age) FROM Person;
ORM
from django.db.models import Min
 
Person.objects.all().aggregate(Min('age'))
{'age__min': 0}


24. MAX FUNCTION

SQL
SELECT MAX(age) FROM Person;
ORM
from django.db.models import Max
 
Person.objects.all().aggregate(Max('age'))
{'age__max': 0}


25. AVG FUNCTION

SQL
SELECT AVG(age) FROM Person; 
ORM
from django.db.models import Avg
 
Person.objects.all().aggregate(Avg('age')) 
{'age__avg': 50}


26. SUM FUNCTION

SQL
SELECT SUM(age) FROM Person; 
ORM
from django.db.models import Sum
 
Person.objects.all().aggregate(Sum('age')) 
{'age__sum': 5050}


27. COUNT FUNCTION

SQL
SELECT COUNT(*) FROM Person; 
ORM
Person.objects.count()


28. GROUP BY

SQL
SELECT gender, COUNT(*) as count FROM Person GROUP BY gender; 
ORM
Person.objects.values('gender').annotate(count=Count('gender'))


29. HAVING 

SQL
--> Count of Person by gender if number of person is greater than 1 

SELECT gender, COUNT('gender') as count
FROM Person
GROUP BY gender 
HAVING count > 1;

ORM
Person.objects.annotate(count=Count('gender')).values('gender', 'count').filter(count__gt=1)







************************************************************     JOIN       ************************************************************


Consider A Foreign Key Relationship Between Books And Publisher

class Publisher(models.Model):
     name = models.CharField(max_length=100)

class Book(models.Model):
     publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
     
     


30. Fetch Publisher Name For a Book

SQL
SELECT name FROM Book  LEFT JOIN  Publisher  ON  Book.publisher_id = Publisher.id  WHERE  Book.id=1;

ORM
book = Book.objects.select_related('publisher').get(id=1)
book.publisher.name



31. Fetch books which have specific publisher

SQL
SELECT * FROM Book WHERE Book.publisher_id = 1;

ORM
publisher = Publisher.objects.prefetch_related('book_set').get(id=1)
books = publisher.book_set.all()





***************************************************   Raw SQL queries in Django views   *************************************************** 



from django.db import connection
cursor = connection.cursor()
cursor.execute('''SELECT * FROM Person''') 
person = cursor.fetchall

for person in persons:
  print(person.name)
  print(person.gender)
  print(person.age)
  
  
  
***************************************************   SQl queries in Django ORM in views   ***************************************************



Person.objects.all()
      
-----Example print in django----
persons = Person.objects.all()
      
for person in persons:
  print(person.name)
  print(person.gender)
  print(person.age)













************************************************************************************************************************************************
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   QUERYSET REFERENCE FROM DOCUMENTATION  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
************************************************************************************************************************************************


What is Model:
A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re 
storing. Generally, each model maps to a single database table.
https://docs.djangoproject.com/en/3.2/topics/db/models/




******************************************************    Model Field References:    ***************************************************


1. Field Options:
https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-options
null, blank, choices, default, primary_key, unique, verbose_name and etc.


2. Field Types:
https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types

AutoField
BinaryField
BooleanField
CharField
DateField
DateTimeField
DecimalField
EmailField
FileField
FloatField
ImageField
IntegerField
JSONField - A field for storing JSON encoded data. In Python the data is represented in its Python native format: dictionaries, lists, strings, 
    numbers, booleans and None. JSONField is supported on MariaDB 10.2.7+, MySQL 5.7.8+, SQLite etc.
PositiveIntegerField
SlugField - A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They’re generally used in URLs.
TextField
TimeField
URLField



3. Relationship Fields:
https://docs.djangoproject.com/en/3.2/ref/models/fields/#module-django.db.models.fields.related



3.a) ForeignKey  (referred as for many-to-one)
**********************************************


A many-to-one relationship. Requires two positional arguments: the class to which the model is related and the on_delete option.
name = models.ForeignKey('model_class', on_delete=models.CASCADE)

If we need to create a relationship on a model that has not yet been defined, you can use the name of the model, rather than the 
model object itself:

class Car(models.Model):
    manufacturer = models.ForeignKey( 'Manufacturer', on_delete=models.CASCADE)

class Manufacturer(models.Model):
    pass

Note: A database index is automatically created on the ForeignKey. You can disable this by setting db_index to False.
Behind the scenes, Django appends "_id" to the field name to create its database column name


Note: Prevent deletion of the referenced object by raising RestrictedError (a subclass of django.db.IntegrityError). Unlike PROTECT, deletion 
of the referenced object is allowed if it also references a different object that is being deleted in the same operation


class Artist(models.Model):
    name = models.CharField(max_length=10)

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.RESTRICT)

Artist can be deleted even if that implies deleting an Album which is referenced by a Song, because Song also references Artist itself 
through a cascading relationship.



3.b) ManyToManyField
********************

A many-to-many relationship. Requires a positional argument: the class to which the model is related, which works exactly the same as it does 
for ForeignKey, including recursive and lazy relationships.

friends = models.ManyToManyField("self")   #  ManyToManyField accepts an extra set of arguments – all optional 

Note: Behind the scenes, Django creates an intermediary join table to represent the many-to-many relationship




3.c) OneToOneField
*******************

A one-to-one relationship. Conceptually, this is similar to a ForeignKey with unique=True, but the “reverse” side of the relation will 
directly return a single object.

user = models.OneToOneField( settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
supervisor = models.OneToOneField( settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='supervisor_of' )

This is most useful as the primary key of a model which “extends” another model in some way; Multi-table inheritance is implemented by adding 
an implicit one-to-one relation from the child model to the parent model

One positional argument is required: the class to which the model will be related.

If you do not specify the related_name argument for the OneToOneField, Django will use the lowercase name of the current model as default value.





**********************************************************   Proxy models   *************************************************************

When using multi-table inheritance, a new database table is created for each subclass of a model. This is usually the desired behavior, since 
the subclass needs a place to store any additional data fields that are not present on the base class. Sometimes, however, you only want to 
change the Python behavior of a model – perhaps to change the default manager, or add a new method.

This is what proxy model inheritance is for: creating a proxy for the original model. You can create, delete and update instances of the 
proxy model and all the data will be saved as if you were using the original (non-proxied) model. The difference is that you can change 
things like the default model ordering or the default manager in the proxy, without having to alter the original.

Proxy models are declared like normal models. You tell Django that it’s a proxy model by setting the proxy attribute of the Meta class to True.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class MyPerson(Person):
    class Meta:
        proxy = True

    def do_something(self):
        pass


Note: The MyPerson class operates on the same database table as its parent Person class. In particular, any new instances of Person will also 
be accessible through MyPerson, and vice-versa:








********************************************************************************************************************************************
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    Making Queries   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
********************************************************************************************************************************************

https://medium.com/django-rest/one-to-many-relationship-foreignkey-64f8da35912a
https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html#models



Once we’ve created our data models, Django automatically gives you a database-abstraction API that lets you create, retrieve, update and 
delete objects. 

Data model reference & lookup options  --  https://docs.djangoproject.com/en/3.2/ref/models/


In official Documentation these are the Models on which all the queries will be based on:



class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)



1.  Methods that return new QuerySets

filter()
exclude()
annotate()
order_by()
reverse()
distinct()
values()
values_list()
dates()
datetimes()
all()
select_related()
prefetch_related()



2.  Operators that return new QuerySets

AND (&)
OR (|)


3.  Methods that do not return QuerySets

get()
create()
get_or_create()
update_or_create()
bulk_create()
bulk_update()
count()
latest()
first()
last()
aggregate()
exists()
update()
delete()


4.  Field lookups

exact
iexact
contains
icontains
in
gt
gte
lt
lte
startswith
istartswith
endswith
iendswith
range


5.  Aggregation functions

filter
**extra
Avg
Count
Max
Min
Sum














******************************************************* Django ORM Models  ***********************************************************




from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField()


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)
    genre = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='covers/')
    copies = models.PositiveIntegerField()


class Branch(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()


class Inventory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    stock = models.IntegerField()


class Member(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_date = models.DateField()
    due_date = models.DateField()
    returned_date = models.DateField(null=True, blank=True)




'''

books = Books.objects.prefetch_related(author__name).all().


Retrieve all books that are genre 'Science Fiction' and have been published after 2010


books = Books.objects.filter(genre="Science Fiction").get(publication_date__gt=2010)


Retrieve all publishers, with a count of the number of books they have published:


from django.db.models import Count

publishers = Book.objects.values('publisher').order_by('author').annotate(count=Count('publication_date'))


Retrieve all members who have borrowed(loan) at least 5 books





'''






"""