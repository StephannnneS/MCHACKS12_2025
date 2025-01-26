from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from User_input_profile import *
from kivy.uix.popup import Popup
from Daily_intake import *







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
        search_button.bind(on_press=self.show_food_popup)
        layout.add_widget(search_button)


        submit_button = Button(
            text="Submit",             # Button label
            size_hint=(0.2, 0.1),      # Button size (adjust as needed)
            pos_hint={'right': 1, 'y': 0}  # Bottom-right corner
        )
        layout.add_widget(submit_button)

        


    def get_the_food(self, x, y):
        meal = Food(x, y)
        return meal.food_choices


    def show_food_popup(self, instance):
        # Get input values
        value1 = self.input1.text
        value2 = self.input2.text

        # Get the food list
        food_tuple = self.get_the_food(value1, value2)

        if not food_tuple:
            food_tuple = ("No food items found",)

        # Prepare the popup content
        content = FloatLayout()

        food_list_str = "\n".join([str(item) for item in food_tuple[1:]])

        # Food Label
        food_label = Label(
            text=f"Here are the food items:\n{food_list_str}",
            size_hint=(0.8, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.7},  # Positioned at the top center
            halign='center',
            valign='top'
        )
        content.add_widget(food_label)

        # Close Button
        close_button = Button(
            text="Close",
            size_hint=(0.4, 0.2),  # Smaller button
            pos_hint={'center_x': 0.5, 'center_y': 0.2}  # Positioned at the bottom center
        )
        content.add_widget(close_button)

        # Create the popup
        popup = Popup(
            title="Food List",
            content=content,
            size_hint=(0.8, 0.5),
            auto_dismiss=False
        )

        # Bind close button to dismiss the popup
        close_button.bind(on_press=popup.dismiss)

        # Open the popup
        popup.open()
