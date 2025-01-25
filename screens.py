from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        layout = BoxLayout()

        label = Label(
            text = "Welcome!",
            font_size = '32sp',  
            bold = True          
        )
        layout.add_widget(label)
        self.add_widget(layout)


class InputScreen(Screen):
    def __init__(self, **kwargs):
        super(InputScreen, self).__init__(**kwargs)
        layout = BoxLayout()
        layout.add_widget(Label(text="Calculator Screen"))
        self.add_widget(layout)