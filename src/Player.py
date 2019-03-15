from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Rectangle, Color
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


        self.width = Window.width
        self.height = Window.height

        Clock.schedule_interval(self.CheckKeys, 0.01)

        self.LEVEL_NUM = 0

        self.cam = Camera(levels[self.LEVEL_NUM]) # initalizing a camera
        self.add_widget(self.cam) # adding the camera
        self.cam.render()
        # Creating the Player:
        tempPos = self.cam.level.player_pos
        self.sprite=RelativeLayout(size=(60,60), pos=tempPos)
        with self.sprite.canvas:
            Color(0, 0, 1, 1)
            Rectangle(size=(60,60))
            Rectangle(size=self.sprite.size,source="src\\res\\img\\player.png")
        self.add_widget(self.sprite) 

    def CheckKeys(self, dt):
        self.move("down", dt) # Gravity!

        # Generic WASD movement
        if 'a' in self.keys_pressed:
            self.move("left", dt)
        if 'd' in self.keys_pressed:
            self.move("right", dt)

        if "space" in self.keys_pressed:
            self.jump(dt)


        if 'z' in self.keys_pressed:
            self.cam.moveTo()

    def move(self, direction, delta):
        speed = 1000 * delta
        # No "up" because jump handles that!
        if direction is "down":
            for block in self.cam.level.blocks: # Looping through the blocks in the current level
                if ((block.y+30) < self.cam.position[1]) and ((block.x > self.cam.position[0]+60)):
                    pass#self.cam.moveY(-speed)
        if direction is "left":
            self.cam.moveX(-speed)
            print("Camera position: "+str(self.cam.position))
        elif direction is "right":
            self.cam.moveX(speed)
            print("Camera position: "+str(self.cam.position))
    
    def jump(self, delta):
        pass
    
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

        tempPos = self.level.player_pos
        self.position = tempPos


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
        self.position[0] += num
    def moveY(self, num):
        for block in self.level.blocks:
                if block is not None:
                    block.y-=num
        self.position[1] += num
    def moveTo(self, *, x=None, y=None):
        if x is None and y is None:
            print("Moving from: "+str(self.position)+" To: "+str(self.level.player_pos))
            self.moveTo(x=self.level.player_pos[0], y=self.level.player_pos[1]) # If no position is specified, move to the defualt player position
            return
        if x is not None:
            self.moveX(x-self.position[0])
        if y is not None:
            self.moveY(y-self.position[1])

    def snap(self):
        if self.position[0]%30 is not 0 or self.position[1]%30 is not 0:
            self.moveX(self.round30(self.position[0])-self.position[0])
            self.moveY(self.round30(self.position[1])-self.position[1])
        

    def render(self):
        self.level.render()

    def round30(self, num):
        return int(30 * round(float(num)/30))