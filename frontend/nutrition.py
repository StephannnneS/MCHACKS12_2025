from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class MyLayout(BoxLayout):
    def __init__(self):
        super().__init__()
        self.button=Button(text='Get Started')
        self.button.bind(on_press=function)


class MyApp(App):
    def build(self):
        layout=FloatLayout()
        label1=Label(text="Health Care App",pos_hint={'center_x':0.5,'center_y':0.7},font_size='40sp')
        layout.add_widget(label1)
        return layout      
       
   
if __name__=='__main__':
    MyApp().run()
