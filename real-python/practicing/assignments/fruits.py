# ASSIGNMENT - 1

###
#PROBLEM: Given a dictionary of 'fruits' as shown below, get all the fruit names where color is 'red'

fruits = {'apple': 'red', 'watermellon': 'green', 'grape': 'green', 'lemon': 'yellow', 'kiwifruit': 'brown', 'cherry': 'red'}

#********************* BASICS ******************#
# keys_output = []
# values_output = []

# # Ways to get keys of a dictionary
# ### 1 ###
# for x in fruits:
#     keys_output.append(x)
# # keys_output = ['apple', 'watermelon', 'grape', 'lemon', 'kiwifruit', 'cherry']
# ############

# ### 2 ###
# keys_output = list(fruits.keys())

# # Ways to get values of a dictionary
# ### 1 ###
# values_output = list(fruits.values())
# ############

# ### 2 ###
# values_output=[]
# for key,value in fruits.items():
#     values_output.append(value)
# ############
#*************************************************#


#********************* SOLUTION ******************#

red_fruits = []
### 1 ###
for key, value in fruits.items():
    if value == 'red':
        red_fruits.append(key)
############

### 2 ###
fruits_output = []
colors_output = []
fruits_output = list(fruits.keys())
colors_output = list(fruits.values())


positions = []
for index,color in enumerate(colors_output):
    if color == 'red':
        positions.append(index)
final_output = []
for p in positions:
    final_output.append(fruits_output[p])
############














# key for key, value in fruits.items() if value == 'red'
# print()