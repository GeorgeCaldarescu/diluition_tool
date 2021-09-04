import kivy
from kivy.app import App
from kivy.uix.label import Label  # to be able to add labels
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


# create a class that contain all the desing elements
class MyGrid(GridLayout):
    def __init__(self, **kwargs): # is used to take infinite arguments
        super(MyGrid, self).__init__(**kwargs)
        
        # create another layout inside the main layout to center the button
        self.inside = GridLayout()
        self.inside.cols = 2
        self.cols = 1
        
        self.inside.add_widget(Label(text = "First Name: "))
        self.firstName = TextInput(multiline = False)
        self.inside.add_widget(self.firstName)

        self.inside.add_widget(Label(text = "Last Name: "))
        self.lastName = TextInput(multiline = False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text = "Email: "))
        self.email = TextInput(multiline = False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text = "Submit", font_size = 40)
        self.submit.bind(on_press = self.pressed)
        self.add_widget(self.submit)
    
    
    def pressed(self, instance):    #this function is called when the button is pressed
        name = self.firstName.text
        last = self.lastName.text   # is how to store waht is inside the ui
        email = self.email.text

        print("name:", name, "last name:", last, "email:", email)

        # to clean the form
        self.firstName.text = ""
        self.lastName.text = "" 
        self.email.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()  # run is a method already in App to configure all the graphic and run the app