from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle

class Block(BoxLayout):
    Index=0
    def __init__(self, file, breakable, color, **kwargs):
        super(Block, self).__init__(**kwargs)
        self.file=file
        self.breakable=breakable
        self.color=color
        self.number=Block.Index
        Block.Index+=1

    def render(self):
        with self.canvas:
            Rectangle(pos=(0,0),size=self.size,sou)
