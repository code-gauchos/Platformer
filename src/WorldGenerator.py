import os
from random import choice

from PIL import Image

def generate_world():
    land = generate_land().copy()
    return land

def generate_land():
    possible_land = os.listdir("src/res/img/islands/")
    land=choice(possible_land)
    print(land)

    result=(Image.open("src/res/img/islands/"+land))

    return result

if __name__ == "__main__":
    generate_world()