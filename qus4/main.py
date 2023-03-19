#4. In the dictionary {‘India’:’New Delhi’, ‘USA’:’Washington D.C.’, ‘Nepal’:’Kathmandu’} list out
#all the keys in a list named as ‘list_keys’ and list out all the values in a list named as ‘list_values’.
#Also find out the value of key ‘Australia’ in the list and as it is not existing in the list print ‘NA’ as
#its value.    
dictionary = {'India': 'New Delhi', 'USA': 'Washington D.C.', 'Nepal': 'Kathmandu'}  
list_keys = list(dictionary.keys())             
list_values = list(dictionary.values())         

print("The keys are:", list_keys)           
print("The values are:", list_values)        
key = input("Enter the Value: ")                 
value = dictionary.get(key, 'NA')               
print("The value of", key, "is", value)
