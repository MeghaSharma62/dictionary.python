# Q2. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}




s='w3resource'
a=list(s)
i=0
b=[]
while i<len(a):
        j=0
        b1=[]
        count=0
        while j<len(a):
                if a[i] in a:
                   if a[i]==a[j]:
                        count+=1
                   j+=1
        b1.append(a[i])
        b1.append(count)
        if b1 not in a:
                b.append(b1)
        i+=1
print(dict(b))

