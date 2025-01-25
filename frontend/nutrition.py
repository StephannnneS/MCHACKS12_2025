import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from user_input import UserInputScreen
from home import HomeScreen
from welcome import WelcomeScreen


kivy.require('1.9.0')




class MyScreenManager(ScreenManager):
    pass




class NutritionApp(App):
    def build(self):
        sm = MyScreenManager()

        sm.add_widget(WelcomeScreen(name="welcome"))

        sm.add_widget(UserInputScreen(name="user_input"))


        sm.add_widget(HomeScreen(name="home"))


        return sm


if __name__ == "__main__":
    NutritionApp().run()