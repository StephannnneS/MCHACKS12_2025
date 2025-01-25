import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from user_input import UserInputScreen

kivy.require('1.9.0')


class MyScreenManager(ScreenManager):
    pass


class NutritionApp(App):
    def build(self):
        sm = MyScreenManager()
        
        # Add the UserInputScreen to the ScreenManager
        sm.add_widget(UserInputScreen(name="user_input"))
        
        return sm
    

if __name__ == "__main__":
    NutritionApp().run()

#hi






