# Write a program such that the below given dictionariesare into a single 
# dictionary and add the values having same key.

# Output={1: 10, 2: 60, 3: 30, 5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
# b={}
for i in dic2:
        if i in dic1:
                dic1[i]=dic1[i]+dic2[i]
                dic1.update(dic3)
        else:
                dic1[i]=dic2[i]
print(dic1)
