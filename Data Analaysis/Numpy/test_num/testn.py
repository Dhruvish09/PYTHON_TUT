# np.array
# np.arrange
# np.zeros
# np.ones
# np.linspace
# np.random.rand
# np.random.randn
# np.random.randint
# .shape
# .reshape
# .max
# .min
# .argmax
# .argmin

import numpy as np

print("(1)list of array:")
my_list=[1,2,3,4]
print(np.array(my_list))
print("--------------")

print("(2)Matrix:")
mat=[[1,2,3],[4,5,6],[7,8,9]]
print(np.array(mat))
print("--------------")

print("(3)array with built  in function:")
print(np.arange(0,11,2))
print(np.zeros(3))
print(np.ones(3))
print("--------------")

print("(4)devide perticular space:")
print(np.linspace(0,10,5))
print("--------------")

print("(5)print in number range:")
ar=np.arange(5,20)
print(ar)
print(ar[4])
print(ar[0:4])
print(ar[4:])
print(ar[:4])

print("--------------")

print("slicing of array:")
ar=np.arange(5,20)
slice_ar=ar[0:5]
print(slice_ar)
slice_ar[:]=99
print(slice_ar)
print("--------------")

print("indexing 2d array:")
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print(arr[0][0])
print(arr[1][0])
print(arr[1,1])
print(arr[2,1])
print(arr[0:2,0:2])
print(ar[ar<10])
print("----------------")

print("(6)identity matrix:")
print(np.eye(4))
print("--------------")

print("(7)Random number:")
print(np.random.rand(3))
print("--------------")

print("(8)random matrix:")
print(np.random.rand(3,3))
print("--------------")

print("(9)random one dimetional array:")
print(np.random.randn(3))
print("--------------")

print("(10)random two dimetional array:")
print(np.random.randn(3,3))
print("--------------")

print("(12)get random integer:")
print(np.random.randint(0,10))
print("--------------")

print("(13)get random  perticular range integer:")
print(np.random.randint(1,100,11))
print("--------------")

print("print shape and reshape:")
ar=np.arange(25)
print(ar)
print(ar.shape)
print(ar.reshape(5,5))
print(ar.reshape(5,6))#get error here bcs size define 25
print("--------------")