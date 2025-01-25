from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        label1 = Label(
            text="Health Care App",
            font_size='40sp',
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )

        button = Button(
            text='Get Started',
            size_hint=(0.3, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.2}
        )
        button.bind(on_press=self.switch_to_second_screen)

        layout.add_widget(label1)
        layout.add_widget(button)
        self.add_widget(layout)

    def switch_to_second_screen(self, instance):
        self.manager.current = 'user_input'  
