#The copy() method returns a copy of the specified dictionary.
print("1:")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()

print(x) 

##
#The fromkeys() method returns a dictionary with the specified keys and the specified value.
print("2:")
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

##
#The get() method returns the value of the item with the specified key.
print("3:")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x) 

##
#The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
print("4:")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x) 

##
#The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
print("5:")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

print(x) 

##
#The pop() method removes the specified item from the dictionary.
print("6:")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")

print(car) 

##
#The popitem() method removes the item that was last inserted into the dictionary. 
print("7:")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()

print(car)

##
#The setdefault() method returns the value of the item with the specified key.
print("8:")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)

##
#The update() method inserts the specified items to the dictionary.
print("9:")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)

##
#The values() method returns a view object. The view object contains the values of the dictionary, as a list.
print("10:")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print(x)
