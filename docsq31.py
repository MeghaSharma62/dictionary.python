# Q31.. Write a Python program to get the top three items in a shop. Go to the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3


my_dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# print({"keys:values"})
max=0
for i in my_dict:
        if my_dict[i]>max:
                max=my_dict[i]
                a=i
                max1=0
                for j in my_dict:
                        if my_dict[j]>max1 and my_dict[j]!=max:
                                max1=my_dict[j]
                                b=j
                                max3=0
                                for k in my_dict:
                                        if my_dict[k]>max3 and my_dict[k]!=max1 and my_dict[k]!=max:
                                                max3=my_dict[k]
                                                c=k
print(a,max,b,max1,c,max3)
