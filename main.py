#--[Start platform specific code]
"""This code to detect it's Android or not 
if it's not android than app window size change in android phone size"""
from kivy.utils import platform
 
if platform != 'android':
    from kivy.config import Config
    Config.set("graphics","width",360 )
    Config.set("graphics","height",640)
#--[End platform specific code]

#--[Start Soft_Keyboard code ]
"""code for android keyboard. when in android keyboard show textbox 
automatic go to top of keyboard so user can see when he type msg"""
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore

Window.keyboard_anim_args = {"d":.2,"t":"linear"}
Window.softinput_mode = "below_target"
#--[End Soft_Keyboard code ]
 
# from libs.uix.baseclass.chat_room import Chat_Room_Screen 
from libs.uix.baseclass.forgot import Forgot_Screen
from libs.uix.baseclass.home import Home_Screen
from libs.uix.baseclass.login import Login_Screen
from libs.uix.baseclass.landing_page import Landing_Screen
from libs.uix.baseclass.waiting import Waiting_room
from libs.uix.baseclass.memberadd import Member_add #admin screen
from libs.uix.baseclass.verification import Verification_Screen
from libs.uix.baseclass.signup import Signup_Screen
from libs.uix.baseclass.root import Root
from libs.uix.baseclass.transactions import Transactions
from libs.uix.baseclass.holdings import Holdings
from libs.uix.baseclass.memberholding import Member_holdings
from libs.uix.baseclass.registergroup import Registergroup
from libs.uix.baseclass.groupselection import GroupSelection
from libs.uix.baseclass.notification import Notifications
from libs.uix.baseclass.change_password import ChangePassword
from libs.uix.baseclass.profile import Profile_Screen

# from libs.uix.baseclass.profile import Profile_Screen
from main_imports import ImageLeftWidget, MDApp, TwoLineAvatarListItem
# from kivy.storage.jsonstore import JsonStore
from kivy.factory import Factory
from kivy.network.urlrequest import UrlRequest
# Other Imports
import json
# import jsonpatch
import os
# import sys
# import requests
# import threading
# import certifi as cfi
# from functools import partial

r = Factory.register
_class = 'ChatListItem'
module = 'libs.applibs.list'
r(_class, module=module)
class PMcA(MDApp):
    """
    Hamster App start from here this class is root of app.
    in kivy (.kv) file when use app.method_name app is start from here
    """
    internet = 1
    selected_group = "Tessa"
    def __init__(self, **kwargs):
        super(PMcA, self).__init__(**kwargs)
        # Global Variables
        self.APP_NAME = "PMcA"
        self.COMPANY_NAME = "PMcA.org"
        self.theme_cls.primary_palette = "Orange"
        
    def build(self):
        """
        This method call before on_start() method so anything
        that need before start application all other method and code 
        write here.
        """
        # self.theme_cls.primary_palette = "Blue"
        # self.theme_cls.primary_hue = "500"

        # self.theme_cls.accent_palette = "Amber"
        # self.theme_cls.accent_hue = "500"

        # self.theme_cls.theme_style = "Light"
    
        self.screen_manager = Root()
        self.screen_manager.add_widget(Landing_Screen())
        self.screen_manager.add_widget(Login_Screen())
        self.screen_manager.add_widget(Signup_Screen())
        self.screen_manager.add_widget(Forgot_Screen())
        self.screen_manager.add_widget(Verification_Screen())
        self.screen_manager.add_widget(Waiting_room())
        self.screen_manager.add_widget(Home_Screen())
        self.screen_manager.add_widget(Member_add())
        self.screen_manager.add_widget(Transactions())
        self.screen_manager.add_widget(Holdings())
        self.screen_manager.add_widget(Member_holdings())
        self.screen_manager.add_widget(Registergroup())
        self.screen_manager.add_widget(GroupSelection())
        self.screen_manager.add_widget(Notifications())
        self.screen_manager.add_widget(ChangePassword())
        self.screen_manager.add_widget(Profile_Screen())        

        return self.screen_manager
    def on_start(self):
        file_path = 'Json_Files/userinfo.json'       
        if os.path.getsize(file_path) != 0:
            # with open(file_path) as f:
            #     data = json.load(f)
                # key, value = list(data.items())[0]
                # user_type = data["user_info"]["user_type"]
                # self.screen_manager.get_screen("home").usertype = user_type
                # self.screen_manager.get_screen("holdings").usertype = user_type
                # self.screen_manager.get_screen("admin").usertype = user_type
                # self.screen_manager.get_screen("profile").usertype = user_type
                # self.screen_manager.get_screen("notifications").usertype = user_type
                # self.screen_manager.get_screen("transactions").usertype = user_type
                # print(data["user_info"]["user_type"])
            self.screen_manager.change_screen("groupselection")
        else:
            self.screen_manager.change_screen("land")
    
        
if __name__ == "__main__":
    # Start application from here. 
    PMcA().run() 