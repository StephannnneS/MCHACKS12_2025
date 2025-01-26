from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from Daily_intake import *
from kivy.app import App

class SummaryScreen(Screen):
    def __init__(self, **kwargs):
        super(SummaryScreen, self).__init__(**kwargs)

        self.layout = FloatLayout()


        self.dri_label = Label(
            text="No DRI data yet.",
            font_size="14sp",
            size_hint=(0.4, 0.8),  # Takes 40% width and 80% height
            pos_hint={'x': 0.05, 'y': 0.1},  # Positioned on the left
            
        )
        self.dri_label.bind(size=self.dri_label.setter('text_size'))  # Enable text wrapping
        self.layout.add_widget(self.dri_label)


        self.your_nutrition_label = Label(
            text="Your Nutrition:",
            font_size="15sp",
            bold=True,
            size_hint=(0.4, 0.08),  # Same size as "Recommended:"
            pos_hint={'x': 0.05, 'y': 0.75},  # Positioned slightly below
        )
        self.layout.add_widget(self.your_nutrition_label)





        self.recommended_label = Label(
            text="Recommended:",
            font_size="15sp",
            bold=True,
            size_hint=(0.2, 0.1),  # Takes 40% width and 10% height
            pos_hint={'x': 0.011, 'y': 0.6},  # Positioned slightly higher
            
        )
        self.layout.add_widget(self.recommended_label)







        # Initialize Meal object
        self.breakfast = Meal("Breakfast")
        self.current_index = 0  # Track the current dictionary being displayed
        self.data = []  # Store dictionaries
        self.extra_click_allowed = False  # Track if one extra click is allowed after processing items

        # Label to display the current dictionary
        self.data_label = Label(
            text="No data yet.",
            font_size="16sp",
            bold=True,
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
            pos_hint={'center_x': 0.5, 'y': 0.8}
        )
        self.layout.add_widget(self.weight_input)

        # Next button to process items or calculate
        self.next_button = Button(
            text="Next",
            size_hint=(0.3, 0.1),
            pos_hint={'center_x': 0.5, 'y': 0.7}
        )
        self.next_button.bind(on_press=self.next_item_or_calculate)
        self.layout.add_widget(self.next_button)

        # Label to display cumulative nutrients after all entries
        self.nutrient_label = Label(
            text="Overall Nutrition will appear here after processing.",
            font_size="14sp",
            size_hint=(0.9, 0.3),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            halign="center"
        )
        self.nutrient_label.bind(size=self.nutrient_label.setter('text_size'))  # Enable text wrapping
        self.layout.add_widget(self.nutrient_label)

        # Submit button to go to the next page
        exit_button = Button(
            text="Exit",
            size_hint=(0.2, 0.1),
            pos_hint={'x': 0.8, 'y': 0.05}  # Bottom-right corner
        )
        exit_button.bind(on_press=self.go_to_next_page)
        self.layout.add_widget(exit_button)

        self.add_widget(self.layout)

    def update_data(self, selected_data):
        # Update the data list and reset the index
        self.data = selected_data
        self.current_index = 0
        self.extra_click_allowed = False  # Reset the extra click flag

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
        elif self.current_index == len(self.data):
            # Allow one final click to calculate overall nutrition
            self.data_label.text = "Click Next to calculate overall nutrition."
            self.extra_click_allowed = True  # Allow one more click
            self.weight_input.text = ""  # Clear the input field
        else:
            # Disable the Next button when everything is done
            self.next_button.disabled = True
            self.data_label.text = "All items processed. You can submit now."

    def next_item_or_calculate(self, instance):
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
        elif self.extra_click_allowed:
            # Calculate overall nutrition on the final click
            self.calculate_overall_nutrition()
            self.extra_click_allowed = False  # Disable further clicks

    def calculate_overall_nutrition(self):
        # Ensure nutrients are populated for all foods in breakfast
        for food_item, _ in self.breakfast.foods:
            if not food_item.food_choices:
                continue
            food_item.get_nutrient_info(food_item.food_choices[0])

        # Calculate cumulative nutrients for breakfast
        self.breakfast.nutrients_counter()

        # Format and display the cumulative nutrient info
        nutrient_info = "Overall Nutrition:\n"
        for nutrient, value in self.breakfast.nutrients.items():
            unit = "N/A"
            if nutrient in self.breakfast.foods[0][0].nutrients:
                unit = self.breakfast.foods[0][0].nutrients[nutrient][1]
            nutrient_info += f"{nutrient}: {value} {unit}\n"
        self.nutrient_label.text = nutrient_info
    
    def go_to_next_page(self, instance):
        App.get_running_app().stop()






    def update_dri_data(self, dri_data):
        """Update and display DRI data."""
        formatted_dri = "\n".join([f"{key}: {value}" for key, value in dri_data.items()])
        self.dri_label.text = f"DRI Data:\n{formatted_dri}"
