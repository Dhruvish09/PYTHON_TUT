''' (1) Pythonic Element Exclusion: A Comparative Analysis of List Comprehension and Iterative Removal
    (2) Add Elements to a List at Specific Indices
    (3) Get sum of even and odd numbers in a list
    (4) Flatten a list of lists
'''

'''(1) Pythonic Element Exclusion: A Comparative Analysis of List Comprehension and Iterative Removal'''
my_list = [32, 4, 12, 5, 7, 6, 8, 9]
new_list = [4, 6]

# Using list comprehension for element exclusion
result = [value for value in my_list if value not in new_list]
print("Result using List Comprehension:", result)

# Remove elements from the list iteratively
for i in new_list:
    my_list.remove(i)  # Remove element
    # del my_list[i]  # Remove element by index

print("Result after Iterative Removal:", my_list)



'''(2) Add Elements to a List at Specific Indices'''
original_list = [10, 20, 30, 40, 50]

# Elements to be added
elements_to_add = [15, 25]

# Indices where elements will be added
indices_to_add = [2, 4]

# Add elements at specific indices
for index,element in zip(indices_to_add,elements_to_add):
    original_list.insert(index, element)

# Display the modified list
print("List after adding elements:", original_list)

'''(3) Get sum of even and odd numbers in a list'''

original_list = [10, 19, 30, 40, 53,60,70,80]

def odd_even_sum(original_list):
    even_num = 0
    odd_num = 0

    for i in original_list:
        if i % 2 == 0:
            even_num += i
        else:
            odd_num += i

    return f"Even Number sum is:{even_num}", f"Odd number sum is:{odd_num}"

even,odd = odd_even_sum(original_list)

print(even,odd)

'''(4) Flatten a list of lists'''
original_list = [10, 20,[ 30, 40,[50, 60, 70], 80], 50,60,[12,13,14,15],70,80]
new_list = []
for  i in original_list:
    if type(i) == list:
        for j in i:
            if type(j) == list:
                for k in j:
                    new_list.append(k)
            new_list.append(j)
    else:
        new_list.append(i)

print(new_list)

# Second Approch
def flatter_list(my_list):
    new_list = []
    for element in my_list:
        if isinstance(element,list):
            new_list.extend(flatter_list(element))
        else:
            new_list.append(element)

    return new_list

print(flatter_list(my_list))


'''(5)List Comprehension'''
my_list = [2, 3, 4, 5, 6, 7, 8, 9]
# (1)Power of 2 numbers
result = [x**2 for x in my_list]
print(f"Power of 2 numbers:{result}")

# (2)Even numbers
result = [x for x in my_list if x % 2 == 0]
print(f"Even numbers:{result}")

# (3)Odd numbers
result = [x for x in my_list if x % 2 != 0]
print(f"Odd numbers: {result}")

# (4)Numbers divisible by 3
result = [x for x in my_list if x % 3 == 0]
print(f"Numbers divisible by 3: {result}")

# (5)Flattering list
my_list = [[1, 2], [3, 4], [5, 6]]
result = [x for sublist in my_list for x in sublist]
print(f"Flattening list: {result}")

# (6)Get first letter from list of strings
my_list = ["apple", "banana", "cherry"]
result = [x[0] for x in my_list]
print(f"Your first latter of string is: {result}")


'''(6) Sort element in list using decorator'''
def sort_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list):
            return sorted(result)
        else:
            return result
    return wrapper

@sort_decorator
def get_numbers(my_list):
    return my_list

my_list = [3,2,4,6,3,56,7,8,5,3,3,5]
print(get_numbers(my_list))


'''(7) List element Rotation Program based on provide lenght of index'''
my_list = [1, 2, 3, 4, 5, 6]

def rotate_list(my_list, n):
    result = my_list[-n:] + my_list[:-n]

    return result

print(rotate_list(my_list, 2))  # Output: [5, 6, 1, 2, 3, 4]
print(rotate_list(my_list, 3))  # Output: [4, 5, 6, 1, 2, 3]