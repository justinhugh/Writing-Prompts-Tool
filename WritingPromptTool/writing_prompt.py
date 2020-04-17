# Line to import the functions outlined in sub.py
import sub
import random
import tkinter.filedialog


filenames = sub.Get_all_files()
open_file_characters = open(filenames[0],'r')
open_file_conflicts = open(filenames[1],'r')
open_file_settings = open(filenames[2],'r')

# Print text to introduce user to purpose of program.
sub.Intro()

# Get the user's input for the type of prompt they're looking for.
requested_prompt = sub.Request_prompt_type()

# Print confirmation of selection
sub.Print_prompt_selection(requested_prompt)

# Read the corresponding text file, get list of strings
# Initialize a switch statement, which gives the correct function to use.

switch_prompt_function ={
                    "character": sub.Read_characters(open_file_characters),
                    "conflict": sub.Read_conflicts(open_file_conflicts),
                    "setting": sub.Read_settings(open_file_settings),
                    "all": sub.Read_all(open_file_characters,open_file_conflicts,open_file_settings),
                    }

# Create the appropriate list of prompts
prompt_list = switch_prompt_function.get(requested_prompt)

# Print random entry from list
print(prompt_list[random.randrange(0,len(prompt_list))])

# Print random prompt_list

# Return random string from list

# Print corresponding prompt(s)
