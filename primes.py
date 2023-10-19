"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(num):
    if num <= 1: #if number <= 1, not prime (for now?)
        return False

    if num <= 3: #number <= 3, always prime
        return True

    if num % 2 == 0 or num % 3 == 0: #if divisible by 2 or 3, not prime
        return False

    for i in range(2, int(num**0.5)+1): #start counting from 2; number we are counting to is the sqrt of the number we are checking
        if num % i == 0 or num % (i + 2) == 0: #keep counting while square of counting number is <= number we're checking
            return False #not prime
        i+=6
    return True #prime

def primes(number_of_primes):
    list = []
    num = 2  #start with 2

    if number_of_primes <= 0:
        raise ValueError("WARNING: Number of primes should be a positive integer.")

    while len(list) < number_of_primes: #count until enough numbers in list 
        if isPrime(num):
            list.append(num) #if prime, add to list
        num += 1 #next number
    return list