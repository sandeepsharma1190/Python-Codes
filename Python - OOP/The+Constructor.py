class UserData():
    age = 0
    name = None
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    def user(self):
        print('User name is: {} and has {} years old.'.format(self.name,self.age))
user_1 = UserData('Sandeep', 32)
print(user_1.name)
type(user_1)


user_2 = UserData('Rashu', 31)
print(user_2.age)

user_3 = UserData('John', 30)
user_4 = UserData('Peter', 15)

avg_age = (user_1.age + user_2.age + user_3.age + user_4.age)/3
print(avg_age)

user_1.user()

class Rectangle():
    def __init__(self, length, width):
        self.width = width
        self.length = length
    def rect_area(self):
        return(self.length*self.width)
rect_1 = Rectangle(50,30)
rect_2 = Rectangle(140,60)
rect_3 = Rectangle(120,70)
rect_4 = Rectangle(100,80)

rect_1.length
rect_2.width
rect_3.rect_area()
type(rect_4)
print((rect_1.rect_area()+rect_2.rect_area()+rect_3.rect_area()+rect_2.rect_area())/4)


