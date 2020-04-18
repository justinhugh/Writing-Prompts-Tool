import tkinter.filedialog
import os

# Function to write introductory text at start of the program.
def Intro():
    print('\n\nThis is a program that will provide you with a character, a '
          'conflict, and a setting to write about.')

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
        user_input = input('\n\nType one of "character", "conflict", "setting", or'
                           ' "all"\n>>>: ')
    return user_input

# Print the prompt type the user entered.
def Print_prompt_selection(selection):
    '''Prints the prompt type the user input.
    '''

    if selection == 'all':
        print('\n\nYou asked for a random character, conflict, and setting')
    else:
        print('\n\nYou asked for a random ', selection,sep='')

def Read_from_file(requested_prompt):
    '''(str) -> list of str()

    Return list of entries in textfile determined by requested_prompt.

    Precondition: textfile is a list of entries, one per line,
    with no blank lines.
    '''

    # Initialize empty list to accumulate settings.
    list = []

    # Find the correct file(s) to read based on requested_prompt. Use a switch.
    __location__ = os.path.realpath(
                                    os.path.join(os.getcwd(),
                                    os.path.dirname(requested_prompt + 's.text'))
                                    )
    f = open(os.path.join(__location__, requested_prompt + 's.text'),'r');

    line = f.readline().strip('\n')

    # Until we reach an empty line, append the list and read next line,
    # storing it.
    while line !='':
        list.append(line)
        line = f.readline().strip('\n')
    f.close()
    return list

def Read_all():
    '''
    Return list of list of entries in each of the prompt list textfiles

    Precondition: Each textfile is a list of entries, one per line,
    with no blank lines.
    '''
    # Initialize empty list to accumulate settings.
    list_of_lists = {}
    all_list = ['character', 'conflict', 'setting']

    for each_type in all_list:
        list = []
        # Find the correct file(s) to read based on requested_prompt. Use a switch.
        __location__ = os.path.realpath(
                                        os.path.join(os.getcwd(),
                                        os.path.dirname(each_type + 's.text'))
                                        )
        f = open(os.path.join(__location__, each_type + 's.text'),'r');

        line = f.readline().strip('\n')

        # Until we reach an empty line, append the list and read next line,
        # storing it.
        while line !='':
            list.append(line)
            line = f.readline().strip('\n')
        f.close()
        list_of_lists[each_type] = list
    return list_of_lists

def Thanks_for_using():
    print("\n\nOkay, thanks for using Justin's Writing Prompt Tool!\n\n")
