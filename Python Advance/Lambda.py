####### Lambda ########
# its an anonyms function, we dont name it
# we can use it only once
def sqr(a):
    return a*a
result = sqr(5)
print (result)
# or lambda way
f = lambda a : a*a  # we have to assign it to any variable
result = f(5)
print (result)

####
add1 = lambda x:x+5
print (add1(7))

#########
full_name = lambda fn, ln: fn.strip().title() + ' ' + ln.strip().title()
full_name (' Sandeep', 'sharma')

#we can pass n no. of arguments but expression should be one, which is + here
f = lambda a,b : a+b
result = f(5, 6)
print (result)

x = lambda a:a+10
print(x(5))

###### Function VS Lambda ############
def myfunc (x, y):
    print (x*y)

'''Lambda'''
z = lambda x, y:x*y
print (z(2, 3))

# =================Filter, Map and Reduce
# filter #
def iseven(n):
    return n%2 == 0
nums = [4,7,5,1,3,5,4,3,7]
evens = list(filter(iseven, nums))
print (evens)

# or Lambda way
nums = [4,7,5,1,3,5,4,3,7]
evens = list(filter(lambda n:n%2==0, nums))
print (evens)

# Map #
# we change values (we all doubling the values)
nums = [4,7,5,1,3,5,4,3,7]
evens = list(filter(lambda n:n%2==0, nums))
doubles = list(map(lambda n:n*2, evens))
print (evens)

# Reduce # We need to import it first
# we can pull only one value, like we are adding all values here
from functools import reduce

def addall (a,b):
    return a+b
nums = [4,7,5,1,3,5,4,3,7]
evens = list(filter(lambda n:n%2==0, nums))
doubles = list(map(lambda n:n*2, evens))
sum1 = reduce(addall, doubles)
print (sum1)

# or Lambda way

nums = [4,7,5,1,3,5,4,3,7]
evens = list(filter(lambda n:n%2==0, nums))
doubles = list(map(lambda n:n*2, evens))
sum1 = reduce(lambda a,b : a+b, doubles)
print (sum1)

# names
name = ['Sandeep Sharma', 'Jaspreet S dhaliwal', 'Mr. Rahul rajan']
name.sort(key = lambda name:name.split(' ')[-1].lower())
print(name)

# lambda under function
def myfunc(n):
    return lambda a:a*n

doubledigit = myfunc(2)
print (doubledigit(10))
