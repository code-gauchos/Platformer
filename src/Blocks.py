from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Rectangle

class Block(RelativeLayout):
    Index=0
    def __init__(self, file, color, **kwargs):
        super(Block, self).__init__(**kwargs)
        self.file=file
        self.color=color
        self.number=Block.Index
        Block.Index+=1
        self.size = (30,30)

    def render(self):
        self.canvas.clear()
        with self.canvas:
            Rectangle(pos=(0,0),size=self.size,source="src\\res\\img\\blocks\\"+self.file)
