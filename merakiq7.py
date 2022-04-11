# Take a list having dictionary elements as shown below (Sample Data) and then store
# all the unique values into a list and print.
# Example :-
# Input :-

dict=[{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
# i=0
b=[]
for i in range(len(dict)):
        for j in dict[i].values():
                # print(j)
                if j not in b:
                        b.append(j)
print(b) 





   