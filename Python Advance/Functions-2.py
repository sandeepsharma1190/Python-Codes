# Functions-2

def test1(a,b):
    return (a+b)

test1(4,5)
test1('test', '1')
test1([3,3], [4,5])
#####=========================================================

def test2(a,b):
    return a+b, a*b

test2(3,4)

# to store value for both addition and multiplication
a,b = test2(3,4)
print (a)
print (b)

# To store only one value, we use "_", it wont show in variable explorer
# but if we will call "_", it will give us some value
# "_" name here is placeholder
c,_ = test2(3,4)
print (c)
print (_)

# Local and global variable
a = 3
def test3():
    b = 4
    return a+b

test3()
print (b)   # b wont come as b is local

def test3():
    global b
    b = 4
    return a+b
print (b)   # now here b is a global variable


# When we have multiple values in return and need only one
def test4():
    return 'Python', [4,5,3], {1:'one', 'two':2}

test4()     # all values will be in tuple

# when just need dictionary
_,_,d = test4()
print (d)

# when just need list
_,l,_ = test4()
print (l)

# how to check number is prime or not
# Break is needed, else, it will run a loop
def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            print ('Number is not a prime number')
            break
    else:
        print ('Number is prime')

is_prime(111111111)

# how to check number is prime or not -- in boolean
def is_prime1(n):
    for i in range(2,n):
        if n%i == 0:
            return False
            break
    else:
        return True

is_prime1(11)


def reverse_for_loop(s):
    s1 = ''
    for c in s:
        s1 = c + s1  # appending chars in reverse order
    return s1
reverse_for_loop('text')



def test1(n):
    for i in range(n):
        print (i)
test1(4)

def cube1(n):
    for i in range(n):
        print(i**3)
cube1(3)

# yield - basically a generator (which can generate values (e.g., range function))
# it will store dataset and can be used as an iterator (like range)
def cube(n):
    for i in range(n):
        yield i**3
cube(3)     # it wont show result

# how we can use yield product
for i in cube(3):
    print (i)

next(cube(3))   # wont give any result as cube is not an iterator here

# below code can be used instead
v = iter(cube(3))
next(v)

# Fibonacci series
def fibna(n):
    a = 1
    b = 1
    for i in range (n):
        print (a)
        a,b = b, a+b

fibna(10)

# converting to iterator
def fibna(n):
    a = 1
    b = 1
    for i in range (n):
        yield a
        a,b = b, a+b

for i in fibna(30):
    print (i)


# for doubling values, starts from 1, than 2, than 2+2, than 4+4.... so on
def dose(n):
    a = 1
    b = 2
    for i in range (n):
        print (a)
        a = a*b

def dose(n):
    a = 1
    b = 2
    for i in range (n):
        yield a
        a = a*b

# how to add square of value in a different list
def sq(n):
    return n**2

l3 = [2,3,4,5,6]
new_list = []

for i in l3:
    new_list.append(sq(i))
    
print (new_list)

# MAP function
# it will take function and list as an input
list(map(sq, l3))

for i in map(sq, l3):
    print (i)




























