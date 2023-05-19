from main_imports import MDScreen,MDDialog,MDDropdownMenu,MDFlatButton,FloatLayout,dp,BoxLayout
from libs.applibs import utils
import datetime
import time
utils.load_kv("memberadd.kv")

class Content(BoxLayout):
    pass
class Member_add(MDScreen):
    selected_group = ""
    usertype="Member"
    def call_pre(self):
        print("Inside pre Call")
        self.parent.get_screen("signup").generate_client_id()

    def add_member(self,Name,Phone):
        print(Name,Phone,self.selected_group)
        if Name != "" and Phone!= "":
            self.parent.get_screen("signup").Sign_me_up(Name=Name,Phone=Phone,Password="abc",Confirm_pass="abc",gcode=self.selected_group,is_admin_adding=True)
            # self.image_dialog() 
        else:
            print("Please fill data ")
    
    def image_dialog(self):
        self.dialogs = MDDialog(
            text ="Test image pop up",
            # size_hint=(.45, None),
            auto_dismiss=True,
            md_bg_color= "#FFFFFF",
            type="custom",
            content_cls=Content(),
            buttons=[
            # MDFlatButton(
            #     text= "Cancel",
            #     # md_bg_color= (248/255, 178/255, 45/255,1),
            #     on_release= lambda x:self.dialogs.dismiss() 
            # ),
            MDFlatButton(
                text= "Continue",
                md_bg_color= (242/255, 129/255, 42/255,1),
                on_release= lambda x: self.dialogs.dismiss()
            )
        ],
        )
        # MDDialog(
        #     text="Discard draft?",
        #     content=Image(source='assets\img\icon_LS.png',        
        # )
        self.dialogs.open()
    
    def change(self):
        self.dialogs.dismiss() 
        self.parent.change_screen("transactions")
    # Member list section
    New_data_list = []
    def on_enter(self):
        self.call_pre()
        for i in range(20):
            name = "Member "+str(i)
            self.all_chats(name,"Member")
    
    def remove_member(self,text):
        print(text)
        self.Remove_member_name = text
        self.dialogs = MDDialog(
            title = "Delete Member?",
            text ="This will Delete "+self.Remove_member_name+" permanatly from Foundation and discard Due amount and further transactions.",
            # size_hint=(.45, None),
            auto_dismiss=True,
            # type="custom",
            # content_cls=Content(),
            buttons=[
            MDFlatButton(
                text= "Cancel",
                # md_bg_color= (248/255, 178/255, 45/255,1),
                on_release= lambda x:self.dialogs.dismiss() 
            ),
            MDFlatButton(
                text= "Delete",
                md_bg_color= (242/255, 129/255, 42/255,1),
                on_release= lambda x: self.update(self.Remove_member_name)
            )
        ],
        )
        # MDDialog(
        #     text="Discard draft?",
        #     content=Image(source='assets\img\icon_LS.png',        
        # )
        self.dialogs.open()
        
    def update(self,text):
        # This function will remove the member from the UI for now 
        self.dialogs.dismiss()
        # print(self.New_data_list)
        user_data = [item for item in self.New_data_list if item['text'] != text]
        print(user_data)
        self.ids.rv.data = user_data
    
    def all_chats(self,name,latest_msg):
        """
        All Chat that show in home chat tab. all chat are added by 
        this method. it will use in differe t in future.
        """ 
        
        user_data = {
                "text": name,
                "secondary_text": latest_msg,                
                "image": "assets\img\\blank_profile.png"                
            }
        # pre_data = {'name':name,'path':path}
        self.ids.rv.data.append(user_data)
        self.New_data_list.append(user_data)

    # Add Record page section
    member_list = ["Abhijit","Sid","Ajit","RAJU","Laksha"]
    txn_type = ["Credit","Debit"]
    category = ["Monthly","Loan","Event"]
    txn_mode = ["Online","Offline"]
    def open_menu(self,drop):
        
        if drop == "member":
            menu_id = self.ids.member
            self.menu_items = [
                {
                    "viewclass": "OneLineListItem",                
                    "text": name,
                    "on_release": lambda x = name : self.set_item(x,drop),
                }for name in self.member_list
            ]
        elif drop == "txn_type":
            menu_id = self.ids.txn_type
            self.menu_items = [
                {
                    "viewclass": "OneLineListItem",                
                    "text": name,
                    "on_release": lambda x = name : self.set_item(x,drop),
                }for name in self.txn_type
            ]
        elif drop == "category":
            menu_id = self.ids.category            
            self.menu_items = [
                {
                    "viewclass": "OneLineListItem",                
                    "text": name,
                    "on_release": lambda x = name : self.set_item(x,drop),
                }for name in self.category
            ]
        elif drop == "txn_mode":
            menu_id = self.ids.txn_mode  
            self.menu_items = [
                {
                    "viewclass": "OneLineListItem",                
                    "text": name,
                    "on_release": lambda x = name : self.set_item(x,drop),
                }for name in self.txn_mode
            ]
        self.menu = MDDropdownMenu(
            caller=menu_id,
            items=self.menu_items,
            position="bottom",
            width_mult=5,
            ver_growth="down",
            max_height=dp(200),
        )
        self.menu.bind()
        self.menu.open()
    def set_item(self, text_item,drop):
        if drop == "member":
            self.ids.member.set_item(text_item)
        elif drop == "txn_type": 
            self.ids.txn_type.set_item(text_item)
        elif drop == "category":
            self.ids.category.set_item(text_item)
        elif drop == "txn_mode":
            self.ids.txn_mode.set_item(text_item)

        self.menu.dismiss()
    
    def txn_confirm(self):
        self.dialogs = MDDialog(
            title = "Transaction",
            text ="Your transaction has been completed successfully",
            # size_hint=(.45, None),
            auto_dismiss=True,
            # type="custom",
            # content_cls=Content(),
            buttons=[
            MDFlatButton(
                text= "OK",
                md_bg_color= (248/255, 178/255, 45/255,1),
                on_release= lambda x:self.dialogs.dismiss() 
            ),
            # MDFlatButton(
            #     text= "Delete",
            #     md_bg_color= (242/255, 129/255, 42/255,1),
            #     on_release= lambda x: self.update(self.Remove_member_name)
            # )
        ],
        )
        # MDDialog(
        #     text="Discard draft?",
        #     content=Image(source='assets\img\icon_LS.png',        
        # )
        self.dialogs.open()
    