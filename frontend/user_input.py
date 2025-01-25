from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner








class UserInputScreen(Screen):
    def __init__(self, **kwargs):
        super(UserInputScreen, self).__init__(**kwargs)
        
        # Create a vertical BoxLayout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=5)


        # Sex input (dropdown)
        self.sex_input = Spinner(text="Select sex", values=("Male", "Female", "Other"))
        layout.add_widget(Label(text="Sex:", bold=True, font_size="25sp"))
        layout.add_widget(self.sex_input)

        
        # Age input
        self.age_input = TextInput(hint_text="Enter your age", multiline=False, input_filter="int")
        layout.add_widget(Label(text="Age:", bold=True, font_size="25sp"))
        layout.add_widget(self.age_input)
        
        
        # Height input
        self.height_input = TextInput(hint_text="Enter your height (cm)", multiline=False, input_filter="float")
        layout.add_widget(Label(text="Height (cm):", bold=True, font_size="25sp"))
        layout.add_widget(self.height_input)

         # Weight input
        self.weight_input = TextInput(hint_text="Enter your weight (kg)", multiline=False, input_filter="float")
        layout.add_widget(Label(text="Weight (kg):", bold=True, font_size="25sp"))
        layout.add_widget(self.weight_input)


        self.goal_weight_input = TextInput(hint_text="Enter your GOAL weight (kg)", multiline=False, input_filter="float")
        layout.add_widget(Label(text="GOAL Weight (kg):", bold=True, font_size="25sp"))
        layout.add_widget(self.goal_weight_input)

        
        submit_button = Button(text="Submit", size_hint=(2, 0.7), bold=True)
        submit_button.bind(on_press=self.submit_data)
        layout.add_widget(submit_button)
        
        # Add layout to the screen
        self.add_widget(layout)

    def submit_data(self, instance):
        """Handles submission of user data."""
        age = self.age_input.text
        sex = self.sex_input.text
        height = self.height_input.text
        weight = self.weight_input.text
        goal_weight = self.goal_weight_input.text


        home_screen = self.manager.get_screen("home")
        home_screen.update_info(age, sex, height, weight, goal_weight)



        self.manager.current = "home"






