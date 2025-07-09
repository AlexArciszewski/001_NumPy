import numpy as np


nicer_tab = np.array([[1,2,3],[4,5,6],[7,8,9]])

score = np.where(nicer_tab > 5, nicer_tab, None)
#                (warunek do spelnienia, co ma zwrócic jesli spelniony tu el tab nicer_tab, co ma zwrócić jesiw arunek nie jest spełniony) 
print(score)

#[[None None None]
#[None None 6]
#[7 8 9]]

#parzyste liczby a jesli jest nieparzysta to 0
next_score =np.where( nicer_tab % 2 == 0, nicer_tab, 0)
print(next_score)

# [[0 2 0]
#  [4 0 6]
#  [0 8 0]]