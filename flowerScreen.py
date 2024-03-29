from kivy.app import App,  Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

import sqlite3

Builder.load_file("flowerScreen.kv")

class FlowerScreen(Screen):
    bg_color = (0.9607843137254902, 0.8392156862745098, 0.7294117647058823, 1.0)
    def __init__(self, **kwargs):
        super(FlowerScreen, self).__init__(**kwargs)
        
    def delPlant(self, relationID):
        conn = sqlite3.connect('mypatch.sqlite')
        cursor = conn.cursor()

        query = 'DELETE FROM relacje WHERE id = "'+str(relationID)+'";'
        print(query)
        cursor.execute(query)
        conn.commit()
        conn.close()

    def go_to_menu_screen(self, instance):
        self.manager.current = 'menu_screen'

    def on_enter(self):
        app = App.get_running_app()
        login = app.login
        password = app.password

        conn = sqlite3.connect('mypatch.sqlite')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users WHERE login = ?', (login,))
        user = cursor.fetchone()

        cursor.execute('SELECT rosliny.Nazwa, rosliny.Zdjecie, rosliny.Opis, relacje.ID FROM relacje JOIN rosliny ON relacje.roslina_ID = rosliny.ID WHERE relacje.urzytkownik_ID = ?', (user[0],))
        flowers = cursor.fetchall()
        # print(flowers)

        conn.close()


        self.ids.plants.clear_widgets()

        for flower in flowers:
            plantGrid = BoxLayout(orientation="horizontal", padding = 5)
            
            flower_label = Label(text=flower[0], font_name="font.ttf", font_size=18, size_hint=(1, 1), color=(0.55, 0.36, 0.29, 1))
            zrodlo = 'photos/'+str(flower[1])
            image = Image(source=zrodlo)
            
            
            tekst = flower[2].split()
            opis1 = ""
            dlugosc_linii = 0

            for slowo in tekst:
                if dlugosc_linii + len(slowo) >= 50:
                    opis1 += '\n'
                    dlugosc_linii = 0
                opis1 += slowo + ' '
                dlugosc_linii += len(slowo) + 1

            # print(opis1)

            opis = Label(text=opis1, font_name="font.ttf", font_size=12, size_hint=(1, 1), color=(0.55, 0.36, 0.29, 1))
            
            text = BoxLayout(orientation="vertical")
            text.add_widget(flower_label)
            text.add_widget(opis)
            
            button = Button(text='Usun kwiat',
                            font_name="font.ttf",
                            size_hint=(.5, .5),
                            pos_hint={'center_x': 0.5, 'center_y': 0.5},
                            background_color=(0.55, 0.8, 0.6, 1)
                            )
            button.bind(on_press=lambda x, relation_id=flower[3]: self.delPlant(relation_id))

            plantGrid.add_widget(image)
            plantGrid.add_widget(text)
            plantGrid.add_widget(button)
            
            self.ids.plants.add_widget(plantGrid)
        