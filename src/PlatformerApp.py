from kivy.app import App
from kivy.uix.button import Button

class PlatformApp(App):
    def build(self):
        return Button(text='Hello World')

PlatformApp().run()