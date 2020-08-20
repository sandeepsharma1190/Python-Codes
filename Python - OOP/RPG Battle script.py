##### RPG Battle script ########'
class Enemy:
    def __init__(self, hp, mp):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
    def get_hp(self):
        return self.hp
    
enemy = Enemy(200,60)
print ('HP:', enemy.get_hp())