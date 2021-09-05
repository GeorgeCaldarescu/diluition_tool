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

    # clean the form need to think about. maybe a can make a reset button with a clean function inside
        

class ThirdWindow(Screen):
    conc = ObjectProperty(None)
    odB = ObjectProperty(None)

    def btnBrad(self):
        fConc = float(self.conc.text)
        fOd = float(self.odB.text)*10
        
        a = (fOd * 0.8847 + 0.128) * 1000
        b = (fConc/a) * 1000
        print("Amount of protein to take to have", fConc,"ng is", b)
        print("You need to add", b/5, "SDS before load the samples")    
        


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")



class MyApp(App):
        
    def build(self):
        return kv



if __name__ == '__main__':
    MyApp().run()