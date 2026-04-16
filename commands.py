def get_last_id():
    try:
        with open("notesdb.txt", "r") as notes_file:
            all_notes = notes_file.read().strip().split("\n\n")
    except FileNotFoundError:
        return 0
    
    all_notes = [note for note in all_notes if note.strip()]
    
    if not all_notes:
        return 0
    else:
        return int(all_notes[-1].splitlines()[0])

ID = get_last_id()

def add_note(title, content):
    
    with open("notesdb.txt", "a") as notes_file:
        global ID
        ID += 1
        notes_file.write(str(ID) + "\n")
        notes_file.write(title + "\n")
        notes_file.write(content + "\n")
        notes_file.write("\n")

    return "Note added successfully.\n"


def list_notes():
    try:
        with open("notesdb.txt", "r") as notes_file:
            all_notes = notes_file.read()
    except FileNotFoundError:
        return "File not found.\n"
    
    return all_notes


def show_note(id):
    try:
        with open("notesdb.txt", "r") as notes_file:
            all_content = notes_file.read()
    except FileNotFoundError:
        return "File not found.\n"

    if not all_content:
        return "Empty file.\n"

    all_notes = all_content.strip().split("\n\n")

    for note in all_notes:
        if str(id) == note.splitlines()[0]:
            return note + "\n"
        
    return "Invalid note id.\n"


def delete_note(id):
    try:
        with open("notesdb.txt", "r") as notes_file:
            all_content = notes_file.read()
    except FileNotFoundError:
        return "File not found.\n"
    
    all_notes = all_content.strip().split("\n\n")

    notes_to_copy = []
    found = False

    for note in all_notes:
        if str(id) != note.splitlines()[0]:
            notes_to_copy.append(note)
        else:
            found = True

   
    with open("notesdb.txt", "w") as notes_file:
        for curr_note in notes_to_copy:
            notes_file.write(curr_note)
            notes_file.write("\n\n")
   


    if found:
        return "Note deleted successfully.\n"
    else:
        return "Invalid note id.\n"


def help():
    print("Available commands (press enter twice to execute):")
    print("note add \"title\" \"content\" -> to add a new note")
    print("note list -> to view all notes")
    print("note show 'id' -> to view note with specified id")
    print("note delete 'id' -> to delete a note with specified id")
    print("notes --help -> to view commands")
    print("q -> to quit\n")

if __name__ == "__main__":
    main()
    
    
