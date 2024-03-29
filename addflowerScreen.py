from kivy.app import App, Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
import sqlite3

Builder.load_file("addflowerScreen.kv")

class AddFlowerScreen(Screen):
    bg_color = (0.9607843137254902, 0.8392156862745098, 0.7294117647058823, 1.0)

    def addPlant(self, plantID):
        conn = sqlite3.connect('mypatch.sqlite')
        cursor = conn.cursor()

        
        cursor.execute('SELECT MAX(id) FROM relacje;')
        id = cursor.fetchone()[0]
        id = int(id)
        id += 1
        print(id)
        app = App.get_running_app()
        login = app.login
        query = "SELECT id FROM users WHERE login = ?"
        cursor.execute(query, (login,))
        result = cursor.fetchone()[0]

        query = 'INSERT INTO relacje(ID, roslina_ID, urzytkownik_ID) VALUES ("'+str(id)+'", "'+str(plantID)+'", "'+str(result)+'")'
        print(query)
        cursor.execute(query)
        conn.commit()
        conn.close()

    def go_to_menu_screen(self, instance):
        self.manager.current = 'menu_screen'
        
    def go_to_details_screen(self, plant):
        app = App.get_running_app()
        app.plant = plant
        self.manager.current = 'details_screen'

    def on_enter(self):
        app = App.get_running_app()
        login = app.login
        password = app.password

        conn = sqlite3.connect('mypatch.sqlite')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users WHERE login = ?', (login,))
        user = cursor.fetchone()

        cursor.execute('SELECT ID, Nazwa, Zdjecie, Opis FROM rosliny')
        flowers = cursor.fetchall()

        # print(flowers)

        conn.close()

        self.ids.plants.clear_widgets()

        for flower in flowers:
            plantGrid = BoxLayout(orientation="horizontal", padding=5)            
            flower_label = Label(text=flower[1], font_name="font.ttf", size_hint=(2, 1), color=(0.55, 0.36, 0.29, 1))
            zrodlo = 'photos/'+str(flower[2])
            image = Image(source=zrodlo, size_hint=(0.5, 1))
            
            button = Button(text='Zobacz wiecej',
                            font_name="font.ttf",
                            size_hint=(.5, .5),
                            pos_hint={'center_x': 0.5, 'center_y': 0.5},
                            background_color=(0.55, 0.8, 0.6, 1)
                            )
     
            button2 = Button(text='Dodaj mnie!',
                            font_name="font.ttf",
                            size_hint=(.5, .5),
                            pos_hint={'center_x': 0.5, 'center_y': 0.5},
                            background_color=(0.55, 0.8, 0.6, 1)
                            )
            
            button.bind(on_press=lambda x, plant_id=flower[0]: self.go_to_details_screen(plant_id))
            button2.bind(on_press=lambda x, plant_id=flower[0]: self.addPlant(plant_id))
            
            buttons = BoxLayout(orientation = "vertical", padding=3)
           
            buttons.add_widget(button)
            buttons.add_widget(button2)
            
            plantGrid.add_widget(image)
            plantGrid.add_widget(flower_label)
            # plantGrid.add_widget(opis)
            plantGrid.add_widget(buttons)

            self.ids.plants.add_widget(plantGrid)
