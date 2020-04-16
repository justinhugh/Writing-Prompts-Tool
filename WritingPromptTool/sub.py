# Test function to test import of this file.
def Test():
    print("This is the test function.")

# Function to write introductory text at start of the program.
def Intro():
    print('\n\nThis is a program that will provide you with a character, a conflict, and a setting to write about.\n\n')

# Function to print text and ask for the prompt you're looking for.
def Request_prompt_type():
    '''
    Returns one of four strings, "character", "conflict", "response", or "all"
    that the user inputs.
    '''

    # Initialize a list of acceptable response.
    acceptable = ['character', 'conflict', 'setting', 'all']
    # Initialize user input string variable.
    user_input = ''

    # Request input from user until valid response is entered.
    while user_input not in acceptable:
        user_input = input('Type one of "character", "conflict", "setting", or "all"\n>>>: ')
    return user_input

# Print the prompt type the user entered.
def Print_prompt_selection(selection):
    '''Prints the prompt type the user input.
    '''

    if selection == 'all':
        print('\n\nYou asked for a random character, conflict, and setting')
    else:
        print('\n\nYou asked for a random ', selection,'\n\n',sep='')

# Function to read character text file, and pull a list of all characters
def Read_characters(open_file):
    '''(file open for reading) -> list of str()

    Read and return list of characters in characters textfile.

    Precondition: characters textfile is a list of characters, one per line,
    with no blank lines.
    '''

    # Initialize empty list to accumulate characters
    character_list = []
    # Read and store first character in first line.
    line = open_file.readline()

    # Until we reach an empty line, append the list and read next line,
    # storing it.
    while line !='':
        character_list.append(line)
        line = open_file.readline()
    return character_list

def Read_conflicts():
    '''(file open for reading) -> list of str()

    Read and return list of characters in characters textfile.

    Precondition: characters textfile is a list of characters, one per line,
    with no blank lines.
    '''
    return

def Read_settings():
    '''(file open for reading) -> list of str()

    Read and return list of characters in characters textfile.

    Precondition: characters textfile is a list of characters, one per line,
    with no blank lines.
    '''
    return
