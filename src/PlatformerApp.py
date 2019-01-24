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
        missions = self.LoadLevels()
        
        return Game(blocks, levels)

    def LoadBlocks(self):
        result=[]

        with open("src/res/blocks.json") as file:
            data = json.load(file)
        for dat in data:
            result.append(Block(dat["file"], dat["breakable"], dat["color"]))
        return result

    def LoadLevels(self):
        result=[]

        with open("src/res/missions.json") as file:
            data = json.load(file)
        for dat in data:
            result.append(Mission(dat["name"],dat["length"],dat["file"]))

        return result

PlatformerApp().run()
