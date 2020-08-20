######### Game - Breaking out of a while Loop###
import random

player_health = 300
enemy_strike_min = 30
enemy_strike_max = 60

while player_health > 0:
    demage = random.randrange(enemy_strike_min, enemy_strike_max)
    player_health = player_health - demage
    if player_health <= 0:
        player_health = 0
    print ('Your enemy strikes for:', demage, 'and your health is:', player_health)
    if player_health == 0:
        print('You profile is dead')