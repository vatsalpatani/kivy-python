from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.clearcolor=(0,9,0,1)
Window.size=(300,500)

class ButtonApp(App):
    def build(self):
        layout = GridLayout(rows=2)

        btn1 = Button(text="btn1")
        btn2 = Button(text="btn2")
        btn3 = Button(text="btn3")
        btn4 = Button(text="btn4")
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout



ButtonApp().run() 