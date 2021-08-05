# Example 1
num = 0
tot = 0.0
while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    num += 1  # num = num + 1
    tot += fval  # tot = tot + fval

print(tot, num, tot/num)

# Example 2
# The try block will raise an error when trying to write to a read-only file:
try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()
# The program can continue, without leaving the file object open

# Example 3
x = -1
if x < 0:
    raise Exception("Sorry, no numbers below zero")

# Example 4
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")
