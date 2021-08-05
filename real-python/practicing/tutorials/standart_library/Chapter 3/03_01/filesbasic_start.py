# Basic file operations in Python


# TODO: open a file for writing data
# "w" means write, "r" means read, "a" means append, "r+" means read and write
fb = open("testfile.txt", "w")
fb.write("This is some text\n")
fb.close()

# TODO: read a file's data
with open("testfile.txt", "r") as fb:
    data = fb.read()
    print(data)

# TODO: Add data to an existing file
with open("testfile.txt", "a+") as fb:
    fb.write("This is data added onto the file\n")
    fb.seek(0)
    data = fb.read()
    print(data)
