#*********************** Problem ******************************
# Given a list of 'letters' as shown below
# Print a Dictionary of letter count as shown in Exprected Output
#***************************************************************
letters = ['b', 'a', 'z', 'a', 'b', 'z', 'b', 'b', 'a', 'b']
#*********************** Exprected Output **********************
# alpha_count = {
#     'a': 3,
#     'b': 5,
#     'z': 2
# }
#***************************************************************

#******************* Start your code here **********************
alpha_count = dict() # firstly defigne a dictionary
letters = ['b', 'a', 'z', 'a', 'b', 'z', 'b', 'b', 'a', 'b'] # our list 
for l in letters: # loop though the list
    alpha_count[l] = alpha_count.get(l, 0) + 1 # 'l' - is a key; 0 - is default value if l is not there; to each l + 1
print(alpha_count)

#******************* End your code here **********************