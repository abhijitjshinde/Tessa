import os
import configparser
from kivymd.uix.snackbar import Snackbar
from kivy.core.window import Window
from kivy.metrics import dp
from main_imports import Builder,MDFlatButton,MDDialog,MDRaisedButton,Image, MDDropdownMenu,MDSpinner
selected_group = ""

def load_kv(file_name, file_path=os.path.join("libs", "uix", "kv")):
    """
    `load_kv` func is used to load a .kv file.
    args that you can pass:
        * `file_name`: Name of the kv file.
        * `file_path`: Path to the kv file, it defaults
                       to `project_name/libs/kv`.

    Q: Why a custom `load_kv`?
    A: To avoid some encoding errors.
    """
    # print(file_path)
    with open(os.path.join(file_path, file_name), encoding="utf-8") as kv:
        Builder.load_string(kv.read())
def snack(color,text):
        if color == "red":
            clr= (1, 82/255, 82/255,1)
        elif color=="green":
            clr= (1, 1, 244/255, 1)
        else:
            clr= (11/255, 38/255, 83/255, 1)
        Snackbar(
            text=text,
            elevation=0.5,
            bg_color=clr,
            snackbar_x="10dp",
            snackbar_y="9dp",
            size_hint_x=(
                Window.width - (dp(10) * 2)
            ) / Window.width
        ).open()

def show_alert_dialog():
    print("inside alert box")
    dialog = MDDialog(
        text="Do You Want to Exit?",
        buttons=[
            MDFlatButton(
                text= "Cancel",
                # md_bg_color= (248/255, 178/255, 45/255,1),
                on_release= lambda x:dialog.dismiss() 
            ),
            MDFlatButton(
                text= "Exit",
                md_bg_color= (242/255, 129/255, 42/255,1),
                on_release= lambda x: exit()
            )
        ],
    )
    dialog.open()

def baseurl():
    config = configparser.ConfigParser()
    config.read('project_config.conf')

    url = config["Base_URL"]["base_url"]
    return url
def spinner(state):
    dialog = None
    
    sp =MDSpinner(
    size_hint=(None, None),
    size=(dp(46), dp(46)),
    pos_hint={'center_x': .5, 'center_y': .5},
    active=True,
    palette=[
        [0.28627450980392155, 0.8431372549019608, 0.596078431372549, 1],
        [0.3568627450980392, 0.3215686274509804, 0.8666666666666667, 1],
        [0.8862745098039215, 0.36470588235294116, 0.592156862745098, 1],
        [0.8784313725490196, 0.9058823529411765, 0.40784313725490196, 1],
    ])
    dialog = MDDialog(
        type= "custom",
        elevation = 0,
        md_bg_color = (1,1,1,0),
        opacity=1,
        size_hint=(None, None),
        size=(dp(85), dp(70)),
        content_cls=sp
        )
        # if state:
        #     dialog.open()
        # else:
        #     dialog.dismiss()
        

