class newclass():
    def __init__(self, name, branch, year):
        self.n = name
        self.b = branch
        self.y = year
    def print_mehtod(self):
        print ('Name: ', self.n)
        print ('Branch: ', self.b)
        print ('Year: ', self.y)
obj1 = newclass ('Paul', 'IT', '1990')
obj1.print_mehtod()