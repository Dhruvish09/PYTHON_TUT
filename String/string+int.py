age="20"
txt="my name is dp,and my age is{}"
print(txt.format(age))

#Another one example is
quantity = 3
itemno = 567
price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
myorder = f"I want {quantity} pieces of item {itemno} for {price} dollars."
print(myorder)
# print(myorder.format(quantity, itemno, price)) 
