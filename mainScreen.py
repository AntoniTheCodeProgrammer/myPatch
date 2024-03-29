from kivy.app import App,  Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image


import sqlite3

Builder.load_file("mainScreen.kv")

class MainScreen(Screen):
    bg_color = (0.9607843137254902, 0.8392156862745098, 0.7294117647058823, 1.0)
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        
    def go_to_menu_screen(self, instance):
        self.manager.current = 'menu_screen'

    def on_enter(self):
        app = App.get_running_app()
        login = app.login
        password = app.password
        print("Login:", login)
        print("Password:", password)

        conn = sqlite3.connect('mypatch.sqlite')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users WHERE login = ?', (login,))
        user = cursor.fetchone()

        welcome_message = "Witaj, " + user[1]
        self.ids.welcome_label.text = welcome_message

        query = 'SELECT rosliny.Nazwa, rosliny.Zdjecie FROM relacje JOIN rosliny ON relacje.roslina_ID = rosliny.ID WHERE relacje.urzytkownik_ID = "'+str(user[0])+'";'
        # query = 'SELECT * FROM users;'
        # print(query)
        cursor.execute(query)
        flowers = cursor.fetchall()
        
        # print(flowers)

        


        self.ids.plants_layout.clear_widgets()

        for flower in flowers:
            plantGrid = GridLayout(cols=1)
            #tutaj zamiast GridLayout chciałbym by brał PlantGridLayout
            
            flower_label = Label(text=flower[0], font_name="font.ttf", size_hint=(1, 1), color=(0.55, 0.36, 0.29, 1))
            zrodlo = 'photos/'+str(flower[1])
            image = Image(source=zrodlo)

            plantGrid.add_widget(image)
            plantGrid.add_widget(flower_label)

            self.ids.plants_layout.add_widget(plantGrid)

        self.ids.add_plants_layout.clear_widgets()

        cursor.execute('SELECT Nazwa, Zdjecie FROM rosliny')
        flowers = cursor.fetchall()
        # print(flowers)

        for flower in flowers:
            plantGrid = GridLayout(cols=1)
            #tutaj zamiast GridLayout chciałbym by brał PlantGridLayout
            
            flower_label = Label(text=flower[0], font_name="font.ttf", size_hint=(1, 1), color=(0.55, 0.36, 0.29, 1))
            zrodlo = 'photos/'+str(flower[1])
            image = Image(source=zrodlo)

            plantGrid.add_widget(image)
            plantGrid.add_widget(flower_label)

            self.ids.add_plants_layout.add_widget(plantGrid)


        conn.close()