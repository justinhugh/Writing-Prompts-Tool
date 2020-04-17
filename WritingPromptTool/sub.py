import tkinter.filedialog

# Test function to test import of this file.
def Test():
    print("This is the test function.")

# Function to write introductory text at start of the program.
def Intro():
    print('\n\nThis is a program that will provide you with a character, a conflict, and a setting to write about.\n\n')

# Function to get and open files
def Get_all_files():
    print('\n\nYou will be prompted for 3 file locations. Please select the location of character file, then conflicts file, then settings file.\n\n')
    input('press enter to begin...')
    characters_filename = tkinter.filedialog.askopenfilename()
    conflicts_filename = tkinter.filedialog.askopenfilename()
    settings_filename = tkinter.filedialog.askopenfilename()
    return characters_filename, conflicts_filename, settings_filename

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
    # Initialize empty list to accumulate characters.
    character_list = []
    # Read and store first character in first line.
    line = open_file.readline().strip('\n')

    # Until we reach an empty line, append the list and read next line,
    # storing it.
    while line !='':
        character_list.append(line)
        line = open_file.readline().strip('\n')
    return character_list

# Function to read conflicts text file, and pull a list of all conflicts
def Read_conflicts(open_file):
    '''(file open for reading) -> list of str()

    Read and return list of conflicts in conflicts textfile.

    Precondition: conflicts textfile is a list of conflicts, one per line,
    with no blank lines.
    '''
    # Initialize empty list to accumulate settings.
    conflicts_list = []
    # Read and store first character in first line.
    line = open_file.readline().strip('\n')

    # Until we reach an empty line, append the list and read next line,
    # storing it.
    while line !='':
        conflicts_list.append(line)
        line = open_file.readline().strip('\n')
    return conflicts_list

# Function to read settings text file, and pull a list of all settings
def Read_settings(open_file):
    '''(file open for reading) -> list of str()

    Read and return list of settings in settings textfile.

    Precondition: settings textfile is a list of settings, one per line,
    with no blank lines.
    '''

    # Initialize empty list to accumulate settings.
    settings_list = []
    # Read and store first character in first line.
    line = open_file.readline().strip('\n')

    # Until we reach an empty line, append the list and read next line,
    # storing it.
    while line !='':
        settings_list.append(line)
        line = open_file.readline().strip('\n')
    return settings_list

def Read_all(open_file_characters, open_file_conflicts, open_file_settings):
    pass
