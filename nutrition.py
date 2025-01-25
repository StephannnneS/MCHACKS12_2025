import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.9.0')

class calculator(App):

    def build(self):
        return BoxLayout()
    
calculator1 = calculator()
calculator1.run()


