
List1 = [1, 2, 3] 
List2 = [2, 3, 4, 5] 
  
# Add List2 to List1 
List1.extend(List2)         
print(List1) 
  
# Add List1 to List2 now 
List2.extend(List1)  
print(List2) 
