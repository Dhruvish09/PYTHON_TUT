# def advanced_list_slicing(my_list):
#     # Extracting elements from index 2 to the end
#     part1 = my_list[2:]

#     # Extracting elements from the beginning to index 5 (exclusive)
#     part2 = my_list[:5]

#     # Creating a new list with every third element
#     every_third = my_list[::3]

#     # Reversing every second element in a sublist
#     reversed_sublist = my_list[1:8][::-1]

#     # Displaying results
#     print("Original List:", my_list)
#     print("Part [2:]:", part1)
#     print("Part [:5]:", part2)
#     print("Every Third Element [::3]:", every_third)
#     print("Reversed Every Second Element [1:8][::-1]:", reversed_sublist)

# # Example Usage:
# characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# advanced_list_slicing(characters)



# new_liss = [1,3,5,33,15]
# nw = [34,23,65,73]

# nw.extend(new_liss)
# print(new_liss)

# # Original List
# list1 = [1, 2, 3]

# # List to be added
# list2 = [4, 5, 6]

# # Extending list1 with elements from list2
# list1.extend(list2)

# # Displaying the updated list
# print("Extended List:", list1)


# def greet(name):
#     """
#     This function takes a name as input and returns a greeting message.
    
#     Parameters:
#     name (str): The name of the person to greet.
    
#     Returns:
#     str: A greeting message including the provided name.
#     """
#     return f"Hello, {name}!"

# # Accessing the docstring
# print(greet.__doc__)


# [lst.append(value) for value in a if value not in lst]

# Using the custom behavior defined by __len__
# even_count = len(my_list)
# print(f"Number of even elements in my_list: {even_count}")

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()




# import time
# import requests
# from multiprocessing import Pool

# # Function to download a file given its URL
# def download_file(url):
#     filename = url.split("/")[-1]
#     print(f"Downloading {filename}")
#     response = requests.get(url)
    
#     with open(filename, 'wb') as file:
#         file.write(response.content)
    
#     print(f"{filename} downloaded")

# # Function to demonstrate multiprocessing for file downloads
# def download_files_demo():
#     # List of file URLs to download
#     file_urls = [
#         "https://www.example.com/file1.txt",
#         "https://www.example.com/file2.txt",
#         "https://www.example.com/file3.txt"
#     ]

#     # Using a Pool of processes to download files in parallel
#     with Pool() as pool:
#         pool.map(download_file, file_urls)

# if __name__ == "__main__":
#     download_files_demo()
# my_list = [1,2,3,4,5]

# result = list(map(lambda x: x**3,my_list))
# print(result)


#     (1)Number or string is Palindrome or not?
# (2)Generate an Infinite Fibonacci Series using Generator
# (3)Generate an Infinite Fibonacci Series using Recursion
# (4)Short a Dictionary with Dictionary Comprehension
# (5)Short a List without Using the Sort Keyword
# (6)Manipulate on String and List
# (7)Python Program to Swap Two Numbers without Using a Third Variable
# (8)Find Prime Numbers Between 0 and 100
# (9)Find the Smallest Positive Number in a List
# (10)Find the Factorial of a Number?
# (11)Find the Most Frequent Character in a String?
# (12)Find Non-Repetitive Elements in a List Without Using Count?
# (13)Find Maximum and Minimum Values in a List?


def is_palindrome(num):
    name = str(num)
    length = len(name)

    for  i in range(length):
        if name[i] != name[length-i-1]:
            return False
    return True

print(is_palindrome(121))