#21. You are given a string and width. Your task is to wrap the string into paragraph of width in reverse order. Blank spaces should be ignored. for eg: i/p - first line contains a string with blank spaces - Hello, welcome to this organisation. the second line conatins the width - 4 o/p lleH 
                             #ew,o 
                             #mocl 
                             #tote 
                             #osih 
                             #nagr 
                             #tasi 
                             #.noi

string = "Hello, welcome to this organisation."
width = 4
string = string[::-1].replace(" ", "")
paragraphs = [line[::1] for line in [string[i:i+width] for i in range(0, len(string), width)][::-1]]
for line in paragraphs:
    print(line)
