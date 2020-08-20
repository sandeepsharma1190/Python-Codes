#######Overloading and overriding#######
##-- Overloading can be done in a same class but overriding can not

#### Over loading - Same function with different parameters
'''Overloading'''
def add (a,b):
    return a+b
def add (a,b,c):
    return a+b+c
add (2,3,4)

'''add (a,b) wont work, because next add function has updated systems memory for add (a,b,c)'''
def add(instance, *args):
    if (instance == 'int'):
        result = 0
    if (instance == 'str'):
        result = ''
    if (instance == 'float'):
        result = 0.0
    for i in args:
        result += i
    return result
add ('str', 'a','b')
add ('float', 1,3,4)
add ('int', 1,3,4)


#### Over riding
'''subclass may change the functionality of a python method in the superclass. means 
Child class can change functionality of a parent class'''

class A:
    def checkit(self):
        print ('I am under class A')
class B:
    def checkit(self):
        print ('I am under class B')
        
obj1 = B()
obj2 = A()

obj1.checkit()
obj2.checkit()