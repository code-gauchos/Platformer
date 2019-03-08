from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from final_class import final

from Player import Player 

@final
class Game(FloatLayout):
    def __init__(self, levels, **kwargs):
        super(Game, self).__init__(**kwargs)
        self.block_pos = None
        Window.on_maximize(self.win_max)
        self.m_fullscreen=False
        Window.show_cursor = False
        Window.bind(mouse_pos=self.on_mouse_pos)
        
        self.Begin(levels)

    def Begin(self, Levels):
        self.add_widget(Player(Levels))
    
    def on_mouse_pos(self, *args):
        if self.block_pos:
            self.remove_widget(self.block_pos)
        print(args[1])
        self.block_pos = Label(text="[b]Block("+str(int(args[1][0]/30))+","+str(int(args[1][1]/30))+")[/b]", markup=True, pos=((args[1][0]-(self.width/2)),(args[1][1]-(self.height/2))))
        print(self.block_pos.pos)
        self.add_widget(self.block_pos)
    
    def win_max(self, *args):
        Window.grab_mouse()
        Window.toggle_fullscreen()
        self.m_fullscreen = True