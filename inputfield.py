from kivy.app import App
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

Window.clearcolor=(1,1,1,1)

class loginApp(App):
    def build(self):

        layout = BoxLayout(orientation="vertical",padding=150 , spacing=20 )
        
        self.email = TextInput(text="enter your email :")
        self.password = TextInput(text="enter your password :")
        self.sub = Button(text="login",on_press=self.subtn)

        layout.add_widget(self.email)
        layout.add_widget(self.password)
        layout.add_widget(self.sub)


        return layout

    def subtn(self,obj):
        print("email :",self.email.text)
        print("password :",self.password.text)
    
loginApp().run()