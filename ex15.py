from sys import argv
# sets the inputs for script and filename = to arg variables
script, filename = argv

# assigns txt the value of the command open with the filename from argv as the argument
txt = open(filename)

# prints the name of the filename entered at the command line
print(f"Here's your file {filename}:")
# reads the contents of the file and prints the contents of the file that was opened
print(txt.read())

# prompts input for the name of the file again
print("Type the filename again:")
# takes user input and sets variable equal to it
file_again = input("> ")

# opens the file saved in the variable and assigns its value to the txt_again variable
txt_again = open(file_again)

# reads the file and prints it to the console
print(txt_again.read())

txt_again.close()
txt.close()