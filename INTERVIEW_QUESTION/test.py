original_list = [10, 20, [30, 40, [50, 60, 70], 80], 50, 60, [12, 13, 14, 15], 70, 80]
new_list = []
for  i in original_list:
    if type(i) == list:
        for j in i:
            if type(j) == list:
                for k in j:
                    new_list.append(k)
            else:
                new_list.append(j)
    else:
        new_list.append(i)

print(new_list)