import numpy as np

# 1D Array
arr1 = np.array([50,30,80,70])
# print(arr1)

arr1 = np.array([[10,20,30],[40,50,60],[88,77,99]])
arr2 = np.array([[10,60,30],[40,44,60],[88,22,99]])
# # print(arr1)

# print(arr1[arr1>40])
# print(arr1[:,1])
# print(arr1+arr2)
# index
# print(arr1[0:2])
# print(arr1[:2])

# z = np.eye(4)
# print(z)

# rangearr = np.arange(0,12,2)
# print(rangearr)


# linespace = np.linspace(0,1,5)
# print(linespace)


newarr = arr1+arr2
# print(newarr.T)

flat = newarr.flatten()
# print(flat)


print(np.sum(flat))
print(np.mean(flat))
print(np.max(flat))
print(np.std(flat))

# reshape = flat.reshape(3,3)
# print(reshape)