# Example 1
from functools import reduce
list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))
# ['CAT', 'DOG', 'COW']

# Example 2
list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow']))
# ['dog', 'cow']

# Example 3
reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow'])
# 'cat | dog | cow'

# Example 4
ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
sorted_ids = sorted(ids, key=lambda x: int(x[2:]))  # Integer sort
print(sorted_ids)
# ['id1', 'id2', 'id3', 'id22', 'id30', 'id100']

# Example 5
nums = [1, 2, 3, 4, 5, 6]

# def square(n):
#     return n*n

# lambda n: n*n

print(list(map(lambda n: n*n, nums)))
