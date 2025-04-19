import numpy as np
#create the array
m1 = np.array([[2,3],[4,5]])
#print(m1)
# print(m1[1,1])
# print(m1[1][1])
# print(m1[1])
# print(m1[:,0])

print(np.shape(m1))
print(np.size(m1))
print(np.ndim(m1))

#shape, size, dimension
#shape: num of rows and num of coln
#size: num of elements
# print(m1[[0,1],[1,0]])


# mat1= np.array([[1, 2, 3], 
#                [4, 5, 6], 
#                [7, 8, 9]])
# mat2 = np.array([[3,5,7],
# [8,9,10],
# [2,4,7]])
# mat_add = mat2 + mat1
# result = (np.dot(mat1,mat2))
# print(mat_add)
# print(result)

m2 = np.array([[1,3],[1,5]])
result = (np.dot(m1,m2))
# print(result)

mat_inv = np.linalg.inv(m2)
print(mat_inv)
result1 = np.dot(m1,mat_inv)
print(result1)


