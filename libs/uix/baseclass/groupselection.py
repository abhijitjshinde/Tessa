from main_imports import MDScreen, StringProperty,UrlRequest, NumericProperty,MDDatePicker, MDDropdownMenu, dp, BoxLayout,MDCard,MDDialog,MDFlatButton
from libs.applibs import utils

import os
import json
import certifi as cfi
from functools import partial
utils.load_kv("groupselection.kv")

class Groupitems(MDCard):
    Name = StringProperty()
    Date = StringProperty()
    group_id = StringProperty()
    
class Groupglobalitems(MDCard):
    Name = StringProperty()
    Date = StringProperty()
    group_id = StringProperty()
class GroupSelection(MDScreen):
    client_id_ = ""
    group_data = {}
    group_list = []
    def on_pre_enter(self, *args):
        group_master = "https://test-app-5b62b-default-rtdb.firebaseio.com/masters/group_master.json"
        self.user_group_info = UrlRequest(url = group_master,on_success=partial(self.getgroupdata),ca_file=cfi.where(),verify=True)
        
    def on_enter(self, *args):
        
        file_path = 'Json_Files/userinfo.json'       
        if os.path.getsize(file_path) != 0:
            
            with open(file_path) as f:
                data = json.load(f)
                key, value = list(data.items())[0]
                client_id = data[key]
                self.client_id_ =client_id
                #fetch all group data
                #fetch user group info
                url_clent = "https://test-app-5b62b-default-rtdb.firebaseio.com/"+str(client_id)+"/groups.json"
                self.user_info = UrlRequest(url = url_clent,on_success=partial(self.getuserdata),ca_file=cfi.where(),verify=True)

        else:
            print("File is Empty")
    def getgroupdata(self,*args):
        group_data = self.user_group_info._result
        self.group_data = group_data
        print("group data --->", self.group_data)
    def getuserdata(self,*args):
        user_data = self.user_info._result
        print("Groups IDs---> ",user_data.keys())
        for group in user_data.keys():
            # print(self.group_data[group]["group_name"]," -----> ",group)
            data ={
                "name":self.group_data[group]["group_name"],
                "Date":self.group_data[group]["created_date"],
                "Group_id": group,
                }
            self.group_list.append(data)
            self.ids.Gv.data.append(
                {
                    "viewclass": "Groupitems",                    
                    "Name": self.group_data[group]["group_name"],                    
                    "Date":self.group_data[group]["created_date"],
                    "group_id": group,
                    "callback": lambda x: x,
                }
            )
        # self.set_group_ist()
        
    def set_group_ist(self, text="", search=False,global_search=False):
        '''Builds a list of icons for the screen MDIcons.'''
        if global_search:
            def add_group_name(groupid):
                self.ids.AGV.data.append(
                    {
                        "viewclass": "Groupglobalitems",                    
                        "Name": self.group_data[groupid]["group_name"],                    
                        "Date":self.group_data[groupid]["created_date"],
                        "group_id": groupid,
                        "callback": lambda x: x,
                    }
                )

            self.ids.AGV.data = []
            for group in self.group_data.keys():
                if search:
                    if text.lower() in self.group_data[group]["group_name"].lower():
                        add_group_name(group)
                    elif text in group:
                        add_group_name(group)
                else:
                    # add_group_name(group)
                    self.ids.AGV.data = []
        else:
            def add_group_name(txn):
                self.ids.Gv.data.append(
                    {
                        "viewclass": "Groupitems",                    
                        "Name": txn["name"],                    
                        "Date":txn["Date"],
                        "group_id": txn["Group_id"],
                        "callback": lambda x: x,
                    }
                )

            self.ids.Gv.data = []
            for group in self.group_list:
                if search:
                    if text.lower() in group["name"].lower():
                        add_group_name(group)
                else:
                    add_group_name(group)
        

    def group_selected(self,Name,global_=False):
        print(Name)
        if global_:
            utils.snack("yellow","Group Access Request has been sent to Group Admin")
        else:
            file_path = 'Json_Files/userinfo.json'
            with open(file_path) as f:
                data = json.load(f)
                # key, value = list(data.items())[0]
                user_type = data["groups"][Name]["user_type"]
            self.parent.get_screen("home").usertype = user_type
            self.parent.get_screen("holdings").usertype = user_type
            self.parent.get_screen("admin").usertype = user_type
            self.parent.get_screen("profile").usertype = user_type
            self.parent.get_screen("notifications").usertype = user_type
            self.parent.get_screen("transactions").usertype = user_type
            grp_name = self.group_data[Name]["group_name"]
            self.parent.get_screen("home").set_grp_name(grp_name)
            self.parent.get_screen("admin").selected_group = Name
            self.parent.change_screen("home")
    def on_leave(self, *args):
        self.ids.Gv.data = []
        self.ids.AGV.data = []