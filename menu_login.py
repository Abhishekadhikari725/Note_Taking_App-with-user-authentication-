import hashlib
import sqlite3
from db_conn import DB
from model_user import UserDAO
from menu_note import NoteMenu
from states import StateManager
import configs

class MenuLogin:
    def __init__(self):
        DB.initialize()
        self.state_manager = StateManager()


    def login(self):
        user_dao = UserDAO(sqlite3.connect('notes.db'))
        print("Insert credentials below:")
        username = input("Insert username: ")
        password = input("Insert password: ")
        hashed_password = hashlib.md5(password.encode()).hexdigest()

        user = user_dao.find_user(username, hashed_password)
        if user:
            print("Authenticated!\n")
            self.state_manager.set_logged_in_user(user)
            NoteMenu(username).activate()
        else:
            print("Failed to authenticate!\n")

    def register(self) -> None:
        conn = sqlite3.connect('notes.db')
        user_dao = UserDAO(conn)

        username = input("Insert username: ")

        if len(username) < 4 or len(username) > 10:
            if len(username) < 4:
                print("Username must be a minimum of '4' characters long.")
            else:
                print("Username must be a maximum of '10' characters long.")
            conn.close()
            return None

        for username_char in username:
            if username_char not in configs.ALLOWED_USERNAME_CHARS:
                print("Username can only contain:\n1. Lowercase characters 'a-z'\n2. Uppercase characters 'A-Z'\n3. Special characters '_' and '-'\n")
                conn.close()
                return None

        password = input("Insert password: ")

        for password_char in password:
            if password_char not in configs.ALLOWED_PASSWORD_CHARS:
                print("Password can only contain:\n1. Lowercase characters 'a-z'\n2. Uppercase characters 'A-Z'\n3. Special characters '_' and '-'\n")
                conn.close()
                return None

        if len(password) < 4 or len(password) > 10:
            if len(password) < 4:
                print("Password must be a minimum of '4' characters long.")
            else:
                print("Password must be a maximum of '10' characters long.")
            conn.close()
            return None

        confirm_password = input("Insert password again: ")

        if password != confirm_password:
            print("Passwords do not match!")
            conn.close()
            return None

        hashed_password = hashlib.md5(password.encode()).hexdigest()

        if user_dao.create_user(username, hashed_password):
            print("Registration completed!\n")
        else:
            print("Failed to register user.")

        conn.close()
        return None
    
    def default_user()->None:
        conn=sqlite3.connect('notes.db')
        user_dao=UserDAO(conn)
        username="demo_user"
        password="Secret123"
        hashed_password=hashlib.md5(password.encode()).hexdigest()
        user_dao.create_user(username=username,password=hashed_password)
        conn.close()
