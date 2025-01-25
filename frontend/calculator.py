from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button










class CalculatorScreen(Screen):
    def __init__(self, **kwargs):
        super(CalculatorScreen, self).__init__(**kwargs)
        
        # Create a vertical BoxLayout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=5)


        # Breakfast input 
        self.breakfast_input = TextInput(hint_text="What did you have for breakfast?",multiline=False)
        layout.add_widget(Label(text="Breakfast Menu", bold=True, font_size="25sp"))
        layout.add_widget(self.breakfast_input)

        
       # Lunch input
        self.lunch_input = TextInput(hint_text="What did you have for lunch?", multiline=False)
        layout.add_widget(Label(text="Lunch Menu:", bold=True, font_size="25sp"))
        layout.add_widget(self.lunch_input)
        
        
       #Dinner input
        self.dinner_input = TextInput(hint_text="What did you have for dinner?", multiline=False)
        layout.add_widget(Label(text="Dinner Menu", bold=True, font_size="25sp"))
        layout.add_widget(self.dinner_input)

        self.add_widget(layout)

        