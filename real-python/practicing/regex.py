import re

"""
Regular Expressions
^ Start
$ Stop
. Any character
* Match one character 0+ times
+ Match one character 1+ times
? Non-greedy
\s Whitespace
\S Non-whitespace
[abc] Match one character in the specified set
[^abc] Match one character not in the specified set
"""

# myString = 'Send an email from this@email.com to test@user.com 34 times.'

# result = re.findall('\S+@\S+', myString)
# print(result)

# Example 1
text = open('shakespear.txt')

for line in text:
    line = line.rstrip()
    if re.search('^A.+$', line):
        print(line)

# Example 2
# Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("YES! We have a match!")
else:
    print("No match")

# Exampple 3
# Return a list containing every occurrence of "ai":
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

# Example 4
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

# Example 5
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

# Example 6
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

# Example 7
# Replace all white-space characters with the digit "9":
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

# Example 8
# Replace the first two occurrences of a white-space character with the digit 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

# Example 9
# Search for an upper case "S" character in the beginning of a word, and print its position:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

# Example 10
# The string property returns the search string:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

# Example 11
# Search for an upper case "S" character in the beginning of a word, and print the word:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
