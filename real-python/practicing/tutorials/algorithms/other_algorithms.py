
# * use a hashtable to filter out duplicate items

items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

filter = dict()
for key in items:
    filter[key] = 0

result = set(filter.keys())
print(result)

# * using a hashtable to count individula items

items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

counter = dict()

for item in items:
    if (item in counter.keys()):
        counter[item] += 1
    else:
        counter[item] = 1

print(counter)


# * use a recursive algorithm to find a maximum value

items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]


def find_max(items):
    if len(items) == 1:
        return items[0]

    op1 = items[0]
    print(op1)
    op2 = find_max(items[1:])
    print(op2)

    if op1 > op2:
        return op1
    else:
        return op2


print(find_max(items))
