from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout
from kivy.core.window import Window

Window.clearcolor=(0,9,0,1)
Window.size=(300,500)

class ButtonApp(App):
    def build(self):
        layout = PageLayout()

        btn1 = Button(text="btn1")
        btn2 = Button(text="btn2")
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)

        return layout


ButtonApp().run() 