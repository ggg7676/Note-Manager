import unittest
from commands import add_note, show_note, list_notes, delete_note

class TestCommands(unittest.TestCase):
    def test_add_note(self):
        self.assertEqual(add_note("Title", "Content"), "Note added successfully.\n")
    
    def test_delete_note_invalid(self):
        self.assertEqual(delete_note(str(999)), "Invalid note id.\n")

    def test_list_notes(self):
        with open("notesdb.txt", "r") as test_file:
            content = test_file.read()
        self.assertEqual(len(list_notes()), len(content))


if __name__ == "__main__":
    unittest.main()