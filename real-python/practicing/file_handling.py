# Example 1
import os
f = open("demofile.txt")

# Example 2
# * The open() function returns a file object, which has a read() method for reading the content of the file:
f = open("demofile.txt", "r")
print(f.read())

# Example 3
# * Return the 5 first characters of the file:
f = open("demofile.txt", "r")
print(f.read(5))

# Example 4
# * You can return one line by using the readline() method:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())  # print one more line

# Example 5
f = open("demofile.txt", "r")
for x in f:
    print(x)

# Example 6
f = open("demofile.txt", "r")
print(f.readline())
f.close()

# Example 7
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
# * open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

# Example 8
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
# * open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())

# Example 9
# * To delete a file
os.remove("demofile.txt")
# Example 10
# * To delete a folder
os.rmdir("myfolder")
