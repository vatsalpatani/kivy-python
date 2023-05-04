from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor=(1,1,0,1)

class myApp(App):
    def build(self):
        l1 = Label(text="Hello World",font_size=90,bold=True,italic=True,color=(1,0,0,1)) 
        return l1
    
myApp().run()