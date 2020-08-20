dict_new = {1: 'Python', 2: 'Julia', 3: 'Data Science'}
dict_new[1]
print (dict_new.items())

#merge 2 lists to make a dictionary
key = ['Sandeep', 'Amit', 'Jaspreet']
vals = ['Python', 'Tableau', 'Julia']
dict1 = dict(zip(key,vals))
dict1['vikas'] = 'SQL'          #To add values
del dict1['vikas']          # Del data for vikas

# Dictionary and list in dictionary
prog = {'rahul': 'batting', 'bumrah': 'bowling', 'kohli':['batting', 'bowling'], 
        'jadeja':{'batting': 'lefty', 'bowling': 'spinner'}}
print (prog['bumrah'])
print (prog['kohli'])
print (prog['kohli'][1])
print (prog['jadeja'])
print (prog['jadeja']['bowling'])
'''---------------------------------------------------------------'''
flight_prices = {
    "Chicago": 199,
    "San Francisco": 499,
    "Denver": 295
}

print(flight_prices["Chicago"])
print(flight_prices["Denver"])
# print(flight_prices["Seattle"])
# print(flight_prices["chicago"])

gym_membership_packages = {
    29: ["Machines"],
    49: ["Machines", "Vitamin Supplements"],
    79: ["Machines", "Vitamin Supplements", "Sauna"]
}

print(gym_membership_packages[49])
print(gym_membership_packages[79])
# print(gym_membership_packages[100])

print(gym_membership_packages.get(29, ["Basic Dumbbells"]))
print(gym_membership_packages.get(100, ["Basic Dumbbells"]))
print(gym_membership_packages.get(100))

########################## 2 #############################
############# the-in-and-not-in-operators-on-a-dictionary ############
# print("erm" in "watermelon")
# print("z" in "watermelon")
# print("z" not in "watermelon")

# print(10 in [10, 20, 25])
# print(30 in [10, 20, 25])
# print(30 not in [10, 20, 25])

pokemon = {
    "Fire": ["Charmander", "Charmeleon", "Charizard"],
    "Water": ["Squirtle", "Warturtle", "Blastoise"],
    "Grass": ["Bulbasaur", "Venusaur", "Ivysaur"]
}

print("Fire" in pokemon)
print("Grass" in pokemon)
print("Electric" in pokemon)
print("fire" in pokemon)

print("Electric" not in pokemon)
print("fire" not in pokemon)
print("Zombie" not in pokemon)
print("Water" not in pokemon)

if "Zombie" in pokemon:
    print(pokemon["Zombie"])
else:
    print("The category of Zombie does not exist!")
    

######################### 3 ##################################
######## add-or-modify-key-value-pair-in-dictionary ##############
    sports_team_rosters = {
    "New England Patriots": ["Tom Brady", "Rob Gronkowski", "Julian Edelman"],
    "New York Giants": ["Eli Manning", "Odell Beckham"]
}

# print(sports_team_rosters["Pittsburgh Steelers"])
'''sports_team_rosters = {"Pittsburgh Steelers": ["Ben Roethlisberger", "Antonio Brown"]}'''
########### or ####################
sports_team_rosters["Pittsburgh Steelers"] = ["Ben Roethlisberger", "Antonio Brown"]
# print(sports_team_rosters["Pittsburgh Steelers"])
# print(sports_team_rosters)


##### to override #############
sports_team_rosters["New York Giants"] = ["Eli Manning"]


video_game_options = {}
''' video_game_options = dict()'''

video_game_options["subtitles"] = True
video_game_options["difficulty"] = "Medium"
video_game_options["volume"] = 7
print(video_game_options)

video_game_options["difficulty"] = "Hard"
video_game_options["subtitles"] = False
video_game_options["Volume"] = 10
print(video_game_options)


words = ["danger", "beware", "danger", "beware", "beware"]

def count_words(words):
    counts = {}
    for word in words:
        if word in counts:
            # counts[word] = counts[word] + 1
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(count_words(words))

############################### 4 ################################
################ the-setdefault-method #########################
film_directors = {
    "The Godfather": "Francis Ford Coppola",
    "The Rock": "Michael Bay",
    "Goodfellas": "Martin Scorsese"
}

print(film_directors.get("Goodfellas"))
print(film_directors.get("Bad Boys", "Michael Bay"))
print(film_directors)

# film_directors.setdefault("Bad Boys")
# print(film_directors)

#### Set dafault will add values

film_directors.setdefault("Bad Boys", "Michael Bay")
print(film_directors)

film_directors.setdefault("Bad Boys", "A good director")
print(film_directors)