from pathlib import Path

def readfilelandfolder():
    path = Path('')  # Fix 1: Capital P
    items = list(path.rglob('*'))
    for i, item in enumerate(items):  # Fix 2: renamed loop var to `item`
        print(f'{i+1} : {item}')

def createfile():
    try:
        readfilelandfolder()
        name = input("Please enter your file name: ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("What do you want to write in this file: ")
                fs.write(data)
            print("File created successfully")
        else:
            print("This file already exists.")
    except Exception as err:
        print(f"An error occurred: {err}")

def readfile():
    readfilelandfolder()
    name = input("Enter the file name to read: ")
    p = Path(name)
    if p.exists():
        print(p.read_text())
    else:
        print("File not found.")

def updatefile():
    readfilelandfolder()
    name = input("Enter the file name to update: ")
    p = Path(name)
    if p.exists():
        data = input("Enter new content: ")
        p.write_text(data)
        print("File updated successfully.")
    else:
        print("File not found.")

def deletefile():
    readfilelandfolder()
    name = input("Enter the file name to delete: ")
    p = Path(name)
    if p.exists():
        p.unlink()
        print("File deleted successfully.")
    else:
        print("File not found.")

# Menu
print("Press 1 to create a file")
print("Press 2 to read a file")
print("Press 3 to update a file")
print("Press 4 to delete a file")

check = int(input("Enter your choice: "))  # Fix 3: removed stray quote

# Fix 4: actually handle the user's choice
if check == 1:
    createfile()
elif check == 2:
    readfile()
elif check == 3:
    updatefile()
elif check == 4:
    deletefile()
else:
    print("Invalid choice.")
