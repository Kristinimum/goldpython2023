import os # Connects Python to our operating system so we can interact with our OS like extract info about our files with methods seen below.
files_info = [] # Creates empty list
current_dir = os.getcwd() # This method returns processing from current working directory

for file in os.listdir(current_dir): # This method returns a list of files from the current directory
    file_location = os.path.realpath(file) # This method shows the location or the path to get to each file. This is a string.
    file_size = os.path.getsize(file) # This method shows the size of the file and can be in either bytes or string form. 
    files_info.append({'path': file_location, 'size': file_size}) # This adds or appends our dictionary to our list
    
print(*files_info, sep='\n') # This puts our key-value pairs on their own lines so it is easier to read. 