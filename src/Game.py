from itertools import chain

from kivy.uix.floatlayout import FloatLayout
from final_class import final

from Blocks import Block
from Levels import level

@final
class Game(FloatLayout):
    def __init__(self, blocks, world, levels):
        self.blocks=blocks
        self.world=world
        self.levels=levels
        for level in levels:
            level.data = Game.formatLevel(level.tempData, blocks)
            level.tempData = None

    @staticmethod
    def formatLevel(data, blocks):
        result=[]
        for res in data:
            for block in blocks:
                r,g,b,a=res
                if [r,g,b,a] == (block.color).append(255):
                    result.append(block.number)
                    break
                #checking if this is the last block
                if block.number+1 is Block.Index:
                    result.append(None)
