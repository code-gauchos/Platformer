import json

import kivy
from kivy.app import App
from kivy.uix.button import Button

from Game import Game
from Blocks import Block
from Levels import Level

kivy.require("1.8.0")

class PlatformerApp(App):
    def build(self):
        self.blocks = self.LoadBlocks()
        self.levels = self.LoadLevels()

        return Game(self.levels)

    def LoadBlocks(self):
        result=[]

        with open("src/res/blocks.json") as file:
            data = json.load(file)
        for dat in data:
            result.append(Block(dat["file"], dat["color"]))
        return result

    def LoadLevels(self):
        result=[]

        with open("src/res/levels.json") as file:
            data = json.load(file)
        for dat in data:
            result.append(Level(dat["name"],dat["file"], self.blocks))

        return result

PlatformerApp().run()
