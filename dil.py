import kivy
from kivy.app import App
from kivy.lang import Builder  # this one is useful to load kv files whatever the name is
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")
 



class MyApp(App):
    def build(self):
        return kv



if __name__ == '__main__':
    MyApp().run()