######## Classes and Objects ########
'''Class is a design of object. Like to create a building we need a blueprint, here blueprint is class and building is an object

How we create a class : - Class computer (Same as defining a function)
we put 2 parts, attributes (variables) and behaviour (methods(function))

self: - it is the object we are passing'''

#### you can not access functions outside of a class
##### to access from outside, use self as parameter in function

class Classname:
    string = 'This is a class'
    def func(self):
        print ('I am in this class')
#### creating object for a class        
obj1 = Classname()
obj1.string
obj1.func() ### for its output decalre self as parameter in a function of a class


##### to update class attributes########
obj2 = Classname()
obj2.string = 'This is the second line'
print (obj1.string,'\n',obj2.string)

#############
class Computer:
    def config (self):
        print ('i5, 8GB')
        
comp1 = Computer()
comp2 = Computer()

Computer.config(comp1)
Computer.config(comp2)