from menu_login import MenuLogin
from base_menu import BaseMenu , Option

class MenuAuth(BaseMenu):
    def __init__(self):
        MenuLogin.default_user()
        super().__init__([
            Option("Login", MenuLogin().login),
            Option("Register",MenuLogin().register)
        ], title="Options:")
        return None