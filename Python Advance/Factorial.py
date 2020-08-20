# Factorial

def fac (n):
    f = 1
    for i in range (1,n+1):
        f = f*i
    return f
x = 5
result = fac (x)
print (result)

##### or
def fac (n):
    f = 1
    for i in range (1,n+1):
        f = f*i
    return f
x = int(input('Enter a number: '))
result = fac (x)
print (result)

##### factorial using while loop
a = 1
b = 1
while b <= 10:
    a*=b
    b+=1
print (a)

##### factorial using for loop
a = 1
for fac in range (1,10):
    a*= fac
print (a)


#

