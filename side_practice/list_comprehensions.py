mystring = 'hello'

mylist = []

for letter in mystring:
    mylist.append(letter)

better_list = [letter for letter in mystring]
mylist.reverse()
print(mylist)
print(better_list)
