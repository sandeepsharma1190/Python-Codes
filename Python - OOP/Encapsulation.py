# Encapsulation
class MyClass():
    def set_age(self, num):
        self.age = num
    def get_age(self):
        return self.age
Sara = MyClass()
Sara.set_age(40)
print(Sara.get_age())
Sara.set_age('fourty')
Sara.get_age()




