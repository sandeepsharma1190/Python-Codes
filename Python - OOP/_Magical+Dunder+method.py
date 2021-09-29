class DataUser():
    def __init__(self, name, age):
        self.name = name
        self.age= age
        
    def __str__(self):
        return' User name is: {} and has {} years old.'.format(self.name, self.age)
    
    def __len__(self):
        return self.age

user_1 = DataUser('Sandeep', 32)
user_2 = DataUser('Python', 31)
     
print(user_1)
str(user_1)
len(user_1)
str(user_1)
len(user_2)