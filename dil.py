import kivy
from kivy.app import App
from kivy.lang import Builder  # this one is useful to load kv files whatever the name is
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
  agro = ObjectProperty(None)
  od = ObjectProperty(None)

  def btn(self):
      a = (float(self.od.text)*50)/float(self.agro.text)
      b = (500/a)*4
      print(b)

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