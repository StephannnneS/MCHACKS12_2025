from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class ChoicePopup(Popup):
    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.callback = callback  # Callback function to return value
        self.title = 'Select an Option'
        self.size_hint = (0.5, 0.3)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        label = Label(text="Choose an option:", size_hint=(1, 0.3))
        layout.add_widget(label)

        # Add buttons for choices
        self.choices = ["Option 1", "Option 2", "Option 3"]
        for choice in self.choices:
            btn = Button(text=choice, size_hint=(1, 0.3))
            btn.bind(on_release=lambda btn: self.select_choice(btn.text))
            layout.add_widget(btn)

        self.add_widget(layout)

    def select_choice(self, choice):
        """Pass the selected choice to the callback function."""
        self.callback(choice)  # Return choice to the calling function
        self.dismiss()  # Close the popup

class TestApp(App):
    def build(self):
        self.selected_options = []  # Store selected options here

        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.label = Label(text="Click the button to choose an option.")
        main_layout.add_widget(self.label)

        open_popup_btn = Button(
            text="Open Popup", size_hint=(0.2, 0.1), pos_hint={'center_x': 0.5}
        )
        open_popup_btn.bind(on_release=self.show_popup)
        main_layout.add_widget(open_popup_btn)

        # Scrollable list at bottom left
        self.list_layout = BoxLayout(orientation='vertical', spacing=5, size_hint=(0.5, 0.3))
        self.list_label = Label(text="Selected Options:", size_hint_y=None, height=30)
        self.list_scroll = ScrollView(size_hint=(1, 1))
        self.list_content = BoxLayout(orientation='vertical', size_hint_y=None)
        self.list_scroll.add_widget(self.list_content)

        self.list_layout.add_widget(self.list_label)
        self.list_layout.add_widget(self.list_scroll)
        main_layout.add_widget(self.list_layout)

        return main_layout

    def show_popup(self, instance):
        popup = ChoicePopup(self.set_selected_option)
        popup.open()

    def set_selected_option(self, choice):
        """Add the selected option to the list."""
        formatted_choice = f"\u2022 {choice}"
        self.selected_options.append(formatted_choice)
        self.update_list()

    def update_list(self):
        """Update the displayed list of selected options."""
        self.list_content.clear_widgets()
        for option in self.selected_options:
            self.list_content.add_widget(Label(text=option, size_hint_y=None, height=30))

if __name__ == '__main__':
    TestApp().run()