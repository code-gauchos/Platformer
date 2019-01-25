from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget

from kivy.metrics import dp, sp

class Block(Widget):
    Index=0
    def __init__(self, file, breakable, color, format="", **kwargs):
        super(Block, self).__init__(**kwargs)
        self.file=file
        self.breakable=breakable
        self.color=color
        if format is not "":
            self.format=format
        else:
            self.format=None
        self.number=Block.Index
        Block.Index+=1
        self.size = (128,128)

    def render(self):
        with self.canvas:
            Rectangle(pos=(0,0),size=self.size,source="src\\res\\img\\blocks\\"+self.file)
            print("hi"+str(self.number))
