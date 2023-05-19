from main_imports import MDScreen, UrlRequest
from libs.applibs import utils
import certifi as cfi
import json
utils.load_kv("forgot.kv")

class Forgot_Screen(MDScreen):
    clientmaster={}
    def on_enter(self):
        self.generate_client_id()
        
    def on_leave(self):
        self.ids.Phone.text = ''

    def generate_client_id(self):
        url_common  = "https://pmca-a03a7-default-rtdb.firebaseio.com/masters/client_master.json"
        print("inside generate client id method")
        self.r = UrlRequest(url = url_common,on_success=self.getdata,ca_file=cfi.where(),verify=True)
        
    def getdata(self,*args):
        print("Result set ----> ",(self.r._result))
        self.clientmaster.update(self.r._result)
    def send_forgot_password_req(self,Phone):
        print("Send Forgot password req ---> ",Phone)
        url_blocked_users = "https://pmca-a03a7-default-rtdb.firebaseio.com/masters/blocked_users/.json"

        account_status = False
        client_id = ""
        data ={}
        if Phone != "":
            if len(Phone)==10:
                for key,value in self.clientmaster.items():
                    if value == Phone:
                        account_status=True
                        client_id=key
                        data.update({key:value})
                        print("forgot data ----> ",data)
                        break
                if account_status == True:
                    print("check condition -- > ",value==Phone)
                    forgot_pass_data = json.dumps(data)
                    userinfo = json.dumps({"app_access":3})
                    url_app_access = "https://pmca-a03a7-default-rtdb.firebaseio.com/"+str(client_id)+"/user_info/.json"
                    print(forgot_pass_data)
                    UrlRequest(url = url_blocked_users,req_body = forgot_pass_data,on_success=print("Forgot password list updated."),ca_file=cfi.where(),verify=True,method="PATCH")
                    UrlRequest(url = url_app_access,req_body = userinfo,on_success=print("User info app access updated."),ca_file=cfi.where(),verify=True,method="PATCH")
                    self.parent.change_screen("verification")
                else:
                    utils.snack("red","Do Not have Account with us Please Sign up")
            else:
                utils.snack("red","Please Enter Valid Phone Number.")
        else:
            utils.snack("red","Please Enter Phone Number.")