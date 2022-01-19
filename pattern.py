# wap to print:
"""
# 1
# 3 2
# 6 5 4
# 10 9 8 7

x = 1
for i in range(1, 5):
    y = x
    for j in range(i):
        print(y, end=" ")
        y -= 1
    x = x + i + 1
    print()

----------------------------------------------------------------------------------------
# WAP to print
'''
*****
****
***
**
*
'''
x = 5
for i in range(1, 6):
    print(x * '*')
    x -= 1
------------------------------------------------

n = int(input('Enter no of rows you want: '))
for i in range(n):
    print((n-i) * '*')

for i in range(1, n+1):
    print(i * '*')
--------------------------------------------------
# WAP to print
'''
     *****
      ****
       ***
        **
         *
'''
n = int(input('Enter number of rows you want'))
space = ' '
for i in range(n):
    print(space*(n+i), (n-i) * '*')
----------------------------------------------------------

# WAP to print:
'''
    
            *
           **
          ***
         ****
        *****    
'''
n = int(input('Enter number of rows you want'))
space = ' '

for i in range(1, n+1):
    print((space*(n*2 - i)), i * '*')
--------------------------------------------------------------------

# WAP to print:
'''
        *****
         ****
          ***
           **
            *
            *
           **
          ***
         ****
        *****    
'''

n = int(input('Enter number of rows you want'))
space = ' '
for i in range(n):
    print(space*(n+i), (n-i) * '*')

for i in range(1, n+1):
    print((space*(n*2 - i)), i * '*')

"""
# WAP to print
''''
*******************
********* *********
********   ********
*******     *******
******       ******
*****         *****
****           ****
***             ***
**               **
*                 *
**               **
***             ***
****           ****
*****         *****
******       ******
*******     *******
********   ********
********* *********
*******************

'''
n = int(input('Enter number of rows you want: '))
space = " "
y = 1
for i in range(0, n):
    print(((n - i) - y) * '*', space*((i*2)-1), (n - i) * '*', sep='')
    y = 0
for i in range(2, n+1):
    if i == n:
        print((i-1) * '*', (space * ((n * 2) - (2 * i))), i*'*', sep='')
    else:
        print(i * '*', (space * ((n * 2) - ((2 * i) + 1))), i * '*', sep='')
