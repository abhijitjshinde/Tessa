from main_imports import MDScreen, StringProperty,MDCard,MDFlatButton,MDToggleButton,NumericProperty,MDSwitch
from libs.applibs import utils

utils.load_kv("notification.kv")

class NotificationCard(MDCard):
    From = StringProperty()
    Date = StringProperty()
    notification_type = StringProperty()
    Notification_heading = StringProperty()
    For = StringProperty()




class Notifications(MDScreen):
    usertype="Member"
    notification_list = [{
        "from":"Abhijit Shinde",
        "Date":"15 April 2023",
        "notification_type": "Enable Access",
        "Notification_heading": "Test ",
        "for": "admin"
    },
    {
        "from":"Nikhil Khopkar",
        "Date":"15 April 2023",
        "notification_type": "Password Reset",
        "Notification_heading": "This is test Notification for test",
        "for": "admin"
    },
    {
        "from":"Shyam Alange",
        "Date":"15 April 2023",
        "notification_type": "Request Loan",
        "Notification_heading": "Need loan of 23000 urgent",
        "for": "admin"
    },
    {
        "from":"Abhijit Shinde",
        "Date":"15 April 2023",
        "notification_type": "General",
        "Notification_heading": "This is test Notification for test",
        "for": "all"
    },
    {
        "from":"Sandeep K",
        "Date":"15 April 2023",
        "notification_type": "Personalized",
        "Notification_heading": "This is test Notification for test",
        "for": "Abhijit Shinde"
    },]
    def on_enter(self, *args):
        self.set_notifications()

    def set_notifications(self, text="", search=False):
        '''Builds a list of icons for the screen MDIcons.'''

        def add_notification(txn):
            self.ids.nv.data.append(
                {
                    "viewclass": "NotificationCard",
                    "From": txn["from"],                    
                    "Date":txn["Date"],
                    "notification_type": txn["notification_type"],
                    "Notification_heading": txn["Notification_heading"],
                    "For": txn["for"],
                    "callback": lambda x: x,
                }
            )

        self.ids.nv.data = []
        for txn in self.notification_list:
            if search:
                if text in txn["Notification_heading"]:
                    add_notification(txn)
            else:
                add_notification(txn)