'''
(1)Number or string is Palindrome or not?
(2)Generate an Infinite Fibonacci Series using Generator
(3)Generate an Infinite Fibonacci Series using Recursion
(4)Short a Dictionary with Dictionary Comprehension
(5)Short a List without Using the Sort Keyword
(6)Manipulate on String and List
(7)Python Program to Swap Two Numbers without Using a Third Variable
(8)Find Prime Numbers Between 0 and 100
(9)Find the Smallest Positive Number in a List
(10)Find the Factorial of a Number?
(11)Find the Most Frequent Character in a String?
(12)Find Non-Repetitive Elements in a List Without Using Count?
(13)Find Maximum and Minimum Values in a List?
(14)Remove duplicate value from dictionarry

'''

'''Number or string is Palindrome or not?'''
def is_palindrome_number(number):
    str_number = str(number)
    length = len(str_number)

    for i in range(length):
        print(i)
        if str_number[i] != str_number[length - 1 - i]:
            return False

    return True

# Example usage:
num = 121
if is_palindrome_number(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")


'''(1) Generate an infinte fibonaaci series by using Generator?'''

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Example usage:
fibonacci_gen = fibonacci_generator()

# Print the first 10 Fibonacci numbers
for _ in range(10):
    print(next(fibonacci_gen))

'''(2) Generate an infinte fibonaaci series by using Recurssion?'''

def recur_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recur_fibonacci(n - 1) + recur_fibonacci(n - 2)

# Example usage:
n = 10  # You can change this to the desired position in the Fibonacci series
result = recur_fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")


''' (3)Short a dict with dict comprehension? '''

# Original dictionary
original_dict = {'banana': 3, 'apple': 1, 'orange': 2}

# Sort by keys
sorted_dict_keys = {k: original_dict[k] for k in sorted(original_dict)}

# Sort by values
sorted_dict_values = {k: v for k, v in sorted(original_dict.items(), key=lambda item: item[1])}

# Print results
print("Original Dictionary:", original_dict)
print("Sorted by Keys:", sorted_dict_keys)
print("Sorted by Values:", sorted_dict_values)


''' (4)Short a list without using sort keyword'''

def Quicksort(arr):
    if len(arr)<=1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [ x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot ]
    return Quicksort(left) + middle + Quicksort(right)

my_list = [1,2,4,2,3,5,3,4,6,2,3]
sorted_list = Quicksort(my_list)

print(sorted_list)


''' (5)Find requried output'''
# Input = "The sky is blue"
# Output = "blue is sky the" 

s = "The sky is blue"
l = s.split()
print("first",l)
l = l[::-1]

print("second:",l)
l = ' '.join(l)
print(l)


'''(6)Manupulate on string and list'''

# Extract elements from a list based on index

my_list = [1, 2, 54, 22, 44, 5, 13, 23, 3]
result = [value for index, value in enumerate(my_list, start=1) if index % 3 == 0]
print("Every 3rd element in the list:", result) # Output [54,5,3] return all element at every index 3 difference

# Modify a string by excluding characters at specified indices
string_value = str(input("Enter your string: "))
index_value = int(input("Enter your index: "))
new_string = list(string_value)
modified_string = [value for index, value in enumerate(new_string, start=1) if index % index_value != 0]
print("Modified string:", ' '.join(modified_string)) # return element with remove provided index value

'''(7)Python Program to swap two numbers without using third variable'''

# Input values
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Swapping without using a variable
a = a + b
b = a - b
a = a - b

# Output the swapped values
print("After swapping:")
print("a =", a)
print("b =", b)


'''(8)Find prime numbers between 0 and 100'''

a = 100
for i in range(2, a):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)


# Another short way
for num in range(2, 101):
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
        print(num)


'''(9)Find the Smallest Positive Number in a List'''
# Given list
a = [2, 3, 4, 1, 32, 31]

# Initialize variable for the smallest positive number
small = None

# Iterate through the list to find the smallest positive number
for num in a:
    if num > 0:
        if small is None or num < small:
            small = num

# Output the smallest positive number
print("The smallest positive number in the list is:", small)


'''(10). Find the Factorial of a Number?'''
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}")

'''(11)Find the Most Frequent Character in a String?'''

string_value = "Dhruvish patel"
ch = {}
for i in string_value:
    if i in ch:
        ch[i] += 1
    else:
        ch[i] = 1

max_char = max(ch, key=ch.get)
print(max_char)

'''(12)Find Non-Repetitive Elements in a List Without Using Count'''

# Given list
my_list = [1, 2, 3, 4, 2, 3, 5, 6, 7, 7, 8]

def find_non_repetitive_elements(lst):
    element_count = {}

    # Count occurrences of each element in the list
    for element in lst:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1

    # Create a list of non-repetitive elements
    non_repetitive_elements = [element for element, count in element_count.items() if count == 1]

    return non_repetitive_elements

# Find and print non-repetitive elements
result = find_non_repetitive_elements(my_list)
print("Non-repetitive elements in the list:", result)

'''(13)Find Maximum and Minimum Values in a List?'''

my_list = [1,2,4,12,45,32,4,36,6]

maximum = my_list[0]
minimum = my_list[0]

for i in my_list:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print(f"Maximum: {maximum} Minimum:{minimum}")



'''List programs'''
#Modify List by Inserting Element at Specific Index

my_list = [1, 2, 3, 4, 5]

# Add an element at a specific index
my_list.insert(2, 10)

# Remove an element by value
my_list.remove(3)

# Remove an element by index
del my_list[0]

print("List after modifications:", my_list)


'''String programs'''

my_string = "hello"

# Add a character at the end of the string
my_string += '!'
 
# Add a character at a specific index
my_string = my_string[:2] + 'X' + my_string[2:]

# Remove the last character
my_string = my_string[:-1]

# Remove a character at a specific index
my_string = my_string[:1] + my_string[2:]

print("String after modifications:", my_string)

'''Dict programs'''

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Add a new key-value pair
my_dict['d'] = 4

# Remove a key-value pair by key
del my_dict['b']

print("Dictionary after modifications:", my_dict)


#Remove duplicate values in dictionary
test_dict = {'gfg': 10, 'is': 15,'best': 20, 'for': 10, 'geeks': 20}

def removeduplicatefromdict(dict):
    new_list = []
    new_dict = {}
    for key,value in dict.items():
        if value not in new_list:
            new_dict[key] = value
            new_list.append(value)

    return new_dict

print("Dictionary after remove duplicate value:",removeduplicatefromdict(test_dict))

my_list = [1, 2, 4, 3, 5, 6, 2, 9, 9, 4, 2, 5, 7, 8]

new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)


# Flatter list in list
my_list = [1,2,3,[4,5,6],[7,8,9]]
new_list = []

for i in my_list:
    if type(i) is list:
        for items in i:
            new_list.append(items)
    else:
        new_list.append(i)

print("Flatter list:",new_list)

# Flatter dictionary in single dictionary
def flatten_dict(d):
    flattened_dict = {}
    for key, value in d.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                flattened_dict[key + '_' + sub_key] = sub_value
        else:
            flattened_dict[key] = value
    return flattened_dict

# Your original nested dictionary
nested_dict = {
    "Name": "DHRUVISH",
    "AGE": 21,
    "CITY": {
        "AMD": "Ahmedabad",
        "VD": "Vadodara"
    }
}

# Flatten the dictionary
flattened_dict = flatten_dict(nested_dict)
print(flattened_dict)
