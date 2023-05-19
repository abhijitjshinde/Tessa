from main_imports import MDScreen
from libs.applibs import utils

from libs.applibs import utils

from kivy.network.urlrequest import UrlRequest
import certifi as cfi
# import sys
import json
# sys.path.append("/".join(x for x in __file__.split("/")[:-1]))
# from json import dumps 
# import os.path


# from libs.uix.baseclass.login import Login_Screen

# from libs.uix.baseclass.root import Root
# from libs.uix.baseclass.signup import Signup_Screen
# from libs.uix.baseclass.verification import Verification_Scree


utils.load_kv("signup.kv")

class Signup_Screen(MDScreen):
    debug = False
    url  = "https://test-app-5b62b-default-rtdb.firebaseio.com/"
    url_common  = url + "common.json"
    new_client_id = 0 
    clientmaster={}
    groupmaster ={}
    def on_enter(self):
        self.generate_client_id()
    
    def generate_client_id(self):
        print("inside generate client id method")
        self. r = UrlRequest(url = self.url_common,on_success=self.getdata,ca_file=cfi.where(),verify=True)
        url_client_master  = self.url+"masters/client_master.json"
        url_group_master  = self.url+"masters/group_master.json"
        print("going to call client master")
        self.k = UrlRequest(url = url_client_master,on_success=self.getclientdata,ca_file=cfi.where(),verify=True)
        self.g = UrlRequest(url = url_group_master,on_success=self.getgroupdata,ca_file=cfi.where(),verify=True)

    def getgroupdata(self,*args):
        print("group master ----> ",(self.g._result))
        if self.g._result !=" ":
            self.groupmaster.update(self.g._result)

        else:
            print("CGroup master is blank")

    def getclientdata(self,*args):
        print("Client master ----> ",(self.k._result))
        if self.k._result !=" ":
            self.clientmaster.update(self.k._result)
        else:
            print("Client master is blank")   

    def getdata(self,*args):
        try:
            if self.r != None:
                print("Latest client ----> ",(self.r._result["last_client_id"]))
                last_client_id = str(self.r._result["last_client_id"])
                last_client_id = last_client_id[7:]
                self.new_client_id = "Client-"+str(int(last_client_id)+1)
            else:
                self.new_client_id = "Client-"+str(0)
        except:
            pass
    def Sign_me_up(self,Name,Phone,Password,Confirm_pass,user_type="Member",gcode = " ",is_admin_adding=False):
        client_id_g = ""
        account_exist = False
        if Phone != '' and Name != '':
            if len(Phone) == 10:
                for key,value in self.clientmaster.items():
                    if value == Phone:
                        account_exist=True
                        print("Number Existed ----> ",Phone)
                        client_id_g = key
                        break
                if account_exist == False and is_admin_adding == False:
                    if len(Password)> 5: 
                        if Password == Confirm_pass:
                            # self.generate_client_id()
                            client_id = str(self.new_client_id)
                            new_id_data =  json.dumps({"last_client_id":client_id})
                            UrlRequest(url = self.url_common,req_body = new_id_data,on_success=print("New client Id has been created."),ca_file=cfi.where(),verify=True,method="PATCH")
                            # return self.new_client_id
                            print(client_id)
                            url_client_master = self.url+"masters/client_master.json"

                            # new_client_data = str({f'\"{client_id}\":\"{Phone}\"'}) 
                            # new_client_data = new_client_data.replace(".","-")
                            # new_client_data = new_client_data.replace("\'","")
                            # to_database = json.loads(new_client_data)
                            new_client_data =json.dumps({client_id:Phone})
                            # print(to_database)
                            # data = json.dumps(new_client_data)
                            # print(data)
                            UrlRequest(url = url_client_master,req_body = new_client_data,on_success=print("client master updated."),ca_file=cfi.where(),verify=True,method="PATCH")                            
                            # signup_info =  str({f'\"{Phone}\":{{"user_info" : " ","transactions" : "None","states":""}}'})             
                            signup_info =  json.dumps({client_id:{"user_info" : {"name" : Name,"phone_number":Phone,"profile_pic" : " ","password": Password,"app_access":0},"groups":" "}})             
                            UrlRequest(url = self.url+".json",req_body = signup_info,on_success=print("client has been created."),ca_file=cfi.where(),verify=True,method="PATCH")
                            
                            self.parent.change_screen("login")
                        else:
                            utils.snack("red","Please Enter Same Password")    
                    else:
                        utils.snack("red","Please Enter 6 digit strong Password")                            
                elif account_exist == True and user_type == "Admin" and gcode != " ":
                    for key,value in self.groupmaster.items():
                        if (self.groupmaster[key]["group_name"]).lower() == gcode.lower():
                            # account_exist=True
                            print("group Existed ----> ",gcode)
                            break
                    signup_info =  json.dumps({"group_owner": client_id_g })             
                    UrlRequest(url = "https://test-app-5b62b-default-rtdb.firebaseio.com/masters/group_master/"+gcode+"/.json",req_body = signup_info,on_success=print("group has been created."),ca_file=cfi.where(),verify=True,method="PATCH")
                    client_group_info = json.dumps({gcode: {"your_funds":" ","your_due":"","your_loan":" ","your_penalty":" ","interest_paid":" ","user_type":user_type} }) 
                    UrlRequest(url = "https://test-app-5b62b-default-rtdb.firebaseio.com/"+client_id_g+"/groups/.json",req_body = client_group_info,on_success=print("group has been created."),ca_file=cfi.where(),verify=True,method="PATCH")
                    utils.snack("green","Client Already Exist,Group created !")
                elif account_exist == True and user_type == "Member" and gcode != " " and is_admin_adding==True:
                    # when admin adds member while member already exist
                    print("Inside admin adding client account exist")
                    client_group_info = json.dumps({gcode: {"your_funds":" ","your_due":"","your_loan":" ","your_penalty":" ","interest_paid":" ","user_type":user_type} }) 
                    UrlRequest(url = "https://test-app-5b62b-default-rtdb.firebaseio.com/"+client_id_g+"/groups/.json",req_body = client_group_info,on_success=print("group has been created."),ca_file=cfi.where(),verify=True,method="PATCH")
                    utils.snack("green","Member has been added to Group.")
                    
                elif account_exist == False and user_type == "Member"and is_admin_adding == True and gcode != " ":
                    print("Inside admin adding client account not exist")
                    # while admin adding Member is new
                    client_id = str(self.new_client_id)
                    new_id_data =  json.dumps({"last_client_id":client_id})
                    UrlRequest(url = self.url_common,req_body = new_id_data,on_success=print("New client Id has been created."),ca_file=cfi.where(),verify=True,method="PATCH")
                    # return self.new_client_id
                    print(client_id)
                    url_client_master = self.url+"masters/client_master.json"

                    # new_client_data = str({f'\"{client_id}\":\"{Phone}\"'}) 
                    # new_client_data = new_client_data.replace(".","-")
                    # new_client_data = new_client_data.replace("\'","")
                    # to_database = json.loads(new_client_data)
                    new_client_data =json.dumps({client_id:Phone})
                    # print(to_database)
                    # data = json.dumps(new_client_data)
                    # print(data)
                    UrlRequest(url = url_client_master,req_body = new_client_data,on_success=print("client master updated."),ca_file=cfi.where(),verify=True,method="PATCH")                            
                    # signup_info =  str({f'\"{Phone}\":{{"user_info" : " ","transactions" : "None","states":""}}'})             
                    signup_info =  json.dumps({client_id:{"user_info" : {"name" : Name,"phone_number":Phone,"profile_pic" : " ","password": Password,"app_access":2},"groups":{gcode: {"your_funds":" ","your_due":"","your_loan":" ","your_penalty":" ","interest_paid":" ","user_type":user_type} }}})             
                    UrlRequest(url = self.url+".json",req_body = signup_info,on_success=print("client has been created."),ca_file=cfi.where(),verify=True,method="PATCH")
                    
                    # self.parent.change_screen("login")                    
                    utils.snack("green","Member has been added to Group.")
                else:
                    utils.snack("red","Phone number is already taken")
            else:
                utils.snack("red","Please Enter valid Phone number")        
        else:
            utils.snack("red","Please fill all filelds.")
    def on_leave(self):
        self.ids.Phone.text = ''
        self.ids.Name.text = ''
        self.ids.Password.text = ''
        self.ids.Confirm_pass.text = ''