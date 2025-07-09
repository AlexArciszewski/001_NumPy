import numpy as np

nice_tab = np.array([[1,2,3],[4,5,6],[7,8,9]])

#zapis list comprehension
some_list = [number for row in nice_tab for number in row if number > 5]
print(some_list)
#[6, 7, 8, 9]