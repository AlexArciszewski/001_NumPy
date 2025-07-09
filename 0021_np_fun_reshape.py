import numpy as np



nice_tab = np.arange(1,21,2)
print(nice_tab)
# [ 1  3  5  7  9 11 13 15 17 19]

reshaped_tab = nice_tab.reshape(2,5)

print(reshaped_tab)
# [[ 1  3  5  7  9]
#  [11 13 15 17 19]]

second_nice_tab = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(second_nice_tab)

# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

reshaped_second_nice_tab = second_nice_tab.reshape(1,9)
print(reshaped_second_nice_tab)

# [[1 2 3 4 5 6 7 8 9]]




