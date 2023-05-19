from main_imports import MDScreen, StringProperty,MDCard,MDFlatButton,MDToggleButton
from libs.applibs import utils

utils.load_kv("holdings.kv")

class CustomOneLineIconListItemh(MDCard):
    Name = StringProperty()
    Paid = StringProperty()
    Due = StringProperty()
    Loan = StringProperty()
    image = StringProperty()
    # Amount = NumericProperty()
    
class ToggleButtons(MDFlatButton, MDToggleButton):
    pass
class Holdings(MDScreen):
    usertype="Member"
    def KJ(self,text,individual=True):
        print(text)
        if individual:
            self.parent.get_screen("memberholdings").ids.ind.text = "individual Folio"
            self.parent.get_screen("memberholdings").ids.ind.state = "down"

        else:
            self.parent.get_screen("memberholdings").ids.ind.text = "your Folio"
            self.parent.get_screen("memberholdings").ids.ind.state = "down"
        self.parent.get_screen("memberholdings").member_name = str(text)
        self.parent.change_screen("memberholdings")
    transaction_list = [{
        "name":"Abhijit Shinde",
        "Paid":"15K",
        "Due": "999",
        "Loan": "78K"
    },
    {
        "name":"Rohit Shinde",
        "Paid":"15K",
        "Due": "999",
        "Loan": "78K"
    },
    {
        "name":"Aaba Bochre",
        "Paid":"15K",
        "Due": "999",
        "Loan": "78K"
    },
    {
        "name":"Maruti Chavan",
        "Paid":"15K",
        "Due": "999",
        "Loan": "78K"
    },
    {
        "name":"Sidheshwar Jevale",
        "Paid":"15K",
        "Due": "999",
        "Loan": "78K"
    },
    {
        "name":"Aaba Bochre",
        "Paid":"15K",
        "Due": "999",
        "Loan": "78K"
    },
    {
        "name":"Loko Bore",
        "Paid":"999",
        "Due": "9K",
        "Loan": "78Lac"
    },
    {
        "name":"Aasha Kene",
        "Paid":"150",
        "Due": "999",
        "Loan": "789K"
    },]
    def on_enter(self):
        self.ids.grp.md_bg_color = "#F8B22D"
        self.set_txns()
        

    def set_txns(self):
        '''Builds a list of icons for the screen MDIcons.'''
        
        def add_txn(txn):
            self.ids.hv.data.append(
                {
                    "viewclass": "CustomOneLineIconListItemh",
                    "Name": txn["name"],                    
                    "Paid":txn["Paid"],
                    "image": "assets/img/blank_profile.png",
                    "Due": txn["Due"],
                    "Loan": txn["Loan"],
                    "callback": lambda x: x,
                }
            )

        self.ids.hv.data = []
        for txn in self.transaction_list:
            add_txn(txn)
