from kivy.app import App
from kivy.uix.image import Image , AsyncImage

class MyImageApp(App):
    def build(self):
        img = Image(source="img.png",size_hint=(None,None),width=500,height=500,pos_hint={"center_x":0.5,"center_y":0.5}) # img from pc
        #img = AsyncImage(source="https://download.baps.org/Data/Sites/1/Media/DownloadableFile/Wallpapers/2011/01_january_2011f_001.jpg") #img from net
        return img
    
MyImageApp().run() 