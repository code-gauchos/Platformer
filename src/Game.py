from itertools import chain

from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from final_class import final

from Blocks import Block
from Levels import Level

@final
class Game(FloatLayout):
    def __init__(self, levels, **kwargs):
        super(Game, self).__init__(**kwargs)
        ms=0
        for level in levels:
            if level.size[0] > ms:
                ms = level.size[0]
        self.size=(ms, ms)
        print(self.size)
        self.levels=levels
        self.Begin(0)

    def Begin(self, LevelNum):
        self.add_widget(self.levels[LevelNum])
        self.levels[LevelNum].render()
