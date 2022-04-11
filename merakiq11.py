# Write a program to print the top 3 highest values of a given dictionary.
# Input :-

# Output :-

# [58,56,100]

my_dict = {
'a':50, 
'b':58, 
'c':56,
'd':40, 
'e':100, 
'f':20
}
max=0
for i in my_dict:
        if my_dict[i]>max:
                max=my_dict[i]
                max1=0
                for j in my_dict:
                        if my_dict[j]>max1 and my_dict[j]!=max:
                                max1=my_dict[j]
                                max3=0
                                for k in my_dict:
                                        if my_dict[k]>max3 and my_dict[k]!=max1 and my_dict[k]!=max:
                                                max3=my_dict[k]
print(max,max1,max3)