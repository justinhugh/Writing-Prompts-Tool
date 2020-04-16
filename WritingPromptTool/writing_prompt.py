# Line to import the functions outlined in sub.py
import sub
import tkinter.filedialog

# Print text to introduce user to purpose of program.
sub.Intro()

# Get the user's input for the type of prompt they're looking for.
requested_prompt = sub.Request_prompt_type()

# Print confirmation of selection
sub.Print_prompt_selection(requested_prompt)

filename = tkinter.filedialog.askopenfilename()
open_file = open(filename,'r')

print(sub.Read_characters(open_file))

# Read the corresponding text file, get list of strings
### if requested_prompt == 'all':
    # get lists from all three files
    ### pass
### else:
    ### pass
    # get list of corresponding category.


# Return random string from list

# Print corresponding prompt(s)
