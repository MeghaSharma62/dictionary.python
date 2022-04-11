
# Q51.Write a Python program to filter even numbers from a given dictionary values. 
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}


# dict={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# a={}
# for i,y in dict.items():
#         b=[]
#         for j in y:
#                 if j%2==0:
#                         b.append(j)
#                         a.update({i:b})
# print(a) 



id=[1,2,3,4]
n=["a","b","c","d","e"]
a=[12,6,8,9]
d={}
for i in range(len(id)):
        d1={}
        for j in range(len(n)):
                if i==j:
                        d1.update({n[j]:a[j]})
        d.update({id[i]:d1})
print(d)


# a=str(input("enter the number"))
# d={}
# for i in range(len(a)):
#         d.update({a[i]:i})
#         print(d)





# num=int(input("Enter the number"))
# l=[]
# for i in range(1,num):
#         l.append(i)
# print(l)
# d={}
# for i in range(len(l)):
#         if l[i]%2==0:
#                 d.update({l[i]:"true"})
#         else:
#                 d.update({l[i]:"false"})
# print(d)


# dict=


# Question 7 Write a Python program to check whether all dictionaries in a list are empty or not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

# n=input("Enter the dictionary:")
# if n=="{}":
#         print("yes")
# else:
#         print("no")

id=['S001', 'S002', 'S003', 'S004']
n=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
a=[85, 98, 89, 92]


d={}
for i in range(len(id)):
        d1={}
        for j in range(len(n)):
                if i==j:
                        d1.update({n[j]:a[j]})
        d.update({id[i]:d1})
print(d)
