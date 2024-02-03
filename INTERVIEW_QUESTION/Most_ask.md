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
