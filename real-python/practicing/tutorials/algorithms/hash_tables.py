
# * Example 1
items1 = dict({"key1": 1, "key2": 2, "key3": "three"})
print(items1)

# * Example 2
items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
print(items2)

# * Example 3
# print(items1["key6"])

# * Example 4
items2["key2"] = "two"
print(items2)

# * Example 5
for k, v in items2.items():
    print("Key: ", k, " value: ", v)
