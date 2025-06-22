lst = [3, 1, 2]

lst.append(4)       # [3, 1, 2, 4]
lst.extend([5, 6])  # [3, 1, 2, 4, 5, 6]
lst.insert(1, 10)   # [3, 10, 1, 2, 4, 5, 6]
lst.remove(10)      # [3, 1, 2, 4, 5, 6]
last = lst.pop()    # Removes 6
i = lst.index(4)    # 3
c = lst.count(2)    # 1
lst.sort()          # [1, 2, 3, 4, 5]
lst.reverse()       # [5, 4, 3, 2, 1]
copy_lst = lst.copy()
lst.clear()         # []


# append,extend,
# count,index,len
# del,remove,insert
# min,max,sum

##[append()]
# Adds List Element as value of List. 
List = ['Mathematics', 'chemistry', 1997, 2000] 
List.append(20544) 
print(List) 

##[count()]
#Calculates total occurrence of given element of List.
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
print(List.count(1)) 

##[del]
#Element to be deleted is mentioned using list name and index.
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
del List[0] 
print(List) 

##[extend()]
List1 = [1, 2, 3] 
List2 = [2, 3, 4, 5] 
  
# Add List2 to List1 
List1.extend(List2)         
print(List1) 
  
# Add List1 to List2 now 
List2.extend(List1)  
print(List2) 

##[index()]
#Returns the index of first occurrence. Start and End index are not necessary parameters.


List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
print(List.index(2)) 

##[insert()]
#Inserts an elements at specified position
print('1:-insert()')
List = ['Mathematics', 'chemistry', 1997, 2000] 
# Insert at index 2 value 10087 
List.insert(2,10087)      
print(List) 

##[len()]
#Calculates total length of List
print('2:-len()')
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
print(len(List)) 

##[max()]
#Calculates maximum of all the elements of List.
print('3:-max()')
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
print(max(List)) 

##[min()]
#Calculates minimum of all the elements of List.
print('4:-min()')
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
print(min(List))

##[pop()]
# Index is not a necessary parameter, if not mentioned takes the last index.
print('5:-pop()')
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
print(List.pop()) 
 
 ##[remove()]
 #Element to be deleted is mentioned using list name and element.
print('6:-remove()')
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
List.remove(3) 
print(List) 

##[reverse]
#Sort the given data structure (both tuple and list) in ascending order. Key and reverse_flag are not necessary parameter and reverse_flag is set to False, if nothing is passed through sorted().
List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
  
#Reverse flag is set True 
List.sort(reverse=True)  
  
#List.sort()., reverses the sorted list   
print(List)      

##[sum]
#Calculates sum of all the elements of List.
print('7:-sum()')
List = [1, 2, 3, 4, 5] 
print(sum(List)) 



        


