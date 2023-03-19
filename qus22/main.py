#22. Find the palindrome words with the count value from the given string.Output should be in form of dict. key will be palidrome word and value will be number of occurence. i/p given a string - Nittin & his mom went to a park last friday. His Mom observed that the weather was too cool. Nittin also met his sis. If we reverse the number 1331 then we also get 1331. o/p - {'nittin': 2, 'mom': 2, 'sis': 1, '1331': 2}

def is_palindrome(word):
    return word == word[::-1]

def count_palindrome_words(text):
    words = text.split()
    palindrome_words = {}
    for word in words:
        if is_palindrome(word):
            if word in palindrome_words:
                palindrome_words[word] += 1
            else:
                palindrome_words[word] = 1

    return palindrome_words
text = "Nittin & his mom went to a park last friday. His Mom observed that the weather was too cool. Nittin also met his sis. If we reverse the number 1331 then we also get 1331."
palindrome_words = count_palindrome_words(text.lower())
print(palindrome_words)
