# Q14.Write a Python program to multiply all the items in a dictionary.

a={1:20,2:30,3:40,4:50}
prod=1
prod1=1
for i,j in a.items():
        prod*=i
        prod1*=j
        b=prod*prod1
print(b)