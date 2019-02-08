from kivy.uix.floatlayout import FloatLayout

from Blocks import Block
from PIL import Image

class Level(FloatLayout):
    Index=0
    def __init__(self, name, file, blocks, **kwargs):
        super(Level, self).__init__(**kwargs)
        self.pos = (0,0)
        self.blocks_arr=blocks
        self.data = self.formatLevel(self.ParseLevel(file), self.blocks_arr)
        self.getBlocks()
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
        img = img.rotate(270, expand=True)
        self.width, self.height = img.size

        pixels=img.load()

        for i in range(self.width):
            for j in range(self.height):
                result.append(pixels[i,j])

        return result

    def formatLevel(self, data, blocks):
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

    def getBlocks(self):
        result=[]
        i=0
        for dat in self.data:
            for block in range(len(self.blocks_arr)):
                 if dat is self.blocks_arr[block].number:
                     res=Block(self.blocks_arr[block].file, self.blocks_arr[block].color)
                     res.pos=((i%self.height)*res.size[0], int(i/self.height)*res.size[1])
                     result.append(res)

                 if block is len(self.blocks_arr)-1:
                     result.append(None)
            i+=1
        self.blocks=result
