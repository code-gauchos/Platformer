from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget

class Block(Widget):
    Index=0
    def __init__(self, file, color, **kwargs):
        super(Block, self).__init__(**kwargs)
        self.file=file
        self.color=color
        self.number=Block.Index
        Block.Index+=1
        self.size = (30,30)

    def render(self):
        with self.canvas:
            Rectangle(pos=(self.pos),size=self.size,source="src\\res\\img\\blocks\\"+self.file)
