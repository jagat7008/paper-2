#3. Given a tuple (“Msys”, “Technologies”, “2007”), add “Python” at the end of this tuple and the output should also be in the form of tuple. Make a note that tuples are immutable in nature so you need to find some idea to make modification and print the updated tuple.
s=("Msys", "Technologies", "2007")
s_append = s + ("python",)
print(s_append)
