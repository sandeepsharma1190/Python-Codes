###### Array #########
# an array is a collection of same type of elements
# All values should be of same type
#Array dont have fix values
# Signed values can go from -ve to +ve
# unsigned values dont work on -v values
# we can add remove values here

import array as arr
#from array import *
vals = arr.array('i', [5,7,3,5])
print (vals.buffer_info())      
#buffer info gives size of an array
#output: - (1958923888816, 4), "1958923888816" is the address of array and 4 is the size

print (vals.typecode)     # will let us knoe the typecode, which is 'i' here
print (vals[0])     # Indexing
print (vals[1:3])      # Slicing
print (len(vals))
vals.append(9)
vals.insert(1,2)
vals.pop()
vals.remove(2)


# Concatenation    
a = arr.array('d',[1.2, 2.3])
b = arr.array('d',[1.2])
print (a+b)

for i in range(4):
    print (vals[i])
    '''or'''
for i in range(len(vals)):      # when we dont know length of values
    print (vals[i])
    '''or'''
for e in vals:          #for loop is quite dynamic, we can use it this way as well
    print(e)
    
'''For unicodes'''
import array as arr
vals2 = arr.array('u', ['a','e','i'])

for e in vals2:
    print(e)
    
# to copy
new_array = arr.array(vals.typecode, (a for a in vals)) #typecode - to copy type, a means values one by one
new_array = arr.array(vals.typecode, (a*a for a in vals)) #typecode - to copy type, a*a will give us square of values
new_array = arr.array(vals.typecode, (a**3 for a in vals)) #we can use power function as well

'''while loop'''
i = 1
while i < 4:
    print (new_array[i])
    i+=1
    
'''User input to make array'''
from array import *
arr1 = array('i',[])
n = int(input('Enter the length of array: '))
for i in range(n):
    x = int(input('Enter the next value: '))
    arr1.append(x)
print (arr1)

'''to search index number (first manually)'''
index_input = int(input('Enter the index number you want to check: '))
index_value = 0
for e in arr1:
    if e == index_input:
        print (index_value)
        break
    
    index_value+=1
    '''or (automatic)'''
print (arr1.index(index_input))

















