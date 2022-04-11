# Store the unique letters and their frequency of the letters from the word c to a dictionary, 
# were the letters are the keys and their frequencies are the values.
# Example:-
# Output :-

# {'M':1,'I':4,'S':4,'P':2}


# # l="MISSISSIPPI"
# l='brontosaurus' 
# a=(sorted(list(l)))
# i=0
# # count=0
# b=[]
# while i<len(a):
#         j=0
#         b1=[]
#         count=0
#         while j<len(a):
#                 if a[i] in a:
#                         if a[i]==a[j]:
#                                 count+=1
#                         j+=1
#         b1.append(a[i])
#         b1.append(count)
#         if b1 not in a:
#                 b.append(b1)
#         i+=1
# print(dict(b))
# print("Sorted by key: ", sorted(dict(b)))




        
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4={}
# for i in dic1,dic2,dic3:
#         dic4.update(i)
# print(dic4)



# Question6. Write a Python program to print all unique values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}


# a=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# b=[]
# for i in range(len(a)):
#         for j in a[i].values():
#                 if j not in b:
#                         b.append(j)
# print(b)


# Question7. Write a Python program to get the top three items in a shop.
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3
# a={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# my_dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# max=0
# for i in my_dict:
#         if my_dict[i]>max:
#                 max=my_dict[i]
#                 a=i
#                 max1=0
#                 for j in my_dict:
#                         if my_dict[j]>max1 and my_dict[j]!=max:
#                                 max1=my_dict[j]
#                                 b=j
#                                 max3=0
#                                 for k in my_dict:
#                                         if my_dict[k]>max3 and my_dict[k]!=max1 and my_dict[k]!=max:
#                                                 max3=my_dict[k]
#                                                 c=k
# print(a,max,b,max1,c,max3)



# Question8. Write a Python program to convert more than one list to nested dictionary.
# Original strings:                                              
# a=['S001', 'S002', 'S003', 'S004']
# b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# c=[85, 98, 89, 92]
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]



# Question10. Write a Python program to combines two or more dictionaries, creating a list of values for each key.
# Sample Output:
# Original dictionaries:
# {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
# {'x': 300, 'y': 'Red', 'z': 600}
# Combined dictionaries, creating a list of values for each key:
# {'w': [50], 'x': [100, 300], 'y': ['Green', 'Red'], 'z': [400, 600]}
# a={'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
# b={'x': 300, 'y': 'Red', 'z': 600}
# k={}
# d=[]
# for i in b:
#         if i in a:
#                 a[i]=a[i],b[i]
#                 # b.append(a[i],b[i])
#         else:
#                 a[i]=b[i]
#                 # b.append(a[i],b[i])
# print(b)



# Question9. Write a Python program to convert a given dictionary into a list of lists. 
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Convert the said dictionary into a list of lists:
# def test(dictt):
#             result=list(map(list, dictt.items()))
#             return result    

# color_dict = {1 : 'red', 2 : 'green', 3 : 'black', 4 : 'white', 5 : 'black'}
# # print("\nOriginal Dictionary:")
# # print(color_dict)
# # print("Convert the said dictionary into a list of lists:")
# print(test(color_dict))



# Question8. Write a Python program to convert more than one list to nested dictionary.
# Original strings:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]



a=['S001', 'S002', 'S003', 'S004']
b=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
c=[85, 98, 89, 92]
d=[]
for i in len(a,b,c):
        d.append(i)
print(d)
