from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle

class ByeScreen(Screen):
    def __init__(self, **kwargs):

        super(ByeScreen, self).__init__(**kwargs)

        with self.canvas.before:
            Color(0.1, 0.6, 0.8, 1)  # Light blue background
            self.bg = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_bg, pos=self._update_bg)


        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)



        label1 = Label(
            text="Health Care App",
            bold = True,
            font_size='40sp',
            color=(1, 1, 1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )


        button = Button(
            text='Get Started',
            size_hint=(0.3, 0.1),
            bold = True,
            background_color=(0.2, 0.8, 0.6, 1),  # Teal background
            color=(1, 1, 1, 1),  # White text
            pos_hint={'center_x': 0.5, 'center_y': 0.2}
        )
        button.bind(on_press=self.switch_to_second_screen)

        layout.add_widget(label1)
        layout.add_widget(button)
        self.add_widget(layout)


    def _update_bg(self, *args):
        """Update the background when the window resizes."""
        self.bg.size = self.size
        self.bg.pos = self.pos

    def switch_to_second_screen(self, instance):
        self.manager.current = 'user_input'