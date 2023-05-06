from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

Window.clearcolor=(0,9,0,1)
Window.size=(300,500)

class ButtonApp(App):
    def build(self):
        layout = FloatLayout(size=(200,200))

        btn1 = Button(text="btn1")
        btn2 = Button(text="btn2",size_hint=(None,None),width=40)
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)

        return layout


ButtonApp().run() 