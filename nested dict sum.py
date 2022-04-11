a={1:{3:30,7:10},
   2:{4:40,5:20}}
sum=0
for i in a.values():
   for j in i.values():
      sum+=j  
print(sum)

# prod=1
# for i in a.values():
#    for j in i.values():
#       prod*=j
# print(prod)``