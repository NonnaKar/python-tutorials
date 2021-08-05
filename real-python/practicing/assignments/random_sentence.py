# text = input("Write some text with words 'He' and 'she':\n")
# # He wasn't bitter that she had moved on but from the radish.
# wordDict = {
#     'she': 'he',
#     'He': 'She'
# }

# def properCase(sentenses): 
# 	words=sentenses.split(". ") 
# 	new=". ".join([word.capitalize() for word in words]) 
# 	return new 

# for key, value in wordDict.items():
#     text = text.replace(key, value)

# new_text = properCase(text)
# print(new_text) 

# given text
text = "He wasn't bitter that she had moved on but from the radish. She is great."

##### Algorithm to solve this problem #######
# step1: convert entire text to case insensitive string 
case_insensitive_text = text.lower()
case_insensitive_text_list = case_insensitive_text.split(' ')
print(case_insensitive_text_list) # ['she', 'are', 'a', "man's", 'he', 'friend', 'and', 'she', 'are', 'she.']

# step2: now replace every "she" with "he"
replacement_dict = {'he': 'she', 'she': 'he'}
# for d_key, d_value in replacement_dict.items():
#     for l_idx, l_val in enumerate(case_insensitive_text_list):
#         if (d_key == l_val):
#             case_insensitive_text_list[l_idx] = d_value
for l_idx, word in enumerate(case_insensitive_text_list):
    if word in replacement_dict:
        case_insensitive_text_list[l_idx] = replacement_dict[word]
print(case_insensitive_text_list)

# step3: apply the logic of sentence case to above replaced string 
replaced_text = " ".join(case_insensitive_text_list)
print(replaced_text)

def properCase(replaced_text):
    sentences=replaced_text.split(". ")
    z = [sentence.capitalize() for sentence in sentences]
    # print(z)
    new_text=". ".join(z) 
    return new_text
print(properCase(replaced_text))