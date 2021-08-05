
# * The Top 10 most common words
# Example 1
fhand = open('war_and_peace.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)

# Example 2
# LIST COMPREHENSION creates a dynamic list.
# In this case, we make a list of reversed tuples and then sort it.

c = {'a': 10, 'b': 1, 'c': 22}

print(sorted([(v, k) for k, v in c.items()]))
