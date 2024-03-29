# Opening_screen.py
from kivy.app import App,  Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label

Builder.load_file("openingScreen.kv")

class OpeningScreen(Screen):
    bg_color = (0.42, 0.55, 0.45, 1)
    def __init__(self, **kwargs):
        super(OpeningScreen, self).__init__(**kwargs)
        

    def go_to_login_screen(self, instance):
        self.manager.current = 'login_screen'
    
    def go_to_register_screen(self, instance):
        self.manager.current = 'register_screen'