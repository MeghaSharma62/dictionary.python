b={}
i=0
while i<=10:
        name=input("Enter the name:")
        marks=int(input("enter the marks:"))  
        b.update({name:marks})
        i+=1
print(b)