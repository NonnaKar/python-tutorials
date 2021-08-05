# Example 1
# * using generators to find the longest name

full_names = (name.strip() for name in open('names.txt'))
lengths = ((name, len(name)) for name in full_names)
longest = max(lengths, key=lambda x: x[1])
print(longest)


# Example 2
# * adding separate_names generator as another stage in pipeline

def separate_names(names):
    for full_name in names:
        for name in full_name.split(' '):
            yield name


full_names = (name.strip() for name in open('names.txt'))
names = separate_names(full_names)
lengths = ((name, len(name)) for name in names)
longest = max(lengths, key=lambda x: x[1])
print(longest)


# Example 3

def separate_names(names):
    for full_name in names:
        for name in full_name.split(' '):
            yield name


def get_longest(namelist):
    full_names = (name.strip() for name in open(namelist))
    names = separate_names(full_names)
    lengths = ((name, len(name)) for name in names)
    return max(lengths, key=lambda x: x[1])


print(get_longest('names.txt'))
