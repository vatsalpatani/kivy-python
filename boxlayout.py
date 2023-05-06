from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor=(0,9,0,1)
Window.size=(300,500)

class ButtonApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical",spacing=10,padding=10)

        btn1 = Button(text="btn1",pos_hint={"center_x":0.5,"center_y":0.5}, font_size=30 , on_press=self.btn1_prs)
        btn2 = Button(text="btn2",pos_hint={"center_x":0.5,"center_y":0.5}, font_size=30 , on_press=self.btn2_prs)
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)

        return layout

    def btn1_prs(self,btn):
        print("button1 click")

    def btn2_prs(self,btn):
        print("button2 click")


ButtonApp().run() 