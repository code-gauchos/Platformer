import json

import kivy
from kivy.app import App
from kivy.uix.button import Button

from Game import Game
import WorldGenerator as wg
from Missions import Mission
from Blocks import Block
from Tiles import Tile

kivy.require(kivy.__version__)

class PlatformerApp(App):
    def build(self):
        blocks = self.LoadBlocks()
        missions = self.LoadMissions()
        world = wg.generate_world()
        
        return Game(blocks, world, missions)

    def LoadBlocks(self):
        result=[]

        with open("src/res/blocks.json") as file:
            data = json.load(file)
        for dat in data:
            result.append(Block(dat["file"], dat["breakable"], dat["color"]))
        return result

    def LoadTiles(self):
        result=[]

        with open("src/res/tiles.json") as file:
            data = json.load(file)
        for dat in data:
            result.append(Tile(dat["file"], dat["walkable"], dat["color"]))
        return result

    def LoadMissions(self):
        result=[]

        with open("src/res/missions.json") as file:
            data = json.load(file)
        for dat in data:
            result.append(Mission(dat["name"],dat["length"],dat["file"]))

        return result

PlatformerApp().run()