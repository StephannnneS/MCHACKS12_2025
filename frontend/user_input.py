from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from User_input_profile import *








class UserInputScreen(Screen):
    def __init__(self, **kwargs):
        super(UserInputScreen, self).__init__(**kwargs)

        with self.canvas.before:
            Color(0.9, 0.95, 1, 1)  # Light blue background
            self.bg = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_bg, pos=self._update_bg)


        # Create a vertical BoxLayout
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)


        header_label = Label(
            text="Health Goals",
            font_size="32sp",
            bold=True,
            color=(0.1, 0.4, 0.6, 1),  # Dark blue color
            size_hint=(1, 0.2)
        )
        layout.add_widget(header_label)

        
        
        


        # Sex input (dropdown)
        self.sex_input = Spinner(text="Select sex", values=("Male", "Female", "Other"),
                                 background_color=(0.8, 0.8, 0.8, 1), color=(0, 0, 0, 1))
        layout.add_widget(Label(text="Sex:", bold=True, font_size="25sp", color=(0, 0, 0, 1)))
        layout.add_widget(self.sex_input)

        
        # Age input
        self.age_input = TextInput(hint_text="Enter your age", multiline=False, input_filter="int")
        layout.add_widget(Label(text="Age:", bold=True, font_size="25sp", color=(0, 0, 0, 1)))
        layout.add_widget(self.age_input)
        
        
        # Height input
        self.height_input = TextInput(hint_text="Enter your height (cm)", multiline=False, input_filter="float")
        layout.add_widget(Label(text="Height (cm):", bold=True, font_size="25sp", color=(0, 0, 0, 1)))
        layout.add_widget(self.height_input)

         # Weight input
        self.weight_input = TextInput(hint_text="Enter your weight (kg)", multiline=False, input_filter="float")
        layout.add_widget(Label(text="Weight (kg):", bold=True, font_size="25sp", color=(0, 0, 0, 1)))
        layout.add_widget(self.weight_input)


        self.goal_weight_input = TextInput(hint_text="Enter your GOAL weight (kg)", multiline=False, input_filter="float")
        layout.add_widget(Label(text="GOAL Weight (kg):", bold=True, font_size="25sp", color=(0, 0, 0, 1)))
        layout.add_widget(self.goal_weight_input)

        
        submit_button = Button(text="Submit", size_hint=(0.4, 0.8), pos_hint={'center_x': 0.5,}, bold=True
                               ,background_color=(0.2, 0.7, 0.5, 1),  color=(1, 1, 1, 1))
        submit_button.bind(on_press=self.submit_data)
        layout.add_widget(submit_button)
        
        # Add layout to the screen
        self.add_widget(layout)



    def add_labeled_input(self, layout, label_text, hint_text, input_type, **kwargs):
        """Helper function to add a label and input field."""
        layout.add_widget(Label(text=label_text, font_size="20sp", bold=True))
        if input_type == Spinner:
            input_widget = Spinner(text=hint_text, size_hint=(1, 0.6), **kwargs)
        else:
            input_widget = input_type(hint_text=hint_text, multiline=False, size_hint=(1, 0.6), **kwargs)
        setattr(self, label_text.split(':')[0].lower() + "_input", input_widget)
        layout.add_widget(input_widget)


    def _update_bg(self, *args):
        """Update the background when the screen resizes."""
        self.bg.size = self.size
        self.bg.pos = self.pos




    def get_DRI(self, sex, age, height, weight, Goal_weight):
        user1 = User("User", height, weight, sex, age, 2, Goal_weight)
        x = user1.DRI
        return x
    



    def send_to_other_file(self, dri_data):
        """Send DRI data to the SummaryScreen."""
        summary_screen = self.manager.get_screen("result")
        summary_screen.update_dri_data(dri_data)









    def submit_data(self, instance):
        """Handles submission of user data."""
        age = int(self.age_input.text) 
        sex = self.sex_input.text
        height = float(self.height_input.text)  # Convert to float
        weight = float(self.weight_input.text)  # Convert to float
        goal_weight = float(self.goal_weight_input.text) 

        dri_data = self.get_DRI(sex, age, height, weight, goal_weight)


        home_screen = self.manager.get_screen("home")
        home_screen.update_info(age, sex, height, weight, goal_weight)

        self.send_to_other_file(dri_data)



        self.manager.current = "home"






