from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from User_input_profile import *
from kivy.uix.popup import Popup
from Daily_intake import *
from kivy.uix.spinner import Spinner
from functools import partial


class GraphScreen(Screen):
    def __init__(self, **kwargs):
        super(GraphScreen, self).__init__(**kwargs)
        self.nutrient_info = ""  # Placeholder for nutrient data

    def on_enter(self):
        print("Received nutrition info:", self.nutrient_info)