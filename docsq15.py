# Q15.Write a Python program to remove a key from a dictionary.
dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
# if "ball" in dic:
#         del (dic["ball"])
# print(dic)

a=input("enter the key name")
if a in dic:
        del(dic[a])
print(dic)