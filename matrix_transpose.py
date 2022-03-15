'''
x = [[2, 3, 4], [4, 5, 6], [7, 8, 9]]
t = []
for i in range(0, len(x[0])):  # no of rows of new matrix
    y = []
    for j in range(0, len(x)):  # no of cols of new mat
        y.append(x[j][i])    # j indicates row and i indicates col of old matrix
    t.append(y)
print(t)

#-----------------------------------------------

import numpy as np
narr = np.array([[2, 3, 4],[4, 5, 6],[7, 8, 9]])
print(narr)
for i in range(len(narr)):
    for j in range(len(narr)):
        print(narr[j][i],end='')
    print()
'''
# x = [[2, 3, 4], [4, 5, 6], [7, 8, 9]]
import numpy as np
x = np.array([[2, 3, 4],[4, 5, 6],[7, 8, 9]])
#x= narr.tolist()

print([[x[j][i]  for j in range(len(x))] for i in range(len(x))])
