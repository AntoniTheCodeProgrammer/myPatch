from kivy.app import App,  Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image


import sqlite3

Builder.load_file("detailsScreen.kv")

class DetailsScreen(Screen):
    bg_color = (0.9607843137254902, 0.8392156862745098, 0.7294117647058823, 1.0)
    def __init__(self, **kwargs):
        super(DetailsScreen, self).__init__(**kwargs)
        
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
        
    def go_to_main_screen(self, instance):
        self.manager.current = 'main_screen'
        
    def go_to_menu_screen(self, instance):
        self.manager.current = 'menu_screen'

    def on_enter(self):
        app = App.get_running_app()
        plant = app.plant

        conn = sqlite3.connect('mypatch.sqlite')
        cursor = conn.cursor()

        query = 'SELECT * FROM rosliny WHERE ID ="'+str(plant)+'"'
        # print(query)
        cursor.execute(query)
        flower = cursor.fetchone()
        print(flower)

        label = Label(text=flower[1], font_name="font.ttf", font_size=32, size_hint=(1, 0.3), color=(0.55, 0.36, 0.29, 1))
        image = Image(source="photos/"+flower[3], size_hint=(1, 0.5))
        
        tekst = flower[2].split()
        opis1 = ""
        dlugosc_linii = 0

        for slowo in tekst:
            if dlugosc_linii + len(slowo) >= 50:
                opis1 += '\n'                    
                dlugosc_linii = 0
            opis1 += slowo + ' '
            dlugosc_linii += len(slowo) + 1
        
        description = Label(text=opis1, font_name="font.ttf", font_size=24, size_hint=(1, 1), color=(0.55, 0.36, 0.29, 1))
        
        button_layout = BoxLayout(orientation="horizontal", size_hint=(1, 0.3), padding=20)
        
        button = Button(text='Powrot',
                        font_name="font.ttf",
                        size_hint=(.5, 1),
                        pos_hint={'center_x': 0.5, 'center_y': 0.5},
                        background_color=(0.55, 0.8, 0.6, 1)
                        )
     
        button2 = Button(text='Dodaj mnie!',
                        font_name="font.ttf",
                        size_hint=(.5, 1),
                        pos_hint={'center_x': 0.5, 'center_y': 0.5},
                        background_color=(0.55, 0.8, 0.6, 1)
                        )
            
        button.bind(on_press=self.go_to_main_screen)
        button2.bind(on_press=lambda x, plant_id=flower[0]: self.addPlant(plant_id))
        
        button_layout.add_widget(button)
        button_layout.add_widget(button2)
        self.ids.plant.clear_widgets()
        self.ids.plant.add_widget(label)
        self.ids.plant.add_widget(image)
        self.ids.plant.add_widget(description)
        self.ids.plant.add_widget(button_layout)
        

        
        

        conn.close()