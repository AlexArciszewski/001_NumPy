import numpy as np

b = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])


for row in b:
    for number in row:
        if number >4:
            print(number, end=" ")
#5 6 7 8 9 


c = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])

sum = 0
for row in c:
    for num in row:
        sum += num
print(sum)
