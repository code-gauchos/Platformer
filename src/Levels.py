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
        self.data = self.formatLevel(self.ParseLevel(file))
        self.getBlocks()
        #assert (self.player_pos is not None), ("There is no player in the level \"{0}\"".format(name))
        for block in self.blocks:
            if block is not None:
                print(block.file, end=': ')
                print("(" + str(block.x/30) + ", " + str(block.y/30) + ")")
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
        #img = img.rotate(270, expand=True)
        self.width, self.height = img.size

        img.save("src/res/img/levels/1"+file)

        pixels=img.load()

        for i in range(self.width):
            for j in range(self.height):
                result.append(pixels[i,j])

        return result

    def formatLevel(self, data):
        result=[]
        for res in data:
            for block in self.blocks_arr:
                r,g,b,a=res # Setting r, g, b, and a from that position in the level
                if [r,g,b,a] == block.color+[255]: # Checking if that color matches a block
                    result.append(block.number) # if so, append that block to the result
                    break
                elif [r,g,b,a] == [255,0,0,255]: # Checking if it is a 'player_start' block (red)
                    result.append(-1)
                #checking if this is the last block
                if block.number+1 is Block.Index:
                    result.append(None)
        return result

    def getBlocks(self):
        result=[]
        i=0
        for dat in self.data:
            for block in range(len(self.blocks_arr)):
                if dat is self.blocks_arr[block].number:
                    res=Block(self.blocks_arr[block].file, self.blocks_arr[block].color)
                    res.pos=((i%self.height)*res.size[0], (self.height-int(i/self.width))*res.size[1])
                    print(str(i) + " => " + str(res.pos))
                    result.append(res)
                    break
                elif dat is -1: # Player block!
                    plx = i%self.width # Player x = (remainder of i/level_width) times 30 (block size)
                    #assert (plx < 11), "Player is to far out! ({0})".format(plx) # Player has to be within the first 10 blocks!
                    self.player_pos = (plx*30, int(i/self.width)*30) # player_pos = (x, y); y = i/level_height, floored to integer, times 30 (block size)
                    break
                if block is len(self.blocks_arr)-1:
                    result.append(None)
            i+=1
        self.blocks=result
