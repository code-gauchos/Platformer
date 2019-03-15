from kivy.uix.floatlayout import FloatLayout

from Blocks import Block
from PIL import Image

class Level(FloatLayout):
    Index=0
    def __init__(self, name, file, blocks, **kwargs):
        super(Level, self).__init__(**kwargs)
        self.player_pos = None
        self.pos = (0,0)
        self.blocks_arr=blocks
        self.blocks = self.ParseLevel(file)
        assert (self.player_pos is not None), ("There is no player in the level \"{0}\"".format(name))
        self.number=Level.Index
        Level.Index+=1


    def render(self):
        for block in self.blocks:
            if block is not None:
                self.add_widget(block)
                block.render()

    def ParseLevel(self, file):
        result=[]

        img = Image.open("src/res/img/levels/"+file)
        self.width, self.height = img.size

        pixels=img.load()

        result = list()
        for x in range(self.width):
            for y in range(self.height):
                block_type = self.formatPixel(pixels[x,y])
                if block_type is not None:
                    for block in range(len(self.blocks_arr)):
                        if block_type is -1:
                            # The player has to start less than 10 blocks in
                            assert (x < 10), ("The player must start less than 10 blocks into the level! ({0}, {1})".format(x, y))
                            self.player_pos = [x*30,(self.height*30)-30-(y*30)]
                            # X: current x * block_height
                            # Y: Max height (height*30) - 30 - (current y * block_height) since it starts bottom down, and -30 since everything is off by one block up
                            break
                        elif block_type.number is self.blocks_arr[block].number:
                            res=Block(block_type.file, block_type.color)
                            res.pos=(x*res.size[0], self.height * res.size[1]-res.size[1]-(y*res.size[1]))
                            result.append(res)
                            break
        return result

    def formatPixel(self, pixel):
        result=[]
        for block in self.blocks_arr:
            r,g,b,a=pixel # Setting r, g, b, and a from that position in the level
            if [r,g,b,a] == block.color+[255]: # Checking if that color matches a block
                return block # if so, append that block to the result
                break
            elif [r,g,b,a] == [255,0,0,255]: # Checking if it is a 'player_start' block (red)
                return -1
                break
            #checking if this is the last block
            if block.number+1 is Block.Index:
                return None