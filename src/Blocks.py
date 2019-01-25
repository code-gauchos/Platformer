from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle

from kivy.metrics import dp, sp

class Block(BoxLayout):
    Index=0
    def __init__(self, file, breakable, color, format="", **kwargs):
        super(Block, self).__init__(**kwargs)
        self.file=file
        self.breakable=breakable
        self.color=color
        if format is not "":
            self.format=format
        self.number=Block.Index
        Block.Index+=1
        self.size= dp(32),dp(32)

    def render(self):
        with self.canvas:
            Rectangle(pos=(0,0),size=self.size,source=self.file)
