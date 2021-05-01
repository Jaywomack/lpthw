from sys import argv

script, file_in = argv

datain = open(file_in)


def read_file(f):
    return f.read()


def read_a_line(f):
    return f.readline()


print(read_file(datain))

datain.seek(0)

print(read_a_line(datain))

file1 = open(file_in, 'w')

file1.write('This will be written to the file.')


file1.close()