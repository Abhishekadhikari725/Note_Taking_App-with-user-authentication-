from abc import ABC,abstractmethod
from dataclasses import dataclass
from typing import Callable

@dataclass
class Option:
    description: str
    action: Callable


class BaseMenu(ABC):
    options: list[Option]
    @abstractmethod
    def __init__(self,
                 options: list[Option],
                 title: str ,
                 prompt: str = "Your choice: ",
                 submenu: bool=  False,
                 close: str = "") -> None:
        super().__init__()
        self.options=options
        self.title=title
        self.prompt=prompt
        self.submenu=submenu
        self.close=close
        return None
    def askChoice(self)-> int:
        choice : int = -1
        feed = input(self.prompt)
        if feed.isdigit():
            choice = int(feed)
        #TODO
        return choice
    def showOptions(self)-> None:
        if "List notes" in self.options[0].description:
            print(self.title)
            #iterate options
            for i , option in enumerate(self.options):
                print(f"{i+1} - {option.description}")
            print("0 - Logout") 
            return None
        else:
            print(self.title)
            #iterate options
            for i , option in enumerate(self.options):
                print(f"{i+1} - {option.description}")
            print("0 - Exit")
            #TODO iterate options
            return None
    def activate(self)->None:
        while True:
            # 1. show options
            self.showOptions()
            # 2. ask choice
            choice=self.askChoice()
            # 3. Do decision based choice
            if choice == 0:
                print("")
                break
            elif 0 < choice < len(self.options)+1:
                index= choice - 1
                self.options[index].action()
            else:
                print("Unknown Options.")
        return None