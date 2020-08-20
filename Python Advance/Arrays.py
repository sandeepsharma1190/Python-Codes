import array as arr
a = arr.array('d',[2.5,3.5,4.5])
print (a[-1])

import numpy as np
x = np.arange(10)
print(x[5::-2])

x = (0,8,9,15,17,18)
y=slice(1,-2)
print(x[y])

tuple1 = (2,4,6,3,7)
tuple2 = (1,2,3)

N = np.array([1,2,3])


s = {12,13,14,15}
s.intersection_update({17,13,14,16})
print(s)

d = {"plum ":0.66, "pears ":1.25,"oranges ":0.50, 'apple':0.75 }

c = {}
c[1]=1
c['1']=2
c[1]+=1
print(c)

n = [x*x for x in range(4)]
print(n)

list = [2, 4, 6, 8]
a = (x**3 for x in list)
print(next(a))

#np.ones((3,3),True)
np.zeros((3,3),False)
np.arange((3,3),False)
np.full((3,3),True)