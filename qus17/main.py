#17. Write a program to replace duplicate adjacent alphabets from given string with ‘_’.
#For Example -- input given string : 'abcdaa hssbbye' and output : ‘abcda_ hs_b_ye’
def replace_duplicates(string):
    new_string = string[0]  
    for i in range(1, len(string)):
        if string[i] == string[i-1]:   
            new_string += '_'  
        else:
            new_string += string[i]  
    return new_string
input_string = 'abcdaa hssbbye'
output_string = replace_duplicates(input_string)
print(output_string)  
