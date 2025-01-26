from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button




class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)

        # Create a FloatLayout
        layout = FloatLayout()

        # Information Label
        self.info_label = Label(
            text="Your Meals:",
            font_size="25sp",
            bold=True,
            pos_hint={'center_x': 0.5, 'y': 0.7},
            size_hint=(0.8, 0.1)
        )
        layout.add_widget(self.info_label)

        # Add layout to the screen
        self.add_widget(layout)

    def update_info(self, breakfast, lunch, dinner):
        """Update the screen with the passed data."""
        self.info_label.text = (
            f"Your Meals:\n\n"
            f"Breakfast: {breakfast}\n"
            f"Lunch: {lunch}\n"
            f"Dinner: {dinner}"
        )
