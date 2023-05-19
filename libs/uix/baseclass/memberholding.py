from main_imports import MDScreen, StringProperty,MDCard, NumericProperty
from libs.applibs import utils

utils.load_kv("memberholding.kv")

class CustomOneLineIconListItemmh(MDCard):
    Name = StringProperty()
    Date = StringProperty()
    txn_type = StringProperty()
    Amount = NumericProperty()
    # Amount = NumericProperty()
    def KJ(self,text):
        print(text)

class Member_holdings(MDScreen):
    member_name = StringProperty()
    transaction_list = [{
        "name":"Abhijit Shinde",
        "Date":"15 April 2023",
        "txn_type": "Credit",
        "Amount": 100
    },
    {
        "name":"Abhijit Shinde",
        "Date":"15 April 2023",
        "txn_type": "Debit",
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
        self.set_txns(text= self.member_name,search=True)
        
    def pre_screen(self):
        self.parent.previous_screen()
    def set_txns(self,text="", search=False):
        '''Builds a list of icons for the screen MDIcons.'''
        
        def add_txn(txn):
            self.ids.mhv.data.append(
                {
                    "viewclass": "CustomOneLineIconListItemmh",
                    "Name": txn["name"],                    
                    "Date":txn["Date"],
                    "Amount": txn["Amount"],
                    "txn_type": txn["txn_type"],
                    "callback": lambda x: x,
                }
            )

        self.ids.mhv.data = []
        
        for txn in self.transaction_list:
            if search:
                if text in txn["name"]:
                    add_txn(txn)
            else:
                self.ids.mhv.data = []