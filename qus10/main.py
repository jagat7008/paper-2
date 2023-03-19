#10. In the given String -- ‘MsYs TecHNOlogiEs iS a gREat place To woRk’ find the count of lowercase and uppercase letters. 
Str=input("enter a string:")
lower=0
upper=0
for i in Str:
	if(i.islower()):
			lower+=1
	else:
	    upper+=1
print("number of lowercase is:",lower)
print("number of uppercase is:",upper)
