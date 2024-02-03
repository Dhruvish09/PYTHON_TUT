**Topics:**

Core Python:
    What is Python?
    What are the key features of Python?
    What are the different types of data types in Python?
    What is the difference between a list and a tuple?
    What is a dictionary in Python?
    What are 'is', 'not', and 'in' operators?
    What is a ternary operator?
    What is the round function?
    What is a docstring?
    What is PYTHONPATH?
    What is [::-1]?
    What is list comprehension?
    What is dictionary comprehension?
    What is the map function?
    What is the filter function?
    What is an iterator?
    What is a generator?
    What is the zip function?
    What is shallow and deep copy?
    What is pickling and unpickling?
    What is PEP 8?

Object-Oriented Programming (OOP):
    What is object-oriented programming?
    What is the difference between inheritance and polymorphism?
    What is a class in Python?
    What is a function in Python?
    What is encapsulation?
    What is abstraction?
    What are dunder/magic methods?
    What are instance and class variables?
    What are static and class methods?

Development Practices:
    What is the pass statement?
    What is the break and continue statements?
    What is a context manager?
    What is monkey patching?
    What is multithreading and multiprocessing?

DevOps:
    What is PYTHONPATH?
    What is your experience with continuous integration and continuous delivery (CI/CD)?

Unit Testing:
    What is your experience with unit testing?
    What is your experience with debugging Python code?
    What is your experience with performance optimization?

Miscellaneous:
    How is memory managed in Python?
    How to sort a list of tuples by index?
    How to sort a list of dictionaries by key?
    What is the Global Interpreter Lock (GIL)?

Cloud Computing:
    What is your experience with cloud computing platforms such as AWS or Azure?

(1) What is Python?
Ans: Python was created by Guido van Rossum and released in 1991. Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.

(2) Why Python?
Ans: Python is a high-level, interpreted programming language that is object-oriented and has dynamic semantics. Python works with Windows, Mac, Linux, Raspberry Pi, and other platforms. Python has a straightforward syntax when compared to other languages. Compared to other programming languages, Python allows developers to write programs with fewer lines.

(3) What kinds of applications can Python be used for?
Ans: Python can be used for various applications, including games for the web and the internet, scientific and computational applications, language development, image processing, graphic design, enterprise and business applications, operating systems, web applications, email processing, and more.

(4) What are the advantages of Python?****
Ans: Python has several advantages, including being an interpreted language, extensible, object-oriented, and providing built-in data structures like tuples, lists, and dictionaries.

(5)What is the pass statement?
    The pass statement is used as a placeholder for future code.
    When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.

    Example: 
    
    for x in [0, 1, 2]:
        pass

(6)What is the break and continue statements?
    Python break Statement:

    The break statement terminates the loop immediately when it's encountered.

    Example:
    for i in range(5):
        if i == 3:
            break
        print(i)

    Python continue Statement:

    The continue statement skips the current iteration of the loop and the control flow of the program goes to the next iteration.

    Example:

    for i in range(5):
        if i == 3:
            continue
        print(i)

(7)What are 'is', 'not', and 'in' operators?

    is Operator:

    The is operator is used to test object identity. It checks if two objects refer to the same instance in memory.
    Example:
    x = [1, 2, 3]
    y = [1, 2, 3]
    
    if x is y:
        print("x and y refer to the same object")
    else:
        print("x and y do not refer to the same object")

    not Operator:

    The not operator is a logical operator used to negate a boolean expression. It reverses the truth value of the expression.
    Example:
    x = True

    if not x:
        print("x is False")
    else:
        print("x is True")

    in Operator:

    The in operator is used to test if a value is present in a sequence (e.g., a string, list, tuple, or set).
    
    Example:

    my_list = [1, 2, 3, 4, 5]

    if 3 in my_list:
        print("3 is present in the list")
    else:
        print("3 is not present in the list")

(8)What is a ternary operator?
    The Python ternary operator determines if a condition is true or false and then returns the appropriate value in accordance with the result. 
    Example:

    age = 20
    result = "You can vote" if age >= 18 else "You cannot vote"
    print(result)

(9)What are *args and **kwargs?
    *args: Allows a function to accept a variable number of positional arguments, collecting them into a tuple.
    Example:
    def myFun(*argv):
	    for arg in argv:
		    print(arg)

    myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


    **kwargs: Enables a function to accept a variable number of keyword arguments, collecting them into a dictionary.
    Example:

    def print_person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    print_person_info(name="Alice", age=30, city="Wonderland")


(10)What are append, extend, and index functions in a list?
    Append() Method:

    The append() method is used to add a single element to the end of a list.
    Example:

    my_list = [1, 2, 3]
    my_list.append(4)
    print(my_list)  # Output: [1, 2, 3, 4]

    Extend() Method:

    The extend() method is used to append elements from an iterable (e.g., another list) to the end of the list.
    Example:
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list1.extend(list2)
    print(list1)  # Output: [1, 2, 3, 4, 5, 6]
    
    Index() Method:

    The index() method is used to find the index of the first occurrence of a specified value in the list.
    Example:
    my_list = [10, 20, 30, 20, 40]
    index = my_list.index(20)
    print(index)  # Output: 1

(11)What are remove and pop functions in a list?
    Remove() Method:

    The remove() method is used to remove the first occurrence of a specified value from the list.
    Example:
    my_list = [10, 20, 30, 20, 40]
    my_list.remove(20)
    print(my_list)  # Output: [10, 30, 20, 40]

    Pop() Method:

    The pop() method is used to remove and return an element from a specific index in the list. If no index is provided, it removes and returns the last element by default.
    Example:
    my_list = [10, 20, 30, 40]
    popped_value = my_list.pop(1)
    print(popped_value)  # Output: 20
    print(my_list)       # Output: [10, 30, 40]

(12)Convert list to a string?

    Example:

    (1) my_list = ['Hello', 'World']
        my_string = ' '.join([str(item) for item in my_list])

    (2) my_list = ['Hello', 'World']
        my_string = ' '.join(map(str, my_list))
    
(13)What is pickling and unpickling?

    Pickling: Pickling in Python refers to the process of serializing an object into a byte stream. This byte stream can be stored in a file, sent over a network, or otherwise persisted. The pickle module in Python provides a convenient way to serialize objects into a binary format.

    Example:

    import pickle

    # Data to be pickled
    data_to_pickle = {'name': 'John', 'age': 30, 'city': 'Example City'}

    # Pickling the data and writing to a file
    with open('data.pkl', 'wb') as file:
        pickle.dump(data_to_pickle, file)

    Unpickling: Unpickling is the process of deserializing a byte stream back into a Python object. It is the reverse of pickling.

    Example:

    import pickle

    # Unpickling the data from the file
    with open('data.pkl', 'rb') as file:
        unpickled_data = pickle.load(file)

    print(unpickled_data)


(14)What is PEP 8?
    The Python Enhancement Proposal, also known as PEP 8, is a document that provides instructions on how to write Python code. In essence, it is a set of guidelines for formatting Python code for maximum readability. Guido van Rossum, Barry Warsaw, and Nick Coghlan wrote it in 2001.

(15)What is zip() capability in Python?
    In Python, zip() is a built-in function that allows you to combine multiple iterable objects (such as lists, tuples, or strings) into an iterator of tuples. 

    Example:

    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']

    zipped = zip(list1, list2)

    # zipped is now an iterator of tuples
    for item in zipped:
        print(item)

(16)What is shallow and deep copy?

    Copying mechanisms where a shallow copy creates a new object but does not create copies of nested objects, and a deep copy creates fully independent copies of both the object and its nested objects.

    Example shallow copy:
    import copy

    original_list = [1, [2, 3], 4]
    shallow_copied_list = copy.copy(original_list)
    
    shallow_copied_list[1][0] = 'X'
    
    print(original_list)          # Output: [1, ['X', 3], 4]
    print(shallow_copied_list)    # Output: [1, ['X', 3], 4]

    Example deepcopy:
    import copy

    original_list = [1, [2, 3], 4]
    deep_copied_list = copy.deepcopy(original_list)

    deep_copied_list[1][0] = 'X'

    print(original_list)          # Output: [1, [2, 3], 4]
    print(deep_copied_list)       # Output: [1, ['X', 3], 4]

(17)What are local and global variables?

    Global Variables:
    A global variable in Python is a variable declared outside any function or block, making it accessible throughout the entire program.

    Example:

    # Global variable
    global_variable = 10

    def modify_global():
        # Accessing and modifying the global variable
        global global_variable
        global_variable += 5

    # Calling the function to modify the global variable
    modify_global()

    Local Variable: 
    A local variable in Python is a variable declared within a function or block of code. It has a limited scope, accessible only within the specific function or block where it is defined.
    Example:

    def my_function():
        local_variable = 42
        print("Inside the function:", local_variable)

    my_function()


(18)What is list comprehension?

    A concise way to create lists using a single line of code.
    Example: squares = [x**2 for x in range(5)]

(19)What is dictionary comprehension?

    Similar to list comprehension but used to create dictionaries.
    Example: my_dict = {x: x**2 for x in range(5)}

(20)What is the map , filter and reduce function?
    Map:-

    The map() function applies a function to each element in a sequence and returns a new sequence containing the transformed elements.
    Example:
    numbers = [1,2,3,4]

    def square(number):
      return number * number

    squared_numbers = map(square, numbers)
    result = list(squared_numbers)
    print(result) 

    # Output: [1,4,9,16]

    Filter:- 

    The filter() function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate.
    Example:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def is_even(x):
        return x % 2 == 0
    
    even_numbers = filter(is_even, numbers)
    
    print(list(even_numbers))
    

    Reduce:-

    The reduce() function is a higher-order function that applies a function to a sequence and returns a single value. 
    Example:

    from functools import reduce

    numbers = [1, 2, 3, 4, 5]

    def multiply(x, y):
        return x * y

    product = reduce(multiply, numbers)

    print(product) 

(21)What is context menager?
    Ans: 
        A context manager in Python is an object that defines the methods __enter__() and __exit__(), allowing you to manage resources, such as file handles or network connections, in a clean and controlled manner. The with statement is typically used to ensure proper resource acquisition and release.

    Example:

    # Define a simple context manager that prints a message when entering and exiting the block
    class SimpleContextManager:
        def __enter__(self):
            print("Entering the 'with' block")
            return self  
            # This object will be assigned to the variable after 'as' in the 'with' statement

        def __exit__(self, exc_type, exc_value, traceback):
            print("Exiting the 'with' block")

    # Use the context manager with the 'with' statement
    with SimpleContextManager() as scm:
        print("Inside the 'with' block")

(22)What are dunder/magic methods?
Ans: 
    Dunder (double underscore) or magic methods in Python are special  methods with names enclosed in double underscores (__). These methods provide a way to customize the behavior of objects, allowing you to define how instances of your classes interact with built-in functions and operators. 

    Example:
    class MyList:
        def __init__(self, data):
            self.data = data

        def __len__(self):
            # Customizing __len__ to count only even numbers in the list
            return sum(1 for num in self.data if num % 2 == 0)

    # Creating an instance of MyList
    my_list = MyList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # Using the custom behavior defined by __len__
    even_count = len(my_list)
    print(f"Number of even elements in my_list: {even_count}")


(23)What is Memory Management in Python:
Ans:
    Memory management in Python involves the allocation, reference tracking, and deallocation of memory to efficiently handle objects during program execution. 
    Python has a built-in garbage collector that recycles all unused memory and makes it available to the heap space.

    The memory manager in Python is responsible for allocating heap space to Python objects. 

    Example:
        # Automatic memory management
        a = [1, 2, 3]   # List creation allocates memory
        b = a           # Reference count increases
        c = a.copy()    # New object created, reference count increased

        del a           # Reference count decreases
        del b           # Reference count decreases
        del c           # Reference count drops to zero, memory deallocated

        # Garbage collection
        # The garbage collector identifies and reclaims memory of objects with zero reference count, including cyclic references.

(24)What is Monkey Patching:
Ans:
    Monkey patching is a programming technique in which existing code or libraries are dynamically modified or extended at runtime. It involves altering or adding functionality to a class or module without modifying its original source code.
    Example:

        # Original class definition
        class OriginalClass:
            def original_method(self):
                return "Original method"

        # Monkey patching to add a new method
        def new_method(self):
            return "Patched method"

        OriginalClass.patched_method = new_method

        # Creating an instance and using the patched method
        obj = OriginalClass()
        result = obj.patched_method()

        print(result)  # Output: Patched method

(25)What is Iterator?
Ans:
    An iterator is an object in Python that allows you to iterate over a sequence of elements, one at a time, without exposing the underlying structure of the data.

    Example:
        mytuple = ("apple", "banana", "cherry")
        myit = iter(mytuple)
        
        print(next(myit))
        print(next(myit))
        print(next(myit))

(26)What is a recursion?
Ans:
    The process in which a function calls itself directly or indirectly is called recursion and the corresponding function is called a recursive function.
    Example:
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(n-1)

        # Example usage:
        result = factorial(5)
        print(f"The factorial of 5 is: {result}")

(27)Function Arguments in Python?
Ans:
    function arguments are the values passed to a function when it is called. 
    
    (1)Positional Arguments:
    def add(x, y):
        return x + y

    result = add(3, 5)

    (2)Keyword Arguments:
    def greet(name, age):
        print(f"Hello, {name}! You are {age} years old.")

    greet(name="Alice", age=25)

    (3)Default Arguments:
    def add(x=1, y=2):
        return x + y

    result = add(3, 5)

    If values are provide in add(3, 5) then it's take  that value otherwise it's take default value.
    If there is value are provide in add(3, 5) then default values (x=1, y=2) are ignored.

    (4)Variable-Length Arguments::
        def print_args(*args, **kwargs):
            print("Positional arguments:", args)
            print("Keyword arguments:", kwargs)

        print_args(1, 2, 3, name="Alice", age=25)

(28)What is a generator?
Ans:
    The generator is a way that determines how to execute iterators.
    In Python, you can create a generator by using the yield statement in a function. The yield statement returns a value from the generator and suspends the execution of the function until the next value is requested.

        Example:
            def my_generator():
                for i in range(5):
                    yield i

            gen = my_generator()
            print(next(gen))
            print(next(gen))
            print(next(gen))
            print(next(gen))
            print(next(gen))

(29)What is decorators?
Ans:
    decorators are a powerful and flexible way to modify or extend the behavior of functions or methods without changing their actual code.

    Example:
        
    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")
        return wrapper

    @my_decorator
    def say_hello():
        print("Hello!")
    
    say_hello()

(30)What is multithreading and multiprocessing?
Ans:
    Multithreading:

        Multithreading is a programming concept where multiple threads (smaller units of a process) execute independently within the same program, sharing the same resources such as memory space. 
        
        A thread in Python is the smallest unit of execution within a process. 

    Multiprocessing:     
        Multiprocessing is a programming paradigm where multiple processes run independently, each with its own memory space. 

        A process is an executable instance of a computer program. Usually, a process is executed in a single sequence of control flow.   


            
            