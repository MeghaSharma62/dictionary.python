# def a(b=[0,1,1,2,3,5]):
#         i=0
#         c=[]
#         while i<len(b):
#                 c.append(b[i]**3)
#                 i=i+1
#         print(c)
# a()



# def em():
#         a=input("Enter your e-mail")
#         if a>="A" and a<="Z":
#                 print("Verify n")
#         if a>="a" and a<="z":
#                 print("verify y")
#         if a=="@" and a=="&" and a=="*":
#                 print("verify m")
#         if a>="1" and a<="100":
#                 print("valid email adreess")
# em()


# Question 1 Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
# Input 
a = [10, 20, 30, 40]
b = [100, 200, 300, 400]
# Output 
# 10 400
# 20 300
# 30 200
# 40 100

# b=[10,20,30,40]
# i=0
# while i<len(a):
#         j=1
#         while j<=len(b):
#                 print([a[i],b[-j]])
#                 j=j+1
#                 i+=1


# def leap():
#         a=int(input("Enter the year"))
#         if a%4==0:
#                 print("leap year")
#         else:
#                 print("not leap year")
# leap()


# n=int(input("enter the number"))
# def num(a):
#         i=0
#         while i<=a:
#                 print(i)
#                 i+=1
# a=int(input("enter the number"))
# num(a)


# # Question 2. Write a program to separate the character and numeric value from a given list and store them in a separate list.
# a=[1,'f',2,'b',3,4,'h','j',6,9,0,'k']
# i=0
# b=[]
# c=[]
# while i<len(a):
#         if type(a[i])!=(int):
#                 b.append(a[i])
#         elif type(a[i])==(int):
#                 c.append(a[i])
#         i+=1
# print(b)
# print(c)


# Question 5 Write a program for sum of this list
# List = [1,2,[3,2,[5,6],3[4]]89,80]

# l = [[1,2],[3,2],[5,6],[3,4],[89,80]]
# i=0
# sum=0
# while i<len(l):
#         j=0
#         while j<len(l[i]):
#                 sum+=l[i][j]
#                 j+=1
#         i+=1
# print(sum)

# Question 6 Write a Python program to find the list in a list of lists whose sum of elements is the highest.
# Sample lists: [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# Expected Output: [10, 11, 12]


# a=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# i=0
# sum=0
# while i<len(a):
#         j=0
#         max=0
#         while j<len(a[i]):
#                 sum+=a[i][j]
#                 if a[j]>max:
#                         max=a[j]
#                         c=j

#                 j+=1
#         i+=1
#         print(sum)
# print(max)        