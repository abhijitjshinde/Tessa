from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
import time
kv = '''
<Details>:
    adaptive_height: True
    # size: 20, 80
    spacing: dp(10)
    MDSpinner:
        size_hint: (None, None)
        size: (dp(46), dp(46))
        pos_hint: {'x': 1, 'y': .5}
        active: True
        palette:
            [248/255, 178/255, 45/255, 1],[222/255, 38/255, 59/255, 1],[242/255, 129/255, 42/255, 1],[0.8784313725490196, 0.9058823529411765, 0.40784313725490196, 1],
    MDLabel:
        text: " Collecting Data...."
        pos_hint: {'x': 1, 'y': .5}
        

            
'''
class Details(MDBoxLayout):
    Builder.load_string(kv)

class Dialog_case(MDBoxLayout):  
    Spinnerk =  None   
    def open_dlg(self):
        Spinnerk = None
        
        self.Spinnerk = MDDialog(
        # text="This will reset your device to its default factory settings.",
        type= "custom",
        content_cls=Details()
        )
        self.Spinnerk.open()
       
    def close_dlg(self):
        self.Spinnerk.dismiss()
