'''
(1)Number or string is Palindrome or not?
(2)Generate an Infinite Fibonacci Series using Generator
(3)Generate an Infinite Fibonacci Series using Recursion
(4)Short a Dictionary with Dictionary Comprehension
(5)Short a List without Using the Sort Keyword
(6)Find Required Output
(7)Manipulate on String and List
(8)Python Program to Swap Two Numbers without Using a Third Variable
(9)Find Prime Numbers Between 0 and 100
(10)Find the Smallest Positive Number in a List
(11). Find the Factorial of a Number?

'''

'''Practical exercises:'''

'''1. Reverse a String:'''
def reverse_string(input_string):
    return input_string[::-1]

input_str = "Hello, World!"
reversed_str = reverse_string(input_str)
print(reversed_str)


'''2. Find Prime Numbers Between 1 and 100:'''
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

prime_numbers = [num for num in range(1, 101) if is_prime(num)]
print(prime_numbers)


'''3. Check if a Number is Palindrome:'''
def is_palindrome(number):
    return str(number) == str(number)[::-1]

num = 121
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")


'''4. Find the Factorial of a Number:'''
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}")


'''5. Implement Binary Search Algorithm:'''
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

'''6. Implement Quicksort Algorithm:'''
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
print(sorted_list)

'''7. Implement a Linked List, Hash Table, Graph, Web Server, and Web Scraping** are more complex tasks that require a significant amount of code and cannot be provided in a simple code snippet. Each of these topics would require separate programs with a detailed explanation.'''


# (1)Write a program to print the given number is odd or even.

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

# (2)Write a program to find if the given number is prime or not.
   
num = int(input("enter a number for prime checking: "))
# input: 23
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

# (3)Write a program to check if the given number is palindrome or not.

num = int(input("Enter a number for palindrome checking: "))
# Input: 12321
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

# (4)Write a program to check if the given number is Armstrong or not.
num = int(input("Enter a number for armstrong checking: "))
# Input: 407
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

# (5)Write a program to find a factorial of a number.
   
num = int(input("Enter a number for factorial checking: "))
# 7
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

# (6)Write a program to find a fibonacci of a number.

nterms = int(input("How many terms? "))
# 7
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

# (7)How to sort a list of tuples by index?
       
# Example list of tuples
list_of_tuples = [(3, 2, 1), (1, 4, 2), (5, 3, 0)]

# Specify the index by which you want to sort (e.g., index 1)
index_to_sort = 1

# Use the sorted function with a lambda function as the key
sorted_list = sorted(list_of_tuples, key=lambda x: x[index_to_sort])

# Print the sorted list
print(sorted_list)


# (8)How to sort a list of dictionaries by key?

# Example list of dictionaries
list_of_dicts = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

# Specify the key by which you want to sort (e.g., 'name')
key_to_sort = 'name'

# Use the sorted function with a lambda function as the key
sorted_list = sorted(list_of_dicts, key=lambda x: x[key_to_sort])

# Print the sorted list
print(sorted_list)



# Remove element from string based on given index

String_value = str(input("Enter your string:"))
index_value = int(input("Enter your index"))

new = list(String_value)
final = [value for index, value in enumerate(new, start=1) if index % index_value != 0]
print(final)
