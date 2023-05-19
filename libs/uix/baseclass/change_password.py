from main_imports import MDScreen, UrlRequest
from libs.applibs import utils
import certifi as cfi
import json
utils.load_kv("change_password.kv")

class ChangePassword(MDScreen):
    current_pass = ""
    client_id = ""

    def on_enter(self, *args):
        self.ids.currentpassword.text = self.current_pass
        print(self.client_id)
    
    def change_password(self, newpass, confpass):
        if newpass==confpass:
            if self.client_id !="":
                url = "https://test-app-5b62b-default-rtdb.firebaseio.com/"+self.client_id+"/user_info/.json"
                data = json.dumps({"app_access":0,"password":newpass})
                UrlRequest(url = url,req_body = data,on_success=self.on_pass_change,ca_file=cfi.where(),verify=True,method="PATCH")

        else:
            utils.snack("red","Please Enter Same Password") 
    
    def on_pass_change(self,*args):
        print("Password has been updated.")
        self.parent.change_screen("groupselection")