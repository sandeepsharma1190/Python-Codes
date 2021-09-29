class UserData():
    age = 0
    name = None
    def __init__(self, name, age):
        self.name = name
        self.age  = age 
user_2 = ("David", 50)
user_1 = ("Sara", 40)


class PhoneNum(UserData):
    def __init__(self, name, age, num):
        super().__init__(name, age)
        self.num = num

User_1 = PhoneNum("Sara", 40, 123456789)

user_2 = PhoneNum("David", 60, 234567)

user_2.age

user_1 = PhoneNum("John", 15, 987654321)

user_1.name

user_1.age

user_1.num

