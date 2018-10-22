from pathlib import Path # Instead of opening and reading the file directly, I'm using Python Pathlib to do the work
from _collections import defaultdict # Default dictionary comes in handy when appending and incrementing the result dictionary
import string
import sys


def ask_and_check():
    file1_name = sys.argv[1].strip()
    file2_name = sys.argv[2].strip()
    file1_path = Path(file1_name.strip())
    file2_path = Path(file2_name.strip())
    if not file1_path.exists():
        print('The first file you want to access does not exist, try again!')
    elif not file2_path.exists():
        print('The second file you want to access does not exist, try again!')
    elif file1_path.is_dir() or file2_path.is_dir():
        print('This is a directory, not a file bud! Try again.')
    else:
        try:
            return file1_path.open(), file2_path.open() # might encounter read buffer problem ----------------------
        except(Exception):
            print('Something went wrong while opening the file, Sorry...please try again')
            
def open_and_read(file1_open,file2_open):
    result1 = set()
    result2 = set()
    for line in file1_open:
        for word in word_seperate(line): # helper function
            if word.isalpha():
                result1.add(word)
    for line in file2_open:
        for word in word_seperate(line): # helper function
            if word.isalpha():
                result2.add(word)
    print(len(result1 & result2))

def word_seperate(target : str):
    table = str.maketrans({key: ' ' for key in target if not key.isalpha()})
    return target.strip().lower().translate(table).split()


# Execute main function
if __name__ == '__main__':
    try:
        file1_open,file2_open = ask_and_check()
        open_and_read(file1_open, file2_open)
    except(IndexError):
        print('Enter the name of the file you want to process as the second command argument please!')
    except(Exception):
        print('Something went wrong...? Please enter the right command argument please....')