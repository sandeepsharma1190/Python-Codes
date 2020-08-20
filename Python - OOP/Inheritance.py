######### Inheritance ######

#####Single inheritance######
###### to inherit from only 1 class####
class fruits:
    def __init__(self):
        print ('I am a Fruit!!')

class citrus(fruits):
    def __init__(self):
        super().__init__()
        print ('I am citrus and a part of fruit class!')
        
obj1 = citrus()


##### Multiple inheritance######
###### to inherit from more than 1 class####
class A:
    pass
class B:
    pass
class C(A,B):
    pass
issubclass (C,A) and issubclass (C,B)
'''Output --> True'''

##### Multilevel inheritance######
###### One class from another and another from another ####
####### Grandparents to parents, from parents to you ######
class A:
    x = 10
class B(A):
    pass
class C(B):
    pass

obj1 = C()
obj1.x
'''Output --> 10'''

##### Hierarchical inheritance######
###### More than one class inherits from a Class ####
####### Your parents have 3 children ######

class A:
    x = 10
class B(A):
    pass
class C(A):
    pass
obj1 = C()
obj1.x
issubclass (B,A) and issubclass (C,A)
'''Output --> 10'''
'''Output --> True'''

##### Hybrid inheritance######
###### Combination of any two kinds of inheritance (Hierarchical inheritance and Multiple inheritance)####
####### Class E inherits from Class B n D and both B n D inherits from class A######
class A:
    x = 10
class B(A):
    pass
class C(A):
    pass
class D(A):
    pass
class E(B,D):
    pass
obj2 = E()
obj2.x
'''Output --> 10'''