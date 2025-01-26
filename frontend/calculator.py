from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button





class CalculatorScreen(Screen):
    def __init__(self, **kwargs):
        super(CalculatorScreen, self).__init__(**kwargs)
        
        # Create a vertical BoxLayout
        layout = FloatLayout()


        breakfast_label = Label(
            text="Breakfast Menu",
            font_size="25sp",
            bold=True,
            pos_hint={'center_x': 0.5, 'y': 0.7},  # Position near the top
            size_hint=(0.6, 0.1)
        )
        layout.add_widget(breakfast_label)

        # Breakfast Input
        self.breakfast_input = TextInput(
            hint_text="What did you have for breakfast? (e.g. Cereal, Banana, Milk)",
            multiline=False,
            size_hint=(0.6, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.6}
        )
        layout.add_widget(self.breakfast_input)

        
        lunch_label = Label(
            text="Lunch Menu",
            font_size="25sp",
            bold=True,
            pos_hint={'center_x': 0.5, 'y': 0.5},
            size_hint=(0.6, 0.1)
        )
        layout.add_widget(lunch_label)




        # Lunch Input
        self.lunch_input = TextInput(
            hint_text="What did you have for lunch?",
            multiline=False,
            size_hint=(0.6, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.4}
        )
        layout.add_widget(self.lunch_input)




        
       # Dinner Label
        dinner_label = Label(
            text="Dinner Menu",
            font_size="25sp",
            bold=True,
            pos_hint={'center_x': 0.5, 'y': 0.3},
            size_hint=(0.6, 0.1)
        )
        layout.add_widget(dinner_label)


        # Dinner Input
        self.dinner_input = TextInput(
            hint_text="What did you have for dinner?",
            multiline=False,
            size_hint=(0.6, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.2}
        )
        layout.add_widget(self.dinner_input)


        # Submit Button
        submit_button = Button(
            text="Submit",
            size_hint=(0.4, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.1},
            bold=True
        )
        submit_button.bind(on_press=self.submit_data)
        layout.add_widget(submit_button)

        # Add layout to the screen
        self.add_widget(layout)



    def submit_data(self, instance):
        """Handles submission of user data and passes it to the next screen."""
        breakfast = self.breakfast_input.text
        lunch = self.lunch_input.text
        dinner = self.dinner_input.text

        # Access the next screen and pass the data
        next_screen = self.manager.get_screen("result")
        next_screen.update_info(breakfast, lunch, dinner)

        # Switch to the next screen
        self.manager.current = "result"


    


        

        