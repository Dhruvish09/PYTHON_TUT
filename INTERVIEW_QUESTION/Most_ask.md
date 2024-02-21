(1)Diff between list and dict?
(2)Diff between append and extend?
(3)Can we use a list/tuple or list inside a tuple as key in dict?
(4)Why python is dynamic typed programming language? or what is Duck typing?
(5)why python is interpreted language?
(6)What is lambda function?
(7)What does python support? call by reference or call by value?
(8)What do you mean by MRO in python?
(9)What if we don't use with statement?
(10)What do you mean by OOPS?

(3)Can we use a list/tuple or list inside a tuple as key in dict?\
Ans:We can use only immutable type as key in dict.
    So we can use tuple as key but not list as key.

(4)Why python is dynamic typed programming language? or what is Duck typing?
Ans:
    Because in python we don't requried data type at time of declration of  variable.

(5)why python is interpreted language?
Ans:
    Interpreted means code run line by line.In interpreted language directly compile code convert into machine code. 


(7)What does python support? call by reference or call by value?
Ans:
    Python support both call by reference and call by value.

(8)What do you mean by MRO in python?
Ans:
    Method Resolution Order
    MRO is concept use in inheritance.
    MRO from bottom to top and left to right.

(9)What if we don't use with statement?
Ans: With methods: __enter__ and __exit__
    Example:

        with open("hello.txt","w") as file:
            file.write("Hello, world")
    
    
    if we not use with then we have to close manually.
    Example:

        file = open("Hello.txt","w")
        file.write = ("Hello,world")
        file.close()

(10)What do you mean by OOPS?

    Construcor:
        A constructor is an instance method in a class, that is automatically called whenever a new object of the class is declared.
        Ex:
            The __init__() method acts as a constructor. It needs a mandatory argument self, which the reference to the object.

(11)Authentication and Authorization:
Ans:
    Authentication verifies the identity of users, while authorization controls their access to resources. For instance, in a web application, I would use JWT (JSON Web Tokens) for authentication and role-based access control (RBAC) for authorization.


(12)How the migration work in django?
Ans:
    (1)Make Changes to Models: Modify your Django models in the models.py file of your application, such as adding, modifying, or deleting fields.
    
    (2)Generate Migrations: Run the command python manage.py makemigrations in your terminal. Django inspects the changes you've made to your models and creates migration files (*.py) in your application's migrations folder, representing these changes.
    
    (3)Review Migration Files: Take a look at the generated migration files to ensure they accurately reflect the changes you've made to your models.
    
    (4)Apply Migrations: Execute the command python manage.py migrate. Django analyzes the migration files and applies the necessary changes to your database schema to match the current state of your models.
    
    (5)Check Migration Status: After applying migrations, Django updates the django_migrations table in your database to keep track of which migrations have been applied. You can check the status of migrations using the command python manage.py showmigrations.
    
    (6)Database Schema Update: Once migrations are applied, your database schema is updated to reflect the changes made to your models.

(13)how Django's ORM operates?
Ans:
    Execute Queries: When you perform operations on querysets (e.g., iterating over them, calling certain methods), Django translates them into SQL queries specific to your database backend.

    For example, Product.objects.all() might result in the execution of the SQL query: SELECT * FROM product;

    Interact with Database: Django's ORM sends these SQL queries to the database and receives the results.

(14)which query is better orm or sql?
Ans:
    ORM:
        Pros:
            (1)Simplicity: ORM queries are easier to read and write, especially for basic operations like CRUD (Create, Read, Update, Delete).

            (2)Portability: ORM queries work across different databases without modifications.
        Cons:
            (1)Performance Overhead: ORM queries might be slower, especially for complex operations.
            (2)Limited Control: Less control over the generated SQL can make performance optimization challenging.
    SQL:

        Pros:
            (1)Performance: SQL queries can be faster, especially for complex operations or when performance is crucial.
            (2)Flexibility: You have full control over the SQL syntax and can utilize database-specific features.
        Cons:
            (1)Complexity: SQL queries can be verbose and harder to write, especially for developers unfamiliar with SQL.
            (2)Portability: SQL queries may require modifications to work across different databases.

(15)which kind of type Django ORM?
Ans:
    Active Record Pattern:
        Data mapping pattern where database records are directly represented by objects in the application code, coupling data and behavior within the same entity.

(16)loading in sql?
Ans:
    In SQL, "loading" refers to the process of transferring data from external sources (such as files or other databases) into a database table. Loading data into a database is typically done using specialized SQL commands or utilities provided by the database management system (DBMS).