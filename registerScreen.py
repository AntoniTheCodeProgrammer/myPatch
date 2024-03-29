from kivy.app import App,  Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

import sqlite3

Builder.load_file("registerScreen.kv")

class RegisterScreen(Screen):
    bg_color = (0.9607843137254902, 0.8392156862745098, 0.7294117647058823, 1.0)
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)

    def check_login(self, instance):

        self.name = self.ids.inputName.text
        self.surname = self.ids.inputSurname.text
        self.login = self.ids.inputLogin.text
        self.password = self.ids.inputPassword.text

        conn = sqlite3.connect('mypatch.sqlite')
        cursor = conn.cursor()
        cursor.execute('SELECT haslo FROM users WHERE login = ?', (self.login,))
        row = cursor.fetchone()

        cursor.execute('SELECT MAX(id) FROM users')
        id = cursor.fetchone()
        id = int(id[0])
        id += 1
        
        if row:
            print("Istnieje użytkownik o podanym loginie.")
        else:
            query = 'INSERT INTO users(id, imie, nazwisko, login, haslo, level) VALUES("'+str(id)+'","'+self.name+'", "'+self.surname+'", "'+self.login+'", "'+self.password+'", 1)'
            print("Executing query:", query)
            cursor.execute(query)
            conn.commit()

            app = App.get_running_app()
            app.login = self.login
            app.password = self.password
            
            
            self.manager.current = 'main_screen'
        conn.close()