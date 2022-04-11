dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
b={}
for i in dic:
        if "key" not in dic:
                b.update(dic)
print(b)      