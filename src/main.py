import reference_functions

# Test binary_search_sorted_array function
inputList = [2, 5, 9, 11, 14, 18, 21, 24, 27, 30, 34, 38, 41, 45, 48, 52, 57, 61, 66, 70]
target = 21
location = reference_functions.binary_search_sorted_array(inputList,target)
print(f'\n\nlocation of number: {location}\n\n')