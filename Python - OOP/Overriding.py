#Overiding
class Skills():
    def __init__(self):
        pass
    def msg(self):
        print('skills')

class HR():
    def __init__(self):
        super(HR, self).__init__()
    def msg(self):
        print('HR msg')

communication = HR()
communication.msg()



