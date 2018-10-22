from pathlib import Path # Instead of opening and reading the file directly, I'm using Python Pathlib to do the work
from _collections import defaultdict # Default dictionary comes in handy when appending and incrementing the result dictionary
import sys

# This function create a path object and check if the file is valid for processing
def ask_and_check():
    file_name = sys.argv[1].strip() # Storing the passed command argument to a variable
    file_path = Path(file_name.strip()) # Creating path a object
    if not file_path.exists():
        print('The file you want to access does not exist, try again!')
    elif file_path.is_dir():
        print('This is a directory, not a file bud! Try again.')
    else:
        try:
            return file_path.open() # might encounter read buffer problem ----------------------
        except(Exception):
            print('Something went wrong while opening the file, Sorry...please try again')

# This function reads a opened file and finally output a dictionary whose key is every token and value is the frequency
def open_and_read(file_open):
    result = defaultdict(int)
    for line in file_open:               # <--------------From this part(double loop), it's easy to see that this function/program runs at O(n^2)
        for word in word_seperate(line): # helper function
            if word.isalpha():
                result[word] += 1
    return result

# This function sort the result to the required from and print it out 
def sort_and_output(result: dict):
    result = sorted(result.items(), key = lambda x: (-x[1],x[0]))
    for i,j in result:
        print('{}\t{}'.format(i,j))

# A helper function that replace every punctuation with a white space. It also
# Turn every character to lower case and split them by white space.
# This function returns a list of every processed word or chunk of word.
def word_seperate(target : str):
    table = str.maketrans({key: ' ' for key in target if not key.isalpha()})
    return target.strip().lower().translate(table).split()


# Execute main function
if __name__ == '__main__':
    try:
        file_open = ask_and_check()
        result = open_and_read(file_open)
        sort_and_output(result)
    except(IndexError):
        print('Enter the name of the file you want to process as the second command argument please!')
    except(Exception):
        print('Something went wrong...? Please enter the right command argument please....')
    
    