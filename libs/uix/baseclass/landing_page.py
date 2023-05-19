from main_imports import MDScreen
from libs.applibs import utils
# from plyer import network
# from android.storage import app_storage_path, primary_external_storage_path, secondary_external_storage_path
# from android.permissions import Permission, request_permissions, check_permission
utils.load_kv("landing_page.kv")

class Landing_Screen(MDScreen):
    pass
    # def on_enter(self):
    #     if network.check():
    #         utils.snack("Internet is available")
    #     else:
    #         utils.snack("No internet connection")     
    #     perms = [Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE,Permission.INTERNET]
    #     if  self.check_permissions(perms)!= True:
    #       request_permissions(perms)    # get android permissions     
    #       exit()
    # def check_permissions(self,perms):
    #   for perm in perms:
    #     if check_permission(perm) != True:
    #       return False
    #   return True
            		    