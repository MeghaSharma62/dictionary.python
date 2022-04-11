# Write a program to sort a dictionary in ascending or descending according to its
# values .
# Input :-
import operator
d={'bijender':45,'deepak':60,'param':20,"anjili":30,'roshini':50}

# Expected result in Ascending Order:

# {'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}
# Expected result in Descending Order:

# {'deepak':60,'roshini':50,'bijender':45,'anjili':30,'param':20}



# a={'bijender':45,'deepak':60,'param':20,"anjili":30,'roshini':50}
# for i in sorted (a.keys()) :
#              print(i, end = " ")
# # print(a)


print('Original dictionary : ',d)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)