# main.py
from kivy.app import App
import os, sys
from kivy.resources import resource_add_path, resource_find
from kivy.uix.screenmanager import ScreenManager
from mainScreen import MainScreen
from loginScreen import LoginScreen
from registerScreen import RegisterScreen
from openingScreen import OpeningScreen
from menuScreen import MenuScreen
from flowerScreen import FlowerScreen
from addflowerScreen import AddFlowerScreen
from detailsScreen import DetailsScreen

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(OpeningScreen(name='opening_screen'))
        sm.add_widget(MainScreen(name='main_screen'))
        sm.add_widget(LoginScreen(name='login_screen'))
        sm.add_widget(RegisterScreen(name='register_screen'))
        sm.add_widget(MenuScreen(name='menu_screen'))
        sm.add_widget(FlowerScreen(name='flower_screen'))
        sm.add_widget(AddFlowerScreen(name='addflower_screen'))
        sm.add_widget(DetailsScreen(name='details_screen'))
        return sm

if __name__ == '__main__':
    app = MainApp()
    app.run()