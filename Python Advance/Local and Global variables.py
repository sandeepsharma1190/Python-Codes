def sandy():
    number = 11
    print(number)
sandy()
print (number)    
# print (number) wont work alone, as it is local and functionable in function only

# We always give Prefrence to local variable
a = 10
def something():
    a = 15
    print('Inside func', a)
something()
print ('Outside func', a)
#===========
# global a changed values from 10 to 15
a = 10
def something():
    global a
    a = 15
    print('Inside func', a)
something()
print ('Outside func', a)
#=============
    
def sandy2():
    global number
    number = 190
    name = 'Sandeep' 
    print(number, name)
    
sandy2()
print(number)
# after this number 11 is global, if you will print (number) only outside function, it will work.
number = 40
print (number)
sandy2()
print(number)

# Local n global variable together
#a = 10
#print (id(a))
#def something():
#    a = 15
#    print('Inside func', a)
#something()
#print ('Outside func', a)










