from main_imports import MDScreen, UrlRequest
from libs.applibs import utils
import certifi as cfi
import json
from datetime import datetime, date
utils.load_kv("registergroup.kv")

class Registergroup(MDScreen):
    groupmaster={}
    new_group_id =""
    def on_enter(self):
        self.generate_group_id()
        
    def on_leave(self):
        # self.ids.Phone.text = ''
        pass

    def generate_group_id(self):
        url  = "https://test-app-5b62b-default-rtdb.firebaseio.com/"
        url_common  = url + "common.json"
        print("inside generate client id method")
        self.r = UrlRequest(url = url_common,on_success=self.getdata,ca_file=cfi.where(),verify=True)
        url_client_master  = url+"masters/group_master.json"
        print("going to call group master")
        self.k = UrlRequest(url = url_client_master,on_success=self.getclientdata,ca_file=cfi.where(),verify=True)

    def getclientdata(self,*args):
        print("group master ----> ",(self.k._result))
        if self.k._result !=" ":
            self.groupmaster.update(self.k._result)
        else:
            print("CGroup master is blank") 
    def getdata(self,*args):
        try:
            if self.r != None:
                print("Latest client ----> ",(self.r._result["last_group_id"]))
                last_client_id = str(self.r._result["last_group_id"])
                last_client_id = last_client_id[2:]
                self.new_group_id = "TG"+str(int(last_client_id)+1)
            else:
                self.new_group_id = "TG"+str(0)
        except:
            pass
    
    def group_register(self,gname):
        print(gname)
        
        if gname != '':
            print("Group master from register ",self.groupmaster)
            if self.groupmaster:
                print("in Group")
                print(self.groupmaster)
            for key,value in self.groupmaster.items():
                if (self.groupmaster[key]["group_name"]).lower() == gname.lower():
                    # account_exist=True
                    print("group Existed ----> ",gname)
                    break

            else:
                print("out Group")

                group_id = str(self.new_group_id)
                new_id_data =  json.dumps({"last_group_id":group_id})
                UrlRequest(url = "https://test-app-5b62b-default-rtdb.firebaseio.com/common/.json",req_body = new_id_data,on_success=print("New group Id has been created."),ca_file=cfi.where(),verify=True,method="PATCH")
                # return self.new_client_id
                x = datetime.strptime(str(date.today()), '%Y-%m-%d')
                current_date = x.strftime('%d %b %Y').upper()
                signup_info =  json.dumps({self.new_group_id:{"created_date":current_date,"group_name" : gname,"group_owner": " ","group_T":" ","group_S":" ","group_state":{"total_funds":"","total_loan":"","loan_available":"","total_due":""}}})             
                UrlRequest(url = "https://test-app-5b62b-default-rtdb.firebaseio.com/masters/group_master.json",req_body = signup_info,on_success=print("group has been created."),ca_file=cfi.where(),verify=True,method="PATCH")
                            
        
                self.parent.get_screen("signup").ids.mheading.text = str(gname)
                self.parent.get_screen("signup").ids.groupcode.text = str(group_id)
                self.parent.get_screen("signup").ids.hline.text = "President Registration"
                self.parent.change_screen("signup")