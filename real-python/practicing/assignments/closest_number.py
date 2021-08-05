numbers_input = input("Enter numbers: ")
num = list(map(int, numbers_input.split()))
print("Numbers: ", num)

minus_num = 200
dist_minus_num = [x-minus_num for x in num]
abs_val_list = [abs(n) for n in dist_minus_num]
min_abs_val_list = min(abs_val_list)
index_of_min_abs_val_list = abs_val_list.index(min_abs_val_list)
closest_to_minus_num = num[index_of_min_abs_val_list]
print(closest_to_minus_num)
