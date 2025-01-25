from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Welcome Label
        label = Label(
            text="Welcome to the Home Screen!",
            font_size='24sp',
            bold=True
        )
        layout.add_widget(label)
        
        self.add_widget(layout)





