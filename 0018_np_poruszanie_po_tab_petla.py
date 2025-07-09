import numpy as np

b = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])

for row in b:
    print(row)

#pierwsze liczny z każdego wiersza które dają isza kolumnę
for row in b:
    print(row[0])
    
    
b = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])

for row in b:
    for number in row:
        print(number, end=' ')
#liczby wierszem
#1 2 3 4 5 6 7 8 9


for row in b:
    for number in row:
        print(number)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9







