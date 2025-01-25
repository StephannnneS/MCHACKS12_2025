import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.9.0')

class cal(App):

    def build(self):
        return Label(text="nutrition calculator")
    
call = cal()
call.run()