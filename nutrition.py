import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens import WelcomeScreen, InputScreen

kivy.require('1.9.0')


class MyScreenManager(ScreenManager):
    pass


class CalculatorApp(App):
    def build(self):
        sm = MyScreenManager()  
        
        sm.add_widget(WelcomeScreen(name="welcome"))  # Assign a unique name to the screen
        sm.add_widget(InputScreen(name="calculator"))
        return sm  # Return the ScreenManager as the root widget
    

if __name__ == "__main__":
    CalculatorApp().run()






