from itertools import chain

from kivy.uix.floatlayout import FloatLayout
from final_class import final

from Blocks import Block
from Levels import Level

@final
class Game(FloatLayout):
    def __init__(self, blocks, levels, **kwargs):
        super(Game, self).__init__(**kwargs)
        self.blocks_arr=blocks
        self.levels=levels
        for level in levels:
            level.data = Game.formatLevel(level.tempData, blocks)
            level.tempData = None
        self.Begin(0)

    def Begin(self, LevelNum):
        self.blocks=self.getBlocks(self.levels[LevelNum], self.blocks_arr)
        self.Levels_run(self.blocks)
        

    def Levels_run(self, Blocks):
        for block in Blocks:
            if block is not None:
                self.add_widget(block)
                block.render()
        return True


    @staticmethod
    def formatLevel(data, blocks):
        result=[]
        for res in data:
            for block in blocks:
                r,g,b,a=res
                if [r,g,b,a] == block.color+[255]:
                    result.append(block.number)
                    break
                #checking if this is the last block
                if block.number+1 is Block.Index:
                    result.append(None)
        return result

    def getBlocks(self, level, blocks_arr):
        result=[]
        height=level.height
        i=0
        for dat in level.data:
            for block in range(len(blocks_arr)):
                 if dat is blocks_arr[block].number:
                     res=Block(blocks_arr[block].file, \
                     blocks_arr[block].breakable, blocks_arr[block].color, blocks_arr[block].format)
                     res.pos=(i%height, int(i/height))
                     result.append(res)

                 if block is len(blocks_arr)-1:
                     result.append(None)
            i+=1
        return result
