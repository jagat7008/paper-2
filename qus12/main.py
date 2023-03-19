#12. Write a method number_of_prime_numbers() which takes two input arguments num1 and
#num2 and should return the total number of prime numbers in the range. The numbers num1 and
#num2 are inclusive of the range. Also add all the numbers in an empty list and return the sum of the
#list. So finally your function will return two things, first will be the count of prime numbers and the
#other will be the sum of all the prime numbers in the given range.
def number_of_prime_numbers(num1, num2):
    primes = []
    count = 0
    for num in range(num1, num2+1):
        if num > 1:
            for i in range(2, int(num**(0.5))+1):
                if (num % i) == 0:
                    break
            else:
                count += 1
                primes.append(num)
    return count, sum(primes)
print(number_of_prime_numbers(1,10))
