"""
IMPORT all modules here that use in this app.

"""


#--[Start UI Imports]
"""All imports for UI here Kivy,KivyMD or etc that help in UI"""
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.network.urlrequest import UrlRequest
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.image import Image
from kivy.metrics import dp


from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.card import MDCardSwipe
from kivymd.app import MDApp
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.uix.button import MDFlatButton,MDRaisedButton
from kivymd.uix.card import MDCard, MDSeparator
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import ImageLeftWidget, TwoLineAvatarListItem,OneLineIconListItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.textfield import MDTextField
from kivymd.uix.snackbar import Snackbar
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.selectioncontrol.selectioncontrol import MDSwitch

#--[End UI Imports]

from libs.uix.baseclass.ui_class import OneLineTextDialog
#--[Start Non UI Imports]
"""All imports that use in application """

#--[End Non UI Imports]