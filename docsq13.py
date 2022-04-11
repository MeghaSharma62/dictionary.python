# Q13.Write a Python program to sum all the items in a dictionary.

a={1:20,2:30,3:40,4:50}
# sum=0
# sum1=0
# for i in a:
#         sum+=a[i]
#         # sum1+=a
# print(sum)
        

# sum=0
# for i in a.keys():
#         sum+=i
#         sum1=0
#         for j in a.values():
#                 sum1=sum1+j
#                 total=sum+sum1
# print(total)

sum=0
sum1=0
for i,j in a.items():
        sum+=i
        sum1+=j
        a=sum+sum1
print(a)