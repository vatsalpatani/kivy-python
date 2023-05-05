from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        btn = Button(text="click me",size_hint=(0.3 ,0.2),pos_hint={"center_x":0.5,"center_y":0.5}, font_size=30 , on_press=self.btn_prs)
        return btn

    def btn_prs(self,btn):
        print("button click")


ButtonApp().run() 