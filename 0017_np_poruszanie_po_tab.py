import numpy as np

a = np.array([1, 2, 3])

#erowy element
print(a[0])
#1

print(a[:1])
# [1] el od 0 do 1 bez 1


print(a[1:])

# [2, 3]

c = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])

print(c[1])
#[4 5 6]

print(c[1][0])
#4

print(c[:2])
#[[1,2,3]
#[4,5,6]]


print(c[:2][:1])
#[1 2 3]

#tożsame z 
d = c[:2]
print(d[:1]) 
#[[1 2 3]]