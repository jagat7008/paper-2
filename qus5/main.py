#5. Given a dictionary {‘Msys Technologies’:’Sanjay Sehgal’, ‘Infosys’:’Salil Parekh’, ‘TCS’:’Rajesh Gopinathan’, ‘Wipro’:’Thierry Delaporte’} make a list of all the values associated with keys in alphabetically sorted order. 
dict = {"Msys Technologies":"Sanjay Sehgal", "Infosys":"Salil Parekh",
"TCS":"Rajesh Gopinathan", "Wipro":"Thierry Delaporte"}
keys = list(dict.keys())
keys.sort()
sorted_dict = {i: dict[i] for i in keys}
print(sorted_dict)
