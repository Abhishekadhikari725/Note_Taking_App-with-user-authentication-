from base_menu import BaseMenu, Option
from model_note import NoteDAO
from states import StateManager
from kirje import Kirje,KirjeDetails

class NoteMenu(BaseMenu):
    def __init__(self, username):
        super().__init__([
            Option("List notes", self.list_notes),
            Option("View note", self.view_note),
            Option("Add note", self.add_note),
            Option("Edit note", self.edit_note),
            Option("Delete note", self.delete_note)
        ], title=f"User '{username}' options:")
        self.username = username
        self.state_manager = StateManager()


    def list_notes(self) -> None:
        NOTES = NoteDAO.get_notes_by_user(self.username)
        length=len(NOTES)
        if length==0:
            print("There are no notes.\n")
        elif length>0:
            rows=[]
            for note in NOTES:
                rows.append(f"{note.id} - {note.title}")

            content = '\n'.join(rows)

            details=KirjeDetails (
                content= content,
                header_separation= " - ",
                headers={'ID': 'Title', 'Title': ' notes '}
            )
            memo_list= Kirje(details)
            memo_list.display("streamlined")
            rows.clear()
            print("")
        return None
    

    def view_note(self):
        note_title = str(input("Search note by title: "))
        note = NoteDAO.get_notes_by_title(self.username,note_title)
        if note :
            content=note.content
            details=KirjeDetails (
                content= content,
                header_separation= " - ",
                headers={'ID': f'{note.id}', 'Title': f'{note.title}'}
            )
            memo_list= Kirje(details)
            memo_list.display("default")
            print("")
        else:
            print("Not found.\n")

    def add_note(self)-> None:
        data_row=[]
        title=str(input("Insert title: "))
        rows=int(input("Insert the amount of rows: "))
        for row in range(rows):
            data=input(f"Insert row {row+1}: ")
            data_row.append(data)
        content='\n'.join(data_row)
        NoteDAO.create_note(self.username,title,content)
        print("Note stored!\n")

    def edit_note(self):
        title = str(input("Insert note title: "))
        NOTES = NoteDAO.get_notes_by_user(self.username)
        note_founded= False
        for note in NOTES:
            if note.title==title:
                new_title = input("Enter new title: ")
                new_content = input("Enter new content: ")
                success = NoteDAO.update_note(title, self.username, new_title, new_content)
                if success:
                    print("Note updated successfully.\n")
                    note_founded=True
                    return None
                else:
                    print("Failed to update note or access denied.\n")
            else:
                note_founded= False
        if not note_founded:
            print(f"'{title}' not found.\n")
            return None

    def delete_note(self):
        title = str(input("Delete note (insert title): "))
        success = NoteDAO.delete_note(title, self.username)
        if success:
            print("Note deleted successfully.")
        else:
            print(f"'{title}' not found.\n")
