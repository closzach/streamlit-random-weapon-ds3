import json
import random


def get_armes():
    file = open('./armes.json')
    data = json.load(file)
    file.close()
    return data

def get_arme_random(armes):
    random_key = random.choice(list(armes.keys()))
    return random_key, armes[random_key]

