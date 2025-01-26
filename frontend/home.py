from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
 

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        with self.canvas.before:
            Color(0.1, 0.6, 0.8, 1)  # Light blue background
            self.bg = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_bg, pos=self._update_bg)


        self.layout = BoxLayout(orientation='vertical', padding=[20, 100, 20, 20], spacing=10)

    
        


        self.welcome_label = Label(
            text="Personal Information",
            font_size='40sp',
            bold=True,
            halign="center",
            valign="top"
        )
            
    
        self.welcome_label.bind(size=self.welcome_label.setter('text_size'))
        self.layout.add_widget(self.welcome_label)
        

        self.info_label = Label(
            text="info here",
            font_size='24sp',  # Standard size for user info
            halign="center",
            bold = True,
            valign="middle"
        )
        self.info_label.bind(size=self.info_label.setter('text_size'))  # Enable text wrapping
        self.layout.add_widget(self.info_label)

        button = Button(
            text='Start Calculating',
            size_hint=(0.3, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        button.bind(on_press=self.switch_to_calculator)
        self.layout.add_widget(button)
        self.add_widget(self.layout)


        button_back = Button(
            text='Go Back',
            size_hint=(0.3, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        button_back.bind(on_press=self.switch_to_user_input)
        self.layout.add_widget(button_back)

    
    def switch_to_calculator(self, instance):
            self.manager.current = 'calculator' 


    def switch_to_user_input(self, instance):
        """Switch to the UserInputScreen."""
        self.manager.current = 'user_input'


    def _update_bg(self, *args):
        """Update the background when the window resizes."""
        self.bg.size = self.size
        self.bg.pos = self.pos





    def update_info(self, age, sex, height, weight, goal_weight):
        """Update the screen with user-provided data."""
        self.info_label.text = (
            f"Age: {age}\n"
            f"Sex: {sex}\n"
            f"Height: {height} cm\n"
            f"Weight: {weight} kg\n"
            f"GOAL Weight: {goal_weight} kg"
        )







