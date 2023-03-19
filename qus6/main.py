#6. Write a program to extract the words starting with lowercase letters present in the list. [‘Nissan’, ‘maruti’, ‘hyundai’, ‘Volkswagen’, ‘audi’] 
list=["maruti", "hyundai", "Volkswagen", "audi"]
lowers = [l for l in list if l.islower()]
print (' '.join(lowers))
