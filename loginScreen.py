from kivy.app import App,  Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

import sqlite3

Builder.load_file("loginScreen.kv")

class LoginScreen(Screen):
    bg_color = (0.9607843137254902, 0.8392156862745098, 0.7294117647058823, 1.0)
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

    # def clear_text(self, instance, value):
    #     if instance.text == 'Login' or instance.text == 'Haslo':
    #         instance.text = ''

    def check_login(self, instance):

        self.login = self.ids.inputLogin.text
        self.password = self.ids.inputPassword.text

        conn = sqlite3.connect('mypatch.sqlite')
        cursor = conn.cursor()
        cursor.execute('SELECT haslo FROM users WHERE login = ?', (self.login,))
        row = cursor.fetchone()
        if row:
            db_password = row[0]

            if self.password == db_password:
                self.ids.response.text = "Haslo poprawne. Logowanie udane!"

                app = App.get_running_app()
                app.login = self.login
                app.password = self.password
                
                self.manager.current = 'main_screen'
            else:
                self.ids.response.text ="Nieprawidlowe haslo. Logowanie nieudane."
        else:
            self.ids.response.text ="Uzytkownik o podanym loginie nie istnieje."
        conn.close()