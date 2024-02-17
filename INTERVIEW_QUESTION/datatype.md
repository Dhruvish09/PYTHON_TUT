<!-- List practicals -->
(1)Swap Two Elements in a List Using enumerate

def swapvalue(list,pos1,pos2):
    for i,x in enumerate(list):
        if i == pos1:
            element1 = x
        if i == pos2:
            element2 = x
    list[pos1] = element2
    list[pos2] = element1

    return list

my_list = [61,24,12,16]
pos1,pos2=1,2

print(swapvalue(my_list,pos1-1,pos2-1))


(2)Remove duplicates from the list using list comprehension 

my_list = [2,3,36,6,3,6,8,9,8,5,9,6,9,3]

new_list = []

result = [new_list.append(x) for x in my_list if x not in new_list]

print(my_list)

(3)

