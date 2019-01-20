from itertools import chain

from kivy.uix.floatlayout import FloatLayout
from final_class import final

from Blocks import Block
from Missions import Mission

@final
class Game(FloatLayout):
    def __init__(self, blocks, world, missions):
        self.blocks=blocks
        self.world=world
        self.missions=missions
        for mission in missions:
            mission.data = Game.formatMission(mission.tempData, blocks)
            mission.tempData = None

    @staticmethod
    def formatMission(data, blocks):
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
        print(result)

