#11. Write a python function with name reverse_vowel that takes one string as an argument and
#reverse the order of vowels present in the string. The function should return the string having
#reversed order of vowels. For example – If the input string which is given as argument is ‘Hello’
#then the output string should be ‘Holle’. You need to reverse the vowel irrespective of lowercase or
#uppercase.
def reverse_vowels(str1):
	vowels = ""
	for char in str1:
		if char in "aeiouAEIOU":
			vowels += char
	result_string = ""
	for char in str1:
		if char in "aeiouAEIOU":
			result_string += vowels[-1]
			vowels = vowels[:-1]
		else:
			result_string += char
	return result_string
print(reverse_vowels("Hello"))
