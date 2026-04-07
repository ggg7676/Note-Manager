import shlex
from commands import add_note, show_note, list_notes, delete_note, help, ID

def main():
    
    while True:
        print("Enter a command and press enter twice: ")
        lines = []

        while True:
            line = input()

            if line == 'q':
                return
            
            if line == "":
                if not lines: 
                    print("Invalid command.\n")
                    print("Enter a command and press enter twice: ")
                    continue
                else:
                    break

            lines.append(line)

        if len(lines) == 1:

            command_line = lines[0]

            split_input = shlex.split(command_line)
            command_type = split_input[1]

            if command_type == 'add':
                print(add_note(split_input[2], split_input[3]))

            elif command_type == 'list':
                print(list_notes())

            elif command_type== 'show':
                print(show_note(split_input[2]))

            elif command_type == 'delete':
                print(delete_note(split_input[2]))
                
            elif command_type == '--help':
                help()
            
            else:
                print("Invalid command.")

        else:
            full_command = ""
            for line in lines:
                full_command += line + "\n"
            
            full_command = full_command.split('"')
            print(add_note(full_command[1], full_command[2]))

   

if __name__ == "__main__":
    main()
    
    
