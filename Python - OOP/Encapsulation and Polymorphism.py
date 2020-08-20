########### Encapsulation and Polymorphism #########

'''Encapsulation : - Abstracting + Data Hiding
Abstraction is showing essential features and hiding non-essential features to user.
abstraction: - like, we send an email, but we dont know what is happening in the backend. 
second example : - like, we see a car from outside, but car contains, tire, engine and piston etc. 
that is abstraction. Inside car, how engine is working from inside, that is data hiding'''

class encap():
    def __init__(self):
        self.a = 123
        self._b = 123
        self.__c = 123
obj1 = encap()
print(obj1.a, obj1._b, obj1.__c)


######Polymorphism : Functions with same name, but functioning in different ways
'''we behave different in front of frnds and family'''

class shark():
    def swim(self):
        print ('Shark can swim')
    def bones(self):
        print ('Shark has strong bones')
class anotherfish():
    def swim(self):
        print ('Another fish can swim')
    def bones(self):
        print ('Another fish has weak bones')
s1 = shark()
af1 = anotherfish()
for fishes in (s1, af1):
    print (fishes.swim)
    print (fishes.bones)
    
###########    
def insideocean(fish):
    fish.swim()
    
s1 = shark()
af1 = anotherfish()

insideocean(s1)
insideocean(af1)