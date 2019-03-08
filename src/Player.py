from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.clock import Clock

class Player(FloatLayout):
    def __init__(self, levels, **kwargs):
        super(Player, self).__init__(**kwargs)
        
        # Getting the defualt keyboard and binding 'keyup' and 'keydown'
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)
        self.keys_pressed = set() # Making a set (array) of all currently pressed keys

        Clock.schedule_interval(self.CheckKeys, 0.01)

        self.LEVEL_NUM = 0

        self.cam = Camera(levels[self.LEVEL_NUM]) # initalizing a camera
        self.add_widget(self.cam) # adding the camera
        self.cam.render()

    def CheckKeys(self, dt):
        # Generic WASD movement
        if 'w' in self.keys_pressed:
            self.cam.moveY(1000*dt)
        if 'a' in self.keys_pressed:
            self.cam.moveX(-(1000*dt))
        if 's' in self.keys_pressed:
            self.cam.moveY(-1000*dt)
        if 'd' in self.keys_pressed:
            self.cam.moveX(1000*dt)
    
    def _keyboard_closed(self):
        # Unbinding the window's keyboard and setting it to 'None'
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard.unbind(on_key_up=self._on_keyboard_up)
        self._keyboard = None
    
    # Adding the key pressed to the array
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        self.keys_pressed.add(keycode[1])
    # Removing the key released from the array
    def _on_keyboard_up(self, keyboard, keycode):
        self.keys_pressed.remove(keycode[1])

class Camera(BoxLayout):
    def __init__(self, current_level, **kwargs):
        super(Camera, self).__init__(**kwargs)
        
        self.size=current_level.size #setting the size of this to the size of the current level
        # Setting 'self.level' and adding it as a wiget
        self.level = current_level
        self.add_widget(self.level)

    def setLevel(self, level):
        # Removing the current level and adding the new one
        self.remove_widget(self.level)
        self.level = level
        self.add_widget(self.level)

    # Looping through the blocks and changing their x / y position
    def moveX(self, num):
        for block in self.level.blocks:
                if block is not None:
                    block.x-=num
    def moveY(self, num):
        for block in self.level.blocks:
                if block is not None:
                    block.y-=num

    def render(self):
        self.level.render()