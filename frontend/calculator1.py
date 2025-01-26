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


class CalculatorScreen1(Screen):
    def __init__(self, **kwargs):


        super(CalculatorScreen1, self).__init__(**kwargs)

        self.selected_food_data = [] 
        
        # Create a vertical BoxLayout
        layout = FloatLayout()


        breakfast_label = Label(
            text="Breakfast Menu",
            font_size="25sp",
            bold=True,
            pos_hint={'center_x': 0.5, 'y': 0.9},  # Position near the top
            size_hint=(0.6, 0.1)
        )
        layout.add_widget(breakfast_label)
        self.add_widget(layout)