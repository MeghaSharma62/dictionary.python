# a=int(input("Enter the starting number:"))
b=int(input("Enter ending number:"))
c={}
for i in range (1,b+1):
        c.update({i:i**2})
print(c)