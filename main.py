from menu_auth import MenuAuth
from db_conn import DB

class Main:
    def __init__(self) -> None:
        # program code here
        print("Program starting.")
        _menu= MenuAuth()
        _menu.activate()
        # 1. initialize
        # 2. run
        # 3. cleanup
        print("Program ending.")
        return None

if __name__ == "__main__":
    app = Main()
