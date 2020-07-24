import random

def username_generator():
#download word list.
#seperate into adjectives and nouns list
#get total amount of lines in each list
#randomly choose number line in that list
#return word from list
    adjs = ["hungry", "stanky", "wobbly", "fatigued", "brazen"]
    nouns = ["dog", "camel", "foot", "crumpet", "humidifier"]

    #choose randomly from lists
    noun = random.choice(nouns).capitalize()
    adj = random.choice(adjs).capitalize()
    #add them together
    username = adj + noun
    return username

