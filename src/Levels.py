from kivy.uix.floatlayout import FloatLayout

from Blocks import Block
from PIL import Image

class Level(FloatLayout):
    Index=0
    def __init__(self, name, file, blocks):
        self.pos = (0,0)
        self.blocks_arr=blocks
        self.data = Level.formatLevel(self.ParseLevel(file), self.blocks_arr)
        self.number=Level.Index
        Level.Index+=1


    def render(self):
        for block in self.blocks:
            if block is not None:
                print(block)
                self.add_widget(block)
                block.render()

    def ParseLevel(self, file):
        result=[]

        img = Image.open("src/res/img/levels/"+file)
        img = img.rotate(-90, expand=True)
        width, height = img.size

        if(width > height):
            height = width
        elif(height > width):
            width = height

        img = img.resize((width, height))
        pixels=img.load()

        for i in range(width):
            for j in range(height):
                result.append(pixels[i,j])

        self.size = (width*30, height*30)
        return result

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

    def getBlocks(self):
        result=[]
        i=0
        for dat in self.data:
            for block in range(len(self.blocks_arr)):
                 if dat is self.blocks_arr[block].number:
                     res=Block(self.blocks_arr[block].file, self.blocks_arr[block].color)
                     res.pos=((i%height)*res.size[0], int(i/height)*res.size[1])
                     result.append(res)

                 if block is len(blocks_arr)-1:
                     result.append(None)
            i+=1
        self.blocks=result
