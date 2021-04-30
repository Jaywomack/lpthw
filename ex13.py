from sys import argv
import pathlib

# # read the WYSS section for how to run this
# script, first, second, third = argv
#
# print("The script is called:", script)
# print("Your first variable is:", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)


script, name, height, weight = argv
print(f'Then your name is {name} and you are {height} inches tall and you weight {weight} lbs.')
