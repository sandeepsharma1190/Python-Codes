####### Private method #######
###"__" means it is private method. Can not be accessed from outside

class Car:
    __maxspeed = 0
    __name = ''
    def __init__(self):
        self.__maxspeed = 200
        self.__name = 'Sandeep'
    def drive(self):
        print ('Max speed of a car is ', self.__maxspeed)

obj1 = Car()
obj1.drive()

##############Wont work, because "__maxspeed" was in private method
obj1.__maxspeed = 400
obj1.drive()


###### How to change variable in Private method######
class Car2:
    __maxspeed = 0
    __name = ''
    def __init__(self):
        self.__maxspeed = 200
        self.__name = 'Sandeep'
    def drive(self):
        print ('Max speed of a car is ', self.__maxspeed)
    def setmaxspeed(self,speed):
        self.__maxspeed = speed

obj1.setmaxspeed = 400
obj1.drive()