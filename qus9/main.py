#9. Given a list [1,2,1,5,9,10,2,2,7,5,3,10,8,9,15,17,21,16,17,90] find the difference between the length of the list and the count of unique elements in the list
list = [1,2,1,5,9,10,2,2,7,5,3,10,8,9,15,17,21,16,17,90]
unique_count = len(set(list))
print("Unique data:",unique_count)
difference = len(list) - unique_count
print("Difference between length of list and count of unique elements:", difference)
