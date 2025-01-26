from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from Daily_intake import *


class SummaryScreen(Screen):
    def __init__(self, **kwargs):
        super(SummaryScreen, self).__init__(**kwargs)

        layout = FloatLayout()

        # Initialize Meal object
        self.breakfast = Meal("Breakfast")
        self.layout = FloatLayout()
        self.current_index = 0  # Track the current dictionary being displayed
        self.data = []  # Store dictionaries

        # Label to display the current dictionary
        self.data_label = Label(
            text="No data yet.",
            font_size="16sp",
            bold = True,
            size_hint=(0.9, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.9},
            halign="left"
        )
        self.layout.add_widget(self.data_label)

        # Input field to take user input for weight
        self.weight_input = TextInput(
            hint_text="Enter weight in grams...",
            multiline=False,
            size_hint=(0.8, 0.1),
            pos_hint={'center_x': 0.5, 'y':0.8}
        )
        self.layout.add_widget(self.weight_input)

        # Button to save input and move to the next dictionary
        self.next_button = Button(
            text="Next",
            size_hint=(0.3, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )
        self.next_button.bind(on_press=self.next_item)
        self.layout.add_widget(self.next_button)

        # Label to display cumulative nutrients after all entries
        self.nutrient_label = Label(
            text="Nutrient info will appear here after all items are processed.",
            font_size="14sp",
            size_hint=(0.7, 0.2),
            pos_hint={'center_x': 0.5, 'center_y': 0.45},
            halign = "center"
        )
        self.nutrient_label.bind(size=self.nutrient_label.setter('text_size'))  # Enable text wrapping
        self.layout.add_widget(self.nutrient_label)

        self.add_widget(self.layout)



        submit_button = Button(
            text="Next",             # Button label
            size_hint=(0.2, 0.1),      # Button size (adjust as needed)
            pos_hint={'right': 1, 'y': 0}  # Bottom-right corner
        )
        submit_button.bind(on_press=self.go_to_next)
        layout.add_widget(submit_button)

        

        



    def go_to_next(self, instance):
        # Get the ScreenManager and navigate to the SummaryScreen
        screen_manager = self.manager
        summary_screen = screen_manager.get_screen("calculator1")
        summary_screen.update_data(self.selected_food_data)
        screen_manager.current = "calculator1"





    def update_data(self, selected_data):
        # Update the data list and reset the index
        self.data = selected_data
        self.current_index = 0

        # Display the first dictionary
        self.display_current_item()

    def display_current_item(self):
        # Display the current dictionary
        if self.current_index < len(self.data):
            current_data = self.data[self.current_index]
            self.data_label.text = (
                f"Index: {current_data['index']}, "
                f"Value1: {current_data['value1']}, "
                f"Value2: {current_data['value2']}"
            )
            self.weight_input.text = ""  # Clear the input field
        else:
            # Ensure nutrients are populated for all foods in breakfast
            for food_item, _ in self.breakfast.foods:
                if not hasattr(food_item, 'nutrients') or not food_item.nutrients:
                    if food_item.food_choices:
                        food_item.get_nutrient_info(food_item.food_choices[0])

            # Process and display cumulative nutrients for breakfast
            self.breakfast.nutrients_counter()
            nutrient_info = "Breakfast Nutrients:\n"
            for nutrient, value in self.breakfast.nutrients.items():
                nutrient_info += f"{nutrient}: {value}\n"
            self.nutrient_label.text = nutrient_info

            # Clear the data label and input field
            self.data_label.text = "All items processed."
            self.weight_input.text = ""

    def next_item(self, instance):
        if self.current_index < len(self.data):
            # Get the weight input from the user
            weight = self.weight_input.text.strip()
            if weight.isdigit():
                weight = int(weight)
                current_data = self.data[self.current_index]
                value1 = current_data["value1"]
                value2 = current_data["value2"]

                # Add food to the Meal object using the provided weight
                self.breakfast.add_food(value1, value2, weight)
            else:
                print("Invalid weight. Please enter a numeric value.")

        # Move to the next dictionary
        self.current_index += 1
        self.display_current_item()
