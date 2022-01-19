'''
*
**
***
****
*****
****
***
**
*
#----------------------------

for i in range(5):
    for j in range(i): # decides no of rows & iterate over a line j times
            print("*", end="")
    print()

for y in range(5):
     for x in range (5-y):
         print("*", end="")
     print()

#----------------------------------------------------
                                                                 
     *                    
    **                                           
   ***
  ****
 *****  --------->
  ****
   ***
    **
     *
''''
"""
program to print diamond
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     *
"""


     
                                                                
for i in range(5):
    print(" " *(6-(i)), end='')
    for j in range(i):           
        print("* ", end='')
    print()
for y in range(5):
     print(" " *(y+1), end='')
     for x in range (5-y):
         print("* ", end='')
     print()
