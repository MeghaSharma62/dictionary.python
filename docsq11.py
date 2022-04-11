# Q11.Write a Python script to merge two Python dictionaries
a={"Megha":90,"Grecy":100}
b={"Shruti":80,"Muskan":70}
c={}
for i in a,b:
        c.update(i)
print(c)