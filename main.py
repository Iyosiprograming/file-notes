from datetime import date
import os

today = date.today()

def add_note():
    title = input("Enter note title: ")
    file_name = f"{title}.txt"
    content = input("Enter note content: ")
    
    with open(file_name, "w") as file:
        file.write(f"{title}\n{content}\n{today}\n\n")

def view_notes():
    try:
        filename = input("Enter the note title to view: ")
        with open(f"{filename}.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Note not found. Please check the title and try again.")
    

def update_note():
    try:
        filename = input("Enter the File Name to update: ")
        with open(f"{filename}.txt", "r") as file:
            content = file.readlines()
        if not content:
            print("Note is empty. Please add content first.")
            return
        print("Current content:")
        print("".join(content))
        file_name = input("Enter new file name (or press Enter to keep the same): ")
        if file_name:
            filename = file_name
        new_content = input("Enter new content: ")
        with open(f"{filename}.txt", "w") as file:
            file.write(f"{content[0]}{new_content}\n{today}\n\n")
           
        print("Note updated successfully.")
        
    except FileNotFoundError:
        print("Note not found. Please check the title and try again.")



def delete_note():
   try:
       filename = input("Enter the File Name to delete: ")
       os.remove(f"{filename}.txt")
       print(f"Note '{filename}' deleted successfully.")
   except FileNotFoundError:
       print("Note not found. Please check the title and try again.")
while True:
    print("********************** NOTE APP **********************")
    print("1. Add Note")
    print("2. View Note")
    print("3. Update Note")
    print("4. Delete Note")
    print("5. Exit")
    try:
        choice = int(input("Enter your choice: "))

    
        if choice == 1:
            add_note()
        elif choice == 2:
            view_notes()
        elif choice == 3:
            update_note()
        elif choice == 4:
            delete_note()
        elif choice == 5:
            print("Exiting the Note App. Goodbye!")
            break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
   



      
