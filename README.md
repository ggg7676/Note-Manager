# Note-Manager-CLI
A command-line note-taking applicatio. Uses a text file as a database to store, access and delete notes.

Supported commands:

notes add 'Title' 'Content' -  adds a new note with specified title and content, and a unique id that increments automatically.
Ex.: notes add "Update schedule" "Add Meeting at 3PM"

notes list - shows all the notes currently stored in the database

notes show 'id' - shows the note with the specified id 
Ex.: notes show 2

notes delete 'id' - deletes the note with the specified id
Ex.: notes delete 5

notes --help - provides information about the supported commands and their usage.

To start the application, run the main.py file and use the command line to interact.
