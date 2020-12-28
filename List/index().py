#Returns the index of first occurrence. Start and End index are not necessary parameters.


List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
print(List.index(2)) 


List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 

"""index(element, start, end) : It will calculate till index end-1. """

# will check from index 2 to 4. 
print("After checking in index range 2 to 4") 
print(List.index(2,2,5)) 

# will check from index 2 to 3. 
print("After checking in index range 2 to 3") 
print(List.index(2,2,4)) 
	
