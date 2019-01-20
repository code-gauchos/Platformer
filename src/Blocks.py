from kivy.uix.boxlayout import BoxLayout

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
            Rectangle
