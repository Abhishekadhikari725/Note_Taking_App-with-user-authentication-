import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int
    username: str
    title: str
    content: str

class NoteDAO:
    def __init__(self):
        pass

    def get_notes_by_user(username):
        with sqlite3.connect('notes.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM notes WHERE username=?", (username,))
            rows = cursor.fetchall()
            return [Note(*row) for row in rows]

    def get_notes_by_title(username, title):
        with sqlite3.connect('notes.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, username, title, content FROM notes WHERE username=? AND title=?", (username, title))
            row = cursor.fetchone()
            if row:
                # Create a Note object using unpacking of the row tuple
                return Note(*row)
            else:
                return None 

    def create_note(username, title, content):
        with sqlite3.connect('notes.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO notes (username, title, content) VALUES (?, ?, ?)", (username, title, content))
            conn.commit()

    def update_note(title, username, new_title, new_content):
        with sqlite3.connect('notes.db') as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE notes SET title=?, content=? WHERE title=? AND username=?", (new_title, new_content,title,username))
            conn.commit()
            return cursor.rowcount > 0

    def delete_note(title, username):
        with sqlite3.connect('notes.db') as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM notes WHERE title=? AND username=?", (title, username))
            conn.commit()
            return cursor.rowcount > 0
