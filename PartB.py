from pathlib import Path # Instead of opening and reading the file directly, I'm using Python Pathlib to do the work
import sys

# This function create a path object and check if the file is valid for processing
def ask_and_check():
    file1_name = sys.argv[1].strip()    # Storing the passed command argument to variables
    file2_name = sys.argv[2].strip()
    file1_path = Path(file1_name.strip())   # Creating path objects
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

## This function reads two opened files, and output the proper result             
def open_and_read(file1_open,file2_open):
    result1 = set() # Words in each file are going to be stored in Python sets, where each value is unique
    result2 = set()
    for line in file1_open:
        for word in word_seperate(line): # helper function
            if word.isalpha():
                result1.add(word)
    for line in file2_open:
        for word in word_seperate(line): # helper function
            if word.isalpha():
                result2.add(word)
    print(len(result1 & result2))   # Merge the two sets to find the intersection, which in this case are those common tokens in two files


# A helper function that replace every punctuation with a white space. It also
# Turn every character to lower case and split them by white space.
# This function returns a list of every processed word or chunk of word.
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