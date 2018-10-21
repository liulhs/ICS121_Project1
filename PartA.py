from pathlib import Path
from _collections import defaultdict
import string

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
        file_open = file_path.open()
    except(Exception):
        print('Something went wrong while opening the file, Sorry...')
    result = defaultdict(int)
    for line in file_open:
        for word in word_seperate(line):
            if word.isalpha():
                result[word] += 1
    return result
    
        

def word_seperate(target : str):
    table = str.maketrans({key: None for key in string.punctuation})
    return target.strip().translate(table).split()

file_path = ask_and_check()
result = open_and_read(file_path)
for i,j in result.items():
    print('{}:{}'.format(i,j))

