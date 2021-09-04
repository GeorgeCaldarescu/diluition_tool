import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return FloatLayout()



if __name__ == '__main__':
    MyApp().run()