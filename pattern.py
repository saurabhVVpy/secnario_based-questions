#1
'''
for i in range(5):
    for j in range(i+1):
        print("* ",end="")
    print()
'''
'''
for i in range(1,6):
    for j in range(i):
        print("* ",end="")
    print()
'''

#without nested for loop
'''
for i in range(1,6):
    print(i*"* ")
'''


#output
'''

*                    
* * 
* * * 
* * * * 
* * * * *     

'''


#2 
'''
for i in range(5):
    for j in range(i,5):
        print("* ",end="")
    print()
'''
'''
for i in range(1,6):
    for j in range(6,i,-1):
        print("* ",end="")
    print()
'''

#without nested loop
'''
for i in range(5,0,-1):
    print(i*'* ')
'''
'''
* * * * * 
* * * * 
* * *
* *
*

'''


#3
'''
for i in range(1,6):
    for j in range(i,5):
        print("  ",end='')
    print(i*'* ',end='')
    print()
'''

'''
for i in range(1,6):
    for j in range(i,5):
        print("  ",end='')
    for j in range(i):    
        print('* ',end='')
    print()
'''
#output
'''    

        * 
      * * 
    * * *
  * * * *
* * * * *

'''

#4
'''
for i in range(5):
    for j in range(i,5):
        print("* ",end='')
    print()
'''
'''
for i in range(5):
    for j in range(5,i,-1):
        print('* ',end='')
    print()
'''
#output
'''    

* * * * *  
* * * *  
* * *
* *
*

'''


#5
'''
for i in range(1,6):
    for j in range(i,6):
        print(' ',end='')
    print(i*'* ',end='')
    print()
'''
'''
for i in range(5):
    for j in range(i+1,5):
        print(' ',end='')
    for j in range(i+1):
        print('* ',end='')
    print()
'''
#output
'''
 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''


#6
'''
for i in range(5,0,-1):
    for j in range(i,5):
        print(' ',end='')
    print(i*'* ',end='')
    print()
'''
'''
for i in range(5,0,-1):
    for j in range(i,5):
        print(' ',end='')
    for j in range(i):
        print('* ',end='')
    print()
'''

'''
for i in range(5):
    for j in range(i):
        print(' ',end='')
    for j in range(5,i,-1):
        print('* ',end='')
    print()
'''

'''
* * * * * 
 * * * *
  * * *
   * *
    *
'''




#7
'''
for i in range(1,10):
    if i<=5:
        for j in range(i,5):
            print(' ',end='')
        print(i*'* ',end='')
        print()
    else:
        for j in range(5,i):
            print(' ',end='')
        print((10-i)*'* ',end='')
        print()
'''

'''
for i in range(1,10):
    if i<=5:
        for j in range(i,5):
            print(' ',end='')
        for j in range(i):
            print('* ',end='')
        print()
    else:
        for j in range(5,i):
            print(' ',end='')
        for j in range(10-i):
            print('* ',end='')
        print()
'''

'''
for i in range(1,10):
    if i<=5:
        print((5-i)*' ',i*'* ')
       
    if i>5:
        print((i-5)*' ',(10-i)*'* ')
'''


#output
'''
     * 
    * * 
   * * *
  * * * *
 * * * * *
  * * * *
   * * *
    * *
     *

'''

#8

'''
for i in range(1,10):
    if i<=5:
        print(i*'* ')
    if i>5:
        print((10-i)*'* ')
'''
#output
'''


* 
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

'''
'''
for i in range(10):
    if i<5:
        print((5-(i+1))*'  ',(i+1)*'* ')
    if i>5:
        print((i-5)*'  ',(10-i)*'* ')
'''
#
'''
         * 
       * * 
     * * *
   * * * *
 * * * * *
   * * * *
     * * *
       * *
         *
'''


#9
'''
for i in range(1,10):
    if i<=5:
        print(i*'* ',(10-(i*2))*'  ',i*'* ')
    else:
        print((10-i)*'* ',(i-(10-i))*'  ',(10-i)*'* ')

'''

# for i in range(10):
#     if i<5:
#         print((i+1)*'* ',(10-((i+1)*2))*'  ',(i+1)*'* ')
#     else:
#         print((10-(i+1))*'* ',((i+1)-(10-(i+1)))*'  ',(10-(i+1))*'* ')


#output

'''
*                   *
* *               * *
* * *           * * *
* * * *       * * * *
* * * * *   * * * * *
* * * *       * * * *
* * *           * * *
* *               * *
*                   *

'''


#10
'''
for i in range(1,6):
    for j in range(i,6):
        print(' ',end='')
    for j in range(i):
        print('* ',end='')
    for j in range(i,5):
        print('  ',end='')
    for j in range(i):
        print('* ',end='')
    print()
#output
'''

'''
     *         * 
    * *       * * 
   * * *     * * *
  * * * *   * * * *
 * * * * * * * * * *
'''
'''
for i in range(5,0,-1):
    print((i-1)*' ',(5-(i-1))*'* ',(i-1)*'  ',(5-(i-1))*'* ')
'''   
#output

'''
     *           * 
    * *         * *
   * * *       * * *
  * * * *     * * * *
 * * * * *   * * * * *

'''




#11
'''
for i in range(1,11):
    if i<=5:
        for j in range(1,i):
            print(' ',end='')
        print((5-(i-1))*'* ',end='')
        print()
    else:
        for j in range(i,10):
            print(' ',end='')
        print((i-5)*'* ',end='')
        print()
'''
#output
'''
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 

'''



#12
'''
for i in range(5,0,-1):
    print((i-1)*' ',(5-(i-1))*'* ',(i-1)*'  ',(5-(i-1))*'* ')
    print()
'''
'''
for i in range(1,6):
    for j in range(i,6):
        print(' ',end='')
    for j in range(i):
        print('* ',end='')
    for j in range(i,5):
        print('  ',end='')
    for j in range(i):
        print('* ',end='')
    print()
#output
'''

'''
     *         * 
    * *       * * 
   * * *     * * *
  * * * *   * * * *
 * * * * * * * * * *
'''

# for i in range(1,11):
#     if i<=5:
#         for j in range(1,6):
#             if i+j<6:
#                 print(" ",end="")
#             else:
#                 print("* ",end="")
#     else:
#         for j in range(6,10):
#             if j-i<0:
#                 print(" ",end="")

#             else:
#                 print(" *",end="")
#     print()

#output
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * *
  * * *
   * *
    *
'''

# for i in range(1,5):
#         if i==1 or i==4: print(4*'* ')
#         else:print('* '+2*'  '+ '*')

#output
'''
* * * * 
*     *
*     *
* * * * 
'''

length=4
breadth=8

for i in range(length):
    if i==0 or i==length-1:
        print('*'*breadth)
    else:
        print('*'+' '*(breadth-2)+'*')

#output
'''
********
*      *
*      *
********
'''

length=4
breadth=8

for i in range(breadth):
    if i==0 or i==breadth-1:
        print('*'*length)
    else:
        print('*'+' '*(length-2)+'*')

#output
'''
****
*  *
*  *
*  *
*  *
*  *
*  *
****
'''

# char_=65
# for i in range(1,6):
#     print(i*chr(char_))
#     char_=char_+1

#output
'''
A
BB
CCC
DDDD
EEEEE
'''

# char_=65
# for i in range(1,6):
#     for j in range(i):
#         print(chr(char_),end='')
#         char_=char_+1
#     char_=65    
#     print()

#output
'''
A
AB
ABC
ABCD
ABCDE
'''
