from main_imports import MDScreen, StringProperty, NumericProperty,MDDatePicker, MDDropdownMenu, dp, BoxLayout,MDCard,MDDialog,MDFlatButton
from libs.applibs import utils

import datetime
utils.load_kv("transactions.kv")

class FilterContent(BoxLayout):
    
    filter_data_list = [{"member":"All"},{"Date":"All"},{"txn_type":"All"}]
    
    #Date picker
    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        print(value, date_range)
        if date_range:
            if max(date_range) > datetime.date.today():
                to_date = datetime.date.today()
            else:
                to_date = max(date_range)
        else:
            to_date = datetime.date.today()
        if date_range:
            from_date = min(date_range)
        else:
            from_date = datetime.date.today()
        Date_reange = str(from_date)+" To "+str(to_date)
        self.Date = Date_reange
        self.set_item(Date_reange,"Date")
        

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
        pass
    
    def show_date_picker(self):
        
        date_dialog = MDDatePicker(mode="range",
                max_date=datetime.date(
                datetime.date.today().year,
                datetime.date.today().month,
                datetime.date.today().day,
            )
            )
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    # FILTERS
    member_list = ["Abhijit Shinde","Rohit Shinde","Aaba Bochre","Maruti Chavan","Sidheshwar Jevale"]
    txn_type = ["All","Credit","Debit","Loan","Event"]
    txn_mode = ["Online","Offline"]

    def open_menu(self,drop):
        
        if drop == "member":
            menu_id = self.ids.member
            ml = self.member_list
            ml.insert(0,"All Member")
            self.menu_items = [
                {
                    "viewclass": "OneLineListItem",                
                    "text": name,
                    "on_release": lambda x = name : self.set_item(x,drop),
                }for name in ml
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
            self.filter_data_list[0]["member"] = text_item
            self.menu.dismiss()
        elif drop == "txn_type": 
            self.ids.txn_type.set_item(text_item)
            self.filter_data_list[2]["txn_type"] = text_item
            self.menu.dismiss()
        elif drop == "Date": 
            self.ids.Date.set_item(text_item)
            self.filter_data_list[1]["Date"] = text_item
        # print(self.Date,self.txn_typel,self.member)
        print(self.filter_data_list)
        

class CustomOneLineIconListItem(MDCard):
    Name = StringProperty()
    Date = StringProperty()
    txn_type = StringProperty()
    Amount = NumericProperty()


class Transactions(MDScreen):
    usertype="Member"
    transaction_list = [{
        "name":"Abhijit Shinde",
        "Date":"15 April 2023",
        "txn_type": "Credit",
        "Amount": 100
    },
    {
        "name":"Abhijit Shinde",
        "Date":"19 April 2023",
        "txn_type": "Credit",
        "Amount": 100
    },
    {
        "name":"Abhijit Shinde",
        "Date":"23 April 2023",
        "txn_type": "Credit",
        "Amount": 100
    },
    {
        "name":"Rohit Shinde",
        "Date":"15 April 2023",
        "txn_type": "Loan",
        "Amount": 3000
    },
    {
        "name":"Aaba Bochre",
        "Date":"15 April 2023",
        "txn_type": "Penalty",
        "Amount": 20
    },
    {
        "name":"Abhijit Shinde",
        "Date":"2023-04-15",
        "txn_type": "Loan",
        "Amount": 100
    },
    {
        "name":"Maruti Chavan",
        "Date":"15 April 2023",
        "txn_type": "Debit",
        "Amount": 10000
    },
    {
        "name":"Sidheshwar Jevale",
        "Date":"15 April 2023",
        "txn_type": "Interest",
        "Amount": 50
    }]
    def on_enter(self):
        self.set_txns()
        
        
    def set_txns(self, text="", search=False,txnfilter=False,sdate="",edate="",member="",txn_type=""):
        '''Builds a list of icons for the screen MDIcons.'''
        if text != "":
            text=text.lower()
        # print(len([sdate,edate,member,txn_type]))
        def add_txn(txn):
            self.ids.rv.data.append(
                {
                    "viewclass": "CustomOneLineIconListItem",
                    "Name": txn["name"],                    
                    "Date":txn["Date"],
                    "txn_type": txn["txn_type"],
                    "Amount": txn["Amount"],
                    "callback": lambda x: x,
                }
            )

        self.ids.rv.data = []
        if search:
            for txn in self.transaction_list:
                if text in txn["name"].lower():
                    add_txn(txn)
                elif text in str(txn["Amount"]):
                    add_txn(txn)
                elif text in txn["txn_type"].lower():
                    add_txn(txn)
        elif txnfilter:
            ll =[]
            print(member,edate,sdate,txn_type)
            if member != "All" or edate != 32 or sdate != 32 or txn_type != "All":
                print("In if of txnfilter")
                for i in range(len(self.transaction_list)):
                    if(member == "All"):
                        if(sdate == 32):
                            if(txn_type == "All"):
                                ll.append(self.transaction_list[i])
                            elif(self.transaction_list[i]["txn_type"]==txn_type):
                                ll.append(self.transaction_list[i])
                        elif(self.transaction_list[i]["Date"]>=sdate and self.transaction_list[i]["Date"]<=edate):
                            if(txn_type == "All"):
                                ll.append(self.transaction_list[i])
                            elif(self.transaction_list[i]["txn_type"]==txn_type):
                                ll.append(self.transaction_list[i])
                    elif(member == self.transaction_list[i]["name"]):
                        if(sdate == 32):
                            if(txn_type == "All"):
                                ll.append(self.transaction_list[i])
                            elif(self.transaction_list[i]["txn_type"]==txn_type):
                                ll.append(self.transaction_list[i])
                        elif(self.transaction_list[i]["Date"]>=sdate and self.transaction_list[i]["Date"]<=edate):
                            if(txn_type == "All"):
                                ll.append(self.transaction_list[i])
                            elif(self.transaction_list[i]["txn_type"]==txn_type):
                                ll.append(self.transaction_list[i])
                print("List from filter -->",ll)
                for txn in ll:
                    add_txn(txn)
            else:
               print("In Else filter")
               for txn in self.transaction_list:
                add_txn(txn) 
        else:
            for txn in self.transaction_list:
                add_txn(txn)    
                



                # if member!="" and txn_type!=""and date_range!="":# 3 filter
                #     f_date = date_range[0:10]
                #     to_date = date_range[14:]
                #     if member in txn["name"] and txn_type in txn["txn_type"]:
                #         if f_date<= date_range<= to_date:
                #             add_txn(txn)                                         
                # elif member=="" and txn_type!=""and date_range!="":# 2 filoter
                #     f_date = date_range[0:10]
                #     to_date = date_range[14:]
                #     if txn_type in txn["txn_type"]:
                #         if f_date<= date_range<= to_date:
                #             add_txn(txn)
                # elif member!="" and txn_type==""and date_range!="":
                #     f_date = date_range[0:10]
                #     to_date = date_range[14:]
                #     if member in txn["name"]:
                #         if f_date<= date_range<= to_date:
                #             add_txn(txn)
                # elif member!="" and txn_type!=""and date_range=="":
                #     if member in txn["name"] and txn_type in txn["txn_type"]:
                #         add_txn(txn)
                

            
    # FILTER Dialog
    dialog = None
    def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Filter",
                type="custom",
                content_cls=FilterContent(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        # text_color=self.theme_cls.primary_color,
                        on_release= lambda x: self.dialog.dismiss()
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        # text_color=self.theme_cls.primary_color,
                        on_release= lambda x: self.getfilterdata()
                    ),
                ],
            )
        self.dialog.open()
    
    def getfilterdata(self):
        F = FilterContent()       

        # self.set_txns(txnfilter=True,)
        
        print("Filter data from Get ",F.filter_data_list)
        print(F.filter_data_list[0]["member"])
        
      
        try:
            Member = F.filter_data_list[0]["member"]
        
            Date = F.filter_data_list[1]["Date"]
        
            Txn_type = F.filter_data_list[2]["txn_type"]
        except KeyError:
            print("Some thing went wrong")
                  
        print(Member,Date,Txn_type)
        if Date != "All":
            f_date = Date[0:10]
            to_date = Date[14:]
        else:
            f_date = 32
            to_date = 32
        if Member == "All Member":
            Member = "All"
        self.set_txns(txnfilter=True,member=Member,txn_type=Txn_type,sdate=f_date,edate=to_date)
        self.dialog.dismiss()