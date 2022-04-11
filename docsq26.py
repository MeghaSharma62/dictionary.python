dict1 = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
print("{:<10} {:<10} {:<10} ".format("a","b","c"))
for key,value in dict1.items():
        a,b,c=value
        print(("{:<10} {:<10} {:<10} ".format(a,b,c)))

