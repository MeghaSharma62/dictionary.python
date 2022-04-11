# Q38.. Write a Python program to drop empty Items from a given Dictionary. 
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}


a={'c1': 'Red', 'c2': 'Green', 'c3': None}
b={}
# for key,value in a.items():
#         if value not in None:
#                 b.update({key:value})
# print(b)

dict1 = {key:value for (key, value) in a.items() if value is not None}
print(dict1)
