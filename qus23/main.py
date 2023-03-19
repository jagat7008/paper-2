#23. create 2 dictionaries as follows:
#dict1 = {'name': 'Msys', 'Place': 'Pune'}
#dict2 = {'EmpID': 0001, 'Salary': 50000}
#Perform following operations:
#a. create single dictionary by merging dict1 & dict2
#b. update the salary to 10%
#c. update age to 35
#d. extract & print all the values & keys separetly in tuple.
#e. delete the element with key 'Age' & print the dictionary elements.
dict1 = {'name': 'Msys', 'Place': 'Pune'}
dict2 = {'EmpID': 1, 'Salary': 50000}

dict1.update(dict2)
print(dict1)
salary = dict1['Salary']
dict1['Salary'] = salary + (salary * 0.1)
print(dict1)
dict1['Age'] = 35
print(dict1)
keys = tuple(dict1.keys())
values = tuple(dict1.values())

print("Keys: ", keys)
print("Values: ", values)
del dict1['Age']
print(dict1)
