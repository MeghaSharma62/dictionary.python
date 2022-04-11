# Write a program to print 'exists' if entered key already exists in the dictionary and
# print 'not exists' if the entered key does not exist.
# Example :-

dict1={"name":"Raju", "marks":56}
n=input("Enter the key:")
# for i in dict1:
if n in dict1:
        print("exists")
else:
        print("not exists")

