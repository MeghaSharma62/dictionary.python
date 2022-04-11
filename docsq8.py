# Q8. Write a Python program to check whether a given key already exists in 
# a dictionary.
# a={"name":"shruti","marks":45}
a={25:67,98:56}
n=int(input("enter the key"))
if n in a:
        print("Exists")
else:
        print("not exists")