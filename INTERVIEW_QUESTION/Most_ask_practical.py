# ============================================
#           PRACTICAL EXERCISES: QUESTIONS
# ============================================

# --------- STRING PRACTICALS ---------
'''
(1) Reverse a String  
(12) Find the Most Frequent Character in a String

# --------- LIST PRACTICALS ---------
(14) Find Maximum and Minimum Values in a List  
(13) Find Non-Repetitive Elements in a List Without Using Count  
(20) Flatten Nested List  
(4) Sort a List without Using the Sort Keyword (Quicksort)  
(5) Implement Binary Search Algorithm

# --------- DICTIONARY PRACTICALS ---------
(21) Flatten a Nested Dictionary  
(15) Remove Duplicate Values from a Dictionary

# --------- LOGIC/ALGORITHM PRACTICALS ---------
(2) Find Prime Numbers Between 1 and 100  
(1) Number or String is Palindrome or not  
(11) Find the Factorial of a Number  
(2) Generate an Infinite Fibonacci Series using Generator  
(3) Generate an Infinite Fibonacci Series using Recursion  
(17) Modify List by Inserting/Removing Element  
(19) Dictionary: Add/Remove key-value  
(7) Remove element from string based on given index interval  
(16) Output: Reverse the words of a string (e.g., 'The sky is blue' -> 'blue is sky The')
'''

# ================================
#         LIST PROGRAMS
# ================================

# (17) Modify List by Inserting/Removing Element
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 10)           # Add an element at specific index
my_list.remove(3)               # Remove element by value
del my_list[0]                  # Remove element by index
print("List after modifications:", my_list)

# (6) Extract every 3rd element
my_list = [1, 2, 54, 22, 44, 5, 13, 23, 3]
result = [value for index, value in enumerate(my_list, start=1) if index % 3 == 0]
print("Every 3rd element in the list:", result)

# (10) Find the Smallest Positive Number in a List
a = [2, 3, 4, 1, 32, 31]
small = None
for num in a:
    if num > 0:
        if small is None or num < small:
            small = num
print("The smallest positive number in the list is:", small)

# (14) Find Maximum and Minimum Values in a List
my_list = [1,2,4,12,45,32,4,36,6]
maximum = my_list[0]
minimum = my_list[0]
for i in my_list:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
print(f"Maximum: {maximum} Minimum:{minimum}")

# (13) Find Non-Repetitive Elements in a List Without Using Count
my_list = [1, 2, 3, 4, 2, 3, 5, 6, 7, 7, 8]
def find_non_repetitive_elements(lst):
    element_count = {}
    for element in lst:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    non_repetitive_elements = [element for element, count in element_count.items() if count == 1]
    return non_repetitive_elements
result = find_non_repetitive_elements(my_list)
print("Non-repetitive elements in the list:", result)

# (16) Remove duplicate values from list
my_list = [1, 2, 4, 3, 5, 6, 2, 9, 9, 4, 2, 5, 7, 8]
new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print("List after removing duplicates:", new_list)

# (20) Flatten list in list
my_list = [1,2,3,[4,5,6],[7,8,9]]
flat_list = []
for i in my_list:
    if type(i) is list:
        for items in i:
            flat_list.append(items)
    else:
        flat_list.append(i)
print("Flatter list:", flat_list)

# (6 & 4) Sort a list (Quicksort, without using sort)
def Quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [ x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot ]
    return Quicksort(left) + middle + Quicksort(right)
my_list = [1,2,4,2,3,5,3,4,6,2,3]
sorted_list = Quicksort(my_list)
print("Sorted List:", sorted_list)

# (3) Generate Fibonacci Series by List Equation
def fibbo(n):
    new = [0,1]
    for i in range(n):
        if i < 2:
            pass
        else:
            sum = new[-2] + new[-1]
            new.append(sum)
    return new
print("Fibonacci by list:", fibbo(5))

# Practical: Binary Search Algorithm
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_list = [1, 3, 5, 7, 9, 11, 13]
target = 7
index = binary_search(sorted_list, target)
print(f"Target {target} found at index {index}")

# Practical: Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

unsorted_list = [3, 6, 8, 10, 1, 2, 1]
sorted_list = quicksort(unsorted_list)
print("Quicksorted:", sorted_list)


# ================================
#         STRING PROGRAMS
# ================================

# (18) String modifications
my_string = "hello"
my_string += '!'                         # Add char at end
my_string = my_string[:2] + 'X' + my_string[2:]   # Add at specific index
my_string = my_string[:-1]               # Remove last char
my_string = my_string[:1] + my_string[2:]   # Remove at specific index
print("String after modifications:", my_string)

# (7) Modify string by removing characters at chosen index interval
string_value = str(input("Enter your string: "))
index_value = int(input("Enter your index: "))
new_string = list(string_value)
modified_string = [value for index, value in enumerate(new_string, start=1) if index % index_value != 0]
print("Modified string (skip every Nth):", ' '.join(modified_string))

# (16) Required output in string: Reverse words
s = "The sky is blue"
l = s.split()
print("Words before reverse:", l)
l = l[::-1]
print("Words after reverse:", l)
l = ' '.join(l)
print("Reversed sentence:", l)

# (12) Find the most frequent character in a string
string_value = "Dhruvish patel"
ch = {}
for i in string_value:
    if i in ch:
        ch[i] += 1
    else:
        ch[i] = 1
max_char = max(ch, key=ch.get)
print("Most frequent char:", max_char)

# Practical: Reverse a String
def reverse_string(input_string):
    return input_string[::-1]
input_str = "Hello, World!"
reversed_str = reverse_string(input_str)
print("Reversed string:", reversed_str)


# ================================
#       DICTIONARY PROGRAMS
# ================================

# (19) Dict Programs: add, remove key-value
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict['d'] = 4                         # Add key-value pair
del my_dict['b']                         # Remove by key
print("Dictionary after modifications:", my_dict)

# (8) How to sort a list of dictionaries by key?
list_of_dicts = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]
key_to_sort = 'name'
sorted_list = sorted(list_of_dicts, key=lambda x: x[key_to_sort])
print("List of dicts sorted by key:", sorted_list)

# (5) Sort dictionary by dict comprehension
original_dict = {'banana': 3, 'apple': 1, 'orange': 2}
# Sort by keys
sorted_dict_keys = {k: original_dict[k] for k in sorted(original_dict)}
# Sort by values
sorted_dict_values = {k: v for k, v in sorted(original_dict.items(), key=lambda item: item[1])}
print("Original Dictionary:", original_dict)
print("Sorted by Keys:", sorted_dict_keys)
print("Sorted by Values:", sorted_dict_values)

# (15, 19) Remove duplicate values in dictionary
test_dict = {'gfg': 10, 'is': 15,'best': 20, 'for': 10, 'geeks': 20}
def removeduplicatefromdict(dict):
    new_list = []
    new_dict = {}
    for key,value in dict.items():
        if value not in new_list:
            new_dict[key] = value
            new_list.append(value)
    return new_dict
print("Dictionary after removing duplicate value:", removeduplicatefromdict(test_dict))

# (21) Flatten dictionary in single dictionary
def flatten_dict(d):
    flattened_dict = {}
    for key, value in d.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                flattened_dict[key + '_' + sub_key] = sub_value
        else:
            flattened_dict[key] = value
    return flattened_dict
nested_dict = {
    "Name": "DHRUVISH",
    "AGE": 21,
    "CITY": {
        "AMD": "Ahmedabad",
        "VD": "Vadodara"
    }
}
flattened_dict = flatten_dict(nested_dict)
print("Flattened dict:", flattened_dict)

# ================================
#      LOGICAL/ALGORITHM PROGRAMS
# ================================

# (1) Number or string is palindrome or not
def is_palindrome_number(number):
    str_number = str(number)
    length = len(str_number)
    for i in range(length):
        if str_number[i] != str_number[length - 1 - i]:
            return False
    return True
num = 121
if is_palindrome_number(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

# (3 & 1) Check if a given number is palindrome (alternative)
def is_palindrome(number):
    return str(number) == str(number)[::-1]
num = 121
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

# (2) Generate an infinite Fibonacci series using Generator
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fibonacci_gen = fibonacci_generator()
for _ in range(10):
    print("Next Fibonacci (generator):", next(fibonacci_gen))

# (3) Generate an infinite Fibonacci series by using Recursion (prints first 10)
def recur_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recur_fibonacci(n - 1) + recur_fibonacci(n - 2)
n = 10        # Number of terms to print
if n <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence (recursion):")
    for i in range(n):
        print(recur_fibonacci(i))

# (3, again) Recursion Demo for Fibonacci (with collecting elements)
def fibbo_recur(n):
    if n < 2:
        return n
    else:
        return fibbo_recur(n-1) + fibbo_recur(n-2)
new = [0,1]
for i in range(2,5):
    s1 = fibbo_recur(i)
    new.append(s1)
print("Fibonacci collected in list:", new)

# (8) Swap two numbers without using third variable
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
a = a + b
b = a - b
a = a - b
print("After swapping:")
print("a =", a)
print("b =", b)

# (9) Find prime numbers between 0 and 100
a = 100
print("Primes with loop:")
for i in range(2, a):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
print("Primes with all():")
for num in range(2, 101):
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
        print(num)

# (10, 11, 4) Find the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}")

# (22) Preventing Multiple Consecutive Calls to a Function
def my_function(a, b, c):
    global call_count
    if call_count >= 1:
        raise ValueError("Function can only be called once")
    call_count += 1
    return a + b + c

call_count = 0   # Initializing the call_count

try:
    print(my_function(1, 2, 3))  # First call
    print(my_function(4, 5, 6))  # Second call
except ValueError as e:
    print("Error occurred:", e)

# ================================
#         PRACTICAL SNIPPETS
# ================================

# (2) Find Prime Numbers Between 1 and 100
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
prime_numbers = [num for num in range(1, 101) if is_prime(num)]
print("Primes with list comprehension:", prime_numbers)

# (1) Write a program to print the given number is odd or even.
num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))

# (2) Write a program to find if the given number is prime or not.
num = int(input("enter a number for prime checking: "))
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

# (3) Write a program to check if the given number is palindrome or not.
num = int(input("Enter a number for palindrome checking: "))
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
    print('Palindrome')
else:
    print("Not Palindrome")

# (4) Write a program to check if the given number is Armstrong or not.
num = int(input("Enter a number for armstrong checking: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")

# (5) Write a program to find a factorial of a number.
num = int(input("Enter a number for factorial checking: "))
factorial = 1
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)

# (6) Write a program to find a fibonacci of a number.
nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

# (7) How to sort a list of tuples by index?
list_of_tuples = [(3, 2, 1), (1, 4, 2), (5, 3, 0)]
index_to_sort = 1
sorted_list = sorted(list_of_tuples, key=lambda x: x[index_to_sort])
print("Sorted tuples by index:", sorted_list)

# Remove element from string based on given index
String_value = str(input("Enter your string:"))
index_value = int(input("Enter your index"))
new = list(String_value)
final = [value for index, value in enumerate(new, start=1) if index % index_value != 0]
print("String after removing by index interval:", final)
