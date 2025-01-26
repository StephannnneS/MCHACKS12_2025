from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from User_input_profile import *







class CalculatorScreen(Screen):
    def __init__(self, **kwargs):
        super(CalculatorScreen, self).__init__(**kwargs)
        
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



        # First Input Field
        self.input1 = TextInput(
            hint_text="Value 1",
            multiline=False,
            size_hint=(0.25, 0.08),  # Smaller size for the input
            pos_hint={'center_x': 0.35, 'y': 0.7}  # Positioned on the left
        )
        layout.add_widget(self.input1)

        # Second Input Field
        self.input2 = TextInput(
            hint_text="Value 2",
            multiline=False,
            size_hint=(0.25, 0.08),  # Smaller size for the input
            pos_hint={'center_x': 0.65, 'y': 0.7}  # Positioned on the right
        )
        layout.add_widget(self.input2)


        search_button = Button(
        text="Search",             # Button label
        size_hint=(0.1, 0.08),     # Button size (adjust as needed)
        pos_hint={'center_x': 0.875, 'y': 0.7}  # Position next to the second input field
        )   
        layout.add_widget(search_button)


        submit_button = Button(
            text="Submit",             # Button label
            size_hint=(0.2, 0.1),      # Button size (adjust as needed)
            pos_hint={'right': 1, 'y': 0}  # Bottom-right corner
        )
        layout.add_widget(submit_button)






    def get_the_food(x,y):
        meal = Food(x,y)
        choices = meal.food_choices

        

        

    


        

        