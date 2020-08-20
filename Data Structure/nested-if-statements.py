ingredient1 = "Pizza"
ingredient2 = "Sausage"

if ingredient1 == "Pasta":
    if ingredient2 == "Meatballs":
        print("I recommend making pasta and meatballs")
    else:
        print("I recommend making plain pasta")
else:
    print("I have no recommendations")

if ingredient1 == "Pasta" and ingredient2 == "Meatballs":
    print("I recommend making pasta and meatballs")
elif ingredient1 == "Pasta":
    print("I recommend making plain pasta")
else:
    print("I have no recommendations")

