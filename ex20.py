from sys import argv

script, input_file = argv


# function that reads entire file and prints its contents
def print_all(f):
    print(f.read())


# uses seek method to move back to the beginning of the file
def rewind(f):
    f.seek(0)


# reads a singular line from a file
def print_a_line(line_count, f):
    print(line_count, f.readline())


# sets current file to the input file input at the command line
current_file = open(input_file)

# Prints entire file
print("First let's print the whole file:\n")
print_all(current_file)

# sets the files current position to the beginning
print("Now let's rewind, kind of like a tape.")
rewind(current_file)

# Print the file line by line calling the readline on all three lines in the file
print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# closes the file
current_file.close()
