from main_imports import ImageLeftWidget, MDScreen,NumericProperty, StringProperty,MDCard,toast,Animation,NumericProperty,MDListBottomSheet
from libs.applibs import utils
from jnius import cast
from jnius import autoclass

utils.load_kv("home.kv")

class RecentTxn(MDCard):
    Name = StringProperty()
    Date = StringProperty()
    txn_type = StringProperty()
    Amount = NumericProperty()

class Home_Screen(MDScreen):
    value = NumericProperty(0)
    # is_admin = 0 
    selected_group = ""
    usertype = "Member"
    def open_gpay(self):

        # import the needed Java class
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Intent = autoclass('android.content.Intent')
        Uri = autoclass('android.net.Uri')

        # create the intent
        intent = Intent()
        intent.setAction(Intent.ACTION_VIEW)
        intent.setData(
            Uri.parse("android-app://com.google.android.apps.nbu.paisa.user"))

        # PythonActivity.mActivity is the instance of the current Activity
        # BUT, startActivity is a method from the Activity class, not from our
        # PythonActivity.
        # We need to cast our class into an activity and use it
        currentActivity = cast('android.app.Activity',
                               PythonActivity.mActivity)
        currentActivity.startActivity(intent)

        # The Gpay will open.
    def set_grp_name(self,text):
        self.ids.grp_name.text = text
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
    }]
    def on_leave(self):
         self.ids.rh.data = []
    def on_enter(self):
        print(self.selected_group)
        # self.ids.appbar.title = self.selected_group
        self.value = 0
        anim = Animation(value=87060, duration=3)
        anim.start(self)
        # Access the carousel.
        # carousel = self.ids.car
        print("inside on start")
        # Set infinite looping (optional).
        # carousel.loop = True
        # # Schedule after every 3 seconds.
        # Clock.schedule_interval(carousel.load_next, 5)
        for x in self.transaction_list:
            self.add_txn(x)
        print("inside on start end")
    def add_txn(self,txn):
            self.ids.rh.data.append(
                {
                    "viewclass": "RecentTxn",
                    "Name": txn["name"],                    
                    "Date":txn["Date"],
                    "txn_type": txn["txn_type"],
                    "Amount": txn["Amount"],
                    "callback": lambda x: x,
                }
            )
    def callback_for_menu_items(self, *args):
        toast(args[0])
    def show_example_list_bottom_sheet(self):
        bottom_sheet_menu = MDListBottomSheet(
            radius_from="top", radius=15
        )
        for i in range(1, 7):
            bottom_sheet_menu.add_item(
                f"Fund name {i}",
                lambda x, y=i: self.callback_for_menu_items(
                    f"Fund name {y}"
                ),
            )
        bottom_sheet_menu.open()
    

