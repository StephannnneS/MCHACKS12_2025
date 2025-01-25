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
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Age input
        self.age_input = TextInput(hint_text="Enter your age", multiline=False, input_filter="int")
        layout.add_widget(Label(text="Age:"))
        layout.add_widget(self.age_input)
        
        # Sex input (dropdown)
        self.sex_input = Spinner(text="Select sex", values=("Male", "Female", "Other"))
        layout.add_widget(Label(text="Sex:"))
        layout.add_widget(self.sex_input)
        
        # Height input
        self.height_input = TextInput(hint_text="Enter your height (cm)", multiline=False, input_filter="float")
        layout.add_widget(Label(text="Height (cm):"))
        layout.add_widget(self.height_input)

         # Weight input
        self.weight_input = TextInput(hint_text="Enter your weight (kg)", multiline=False, input_filter="float")
        layout.add_widget(Label(text="Weight (kg):"))
        layout.add_widget(self.weight_input)
        
        submit_button = Button(text="Submit", size_hint=(1, 0.2))
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


        self.manager.current = "home"






