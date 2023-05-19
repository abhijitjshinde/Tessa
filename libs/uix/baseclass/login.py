from main_imports import MDScreen, UrlRequest
from libs.applibs import utils

# Python imports
import sys
# import requests
import json
import certifi as cfi
from functools import partial
# from android.permissions import Permission, request_permissions
sys.path.append("/".join(x for x in __file__.split("/")[:-1]))



utils.load_kv("login.kv")

class Login_Screen(MDScreen):
    login_check = False
    web_api_key = "AIzaSyDWO1Ko5GRUbt1QmEES09T0hQ3rkBmRYxE"
    # Firebase Authentication Credentials - what developers want to retrieve
    url  = "https://test-app-5b62b-default-rtdb.firebaseio.com/.json"
    auth = "QzCjigNhgwpP9dzrQKKosdRKYtnk2ButNsf2ykIa"
    file_path = 'Json_Files/userinfo.json'
    kp ={}
    def on_enter(self):
        # request_permissions([Permission.INTERNET,
        #                      Permission.READ_EXTERNAL_STORAGE,
        #                      Permission.WRITE_EXTERNAL_STORAGE],
        #                     lambda x: print('permissão'))
        # file_path = self.file_path
        # try:
        #     if os.path.getsize(file_path) != 0:
        #         with open(file_path) as f:
        #             data = json.load(f)
        #             key, value = list(data.items())[0]
        #             self.login_check = True
        #             self.ids.Phone.text = key            
        # except FileNotFoundError:
        #     print("file not Found")
        self.generate_client_id()
        pass
    def generate_client_id(self):
        url_common  = "https://test-app-5b62b-default-rtdb.firebaseio.com/masters/client_master.json"
        print("inside generate client id method")
        self.r = UrlRequest(url = url_common,on_success=self.getdata,ca_file=cfi.where(),verify=True)
        
    def getdata(self,*args):
        print("Result set ----> ",(self.r._result))
        self.kp.update(self.r._result)
        # client_master = data
        # for key, value in self.kp.items():
        #     value 
    def on_leave(self):
        self.ids.Phone.text = ''
        self.ids.Password.text = ''

    def sign_in(self, Phone,Password):
        # self.get_client_id(Phone)  
        try:
            if Phone != "":
                if len(Phone)==10:
                    if Password != "":
                        print("call from sign in -->",self.kp)
                        account_status = False
                        for key,value in self.kp.items():
                            if value == Phone:
                                account_status=True
                                print("value of phone ----> ",value)
                                break
                        if account_status == True:
                            print("check condition -- > ",value==Phone)                
                            url_clent = "https://test-app-5b62b-default-rtdb.firebaseio.com/"+str(key)+"/.json"
                            self.user_info = UrlRequest(url = url_clent,on_success=partial(self.getuserdata,Password,str(key)),ca_file=cfi.where(),verify=True)
                        else:
                            utils.snack("red","Do Not have Account with us Please Sign up")
                    else:
                        utils.snack("red","Please Enter Password.")
                else:
                    utils.snack("red","Please Enter Valid Phone Number.")
                        
            else:
                utils.snack("red","Please Enter Phone Number.")
        except:
            pass
    def getuserdata(self,Password,Client_id,*args):
        data = self.user_info._result
        user_data = data["user_info"]
        print("Client ID ---> ",Client_id)
        user_password = user_data["password"]
        self.parent.get_screen("changepassword").current_pass = user_password
        self.parent.get_screen("changepassword").client_id = Client_id
       
        
        app_access = user_data["app_access"]
        def store_userinfo():
            userinfo = {"Client_id":Client_id,"user_info":user_data,"groups":data["groups"]}
            try:
                with open(self.file_path,'w') as f:
                    json.dump(userinfo,f)
                    print("UserInfo file is modified...")
            except KeyError:
                print("the data is not stored...") 
          
        if user_password == Password and app_access==2:
            #when admin added client login
            # Login cred saved\
            store_userinfo()            
            self.parent.change_screen("changepassword")
        elif user_password == Password and app_access==0:
            self.parent.change_screen("groupselection")
            store_userinfo()

        elif user_password == Password and app_access==3:
            self.parent.change_screen("verification")
        else:
            utils.snack("red","Password is incorrect")

        print(Password," user info ---> ",user_data["password"])
