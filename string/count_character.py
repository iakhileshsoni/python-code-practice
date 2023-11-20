
# Count the number of characters present in the given String
# expected output { 'a': 5, 'b': 6, 'c': 3,'d': 5 }

# Approach 1
test_string = "aaabbbaabbbcccddddd"

a = test_string.count('a')
b = test_string.count('b')
c = test_string.count('c')
d = test_string.count('d')

string_dict = {"a": a, "b": b, "c": c, "d": d}
print(string_dict, '\n')  # O/P     {'a': 5, 'b': 6, 'c': 3, 'd': 5}


# Approach 2
# from collections import Counter
# test_string2 = "Akhilesh"
# collection = Counter(test_string2)
# print(collection)
# # print(type(collection))     # <class 'collections.Counter'>
#
#
# # Approach 3
# import re
# test_string3 = "akhilesh"
# print(len(re.findall('a', test_string3)))
#
