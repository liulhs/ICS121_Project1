from pathlib import Path

def ask_and_check():
    while(True):
        file_name = input("Enter the file you want to process: ")
        file_path = Path(file_name.strip())
        if not file_path.exists():
            print('The file you want to access does not exist, try again!')
        elif file_path.is_dir():
            print('This is a directory, not a file bud! Try again.')
        else:
            return file_path

def open_and_read(file_path:Path):
    try:
        file_path.open()
    except(Exception):
        print('Something went wrong while opening the file, Sorry...')
        return
    
        

def word_seperate(target : str):
    
    return

ask_and_check()
print('ended')

