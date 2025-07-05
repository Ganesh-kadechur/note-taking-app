import os

def load_notes():
    if not os.path.exists("data/notes.txt"):
        return[]

    with open("data/notes.txt", "r") as f:
        return f.readlines()


def save_notes(notes):
    with open("data/notes.txt", "w") as f:
        f.writelines(notes)


def add_note():
    note = input("Enter note: ") + "\n"
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print("Note added successfully")

def view_notes():
    notes = load_notes() #loading the saved notes

    if not notes:                  #checking whether the list is empty
        print("No notes found")
    else:
        for i, note in enumerate(notes,1): #enumerate = Gives (index,notes) starting from 1
             print(f"{i}.{note.strip()}")#line breaks using .string()  = removes trailing \n from each note

def delete_note():
    notes = load_notes()

    if not notes:
        print("No notes found to delete")
        return
    # show all notes
    for i, note in enumerate(notes,1):
        print(f"{i}.{note.strip()}")

    try:
        choice = int(input("Enter note number you want to delete: "))-1

        if 0 <= choice < len(notes):
            deleted_note = notes.pop(choice)
            save_notes(notes)
            print("deleted:",deleted_note.strip())
        else:
            print("invalid number.")

    except ValueError:
        print("please enter a valid number. ")

def main():
    while True:
        print("1. Add note")
        print("2. View notes")
        print("3. Delete note")
        print("4. Exit")

        choice = int(input("Enter choice: "))
        if choice == 1:
            add_note()
        elif choice == 2:
            view_notes()
        elif choice == 3:
            delete_note()
        elif choice == 4:
            print("goodbye /n""Exiting...")
            break
        else:
            print("invalid number.please select between 1 and 4")


if __name__ == "__main__":
    main()