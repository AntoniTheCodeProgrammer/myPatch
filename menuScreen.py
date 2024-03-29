# Menu_screen.py
from kivy.app import App,  Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label

Builder.load_file("menuScreen.kv")

class MenuScreen(Screen):
    bg_color = (0.42, 0.55, 0.45, 1)
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
       

    def go_to_opening_screen(self, instance):
        self.manager.current = 'opening_screen'
    
    def go_to_main_screen(self, instance):
        self.manager.current = 'main_screen'

    def go_to_flower_screen(self, instance):
        self.manager.current = 'flower_screen'

    def go_to_addflower_screen(self, instance):
        self.manager.current = 'addflower_screen'