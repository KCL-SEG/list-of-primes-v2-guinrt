"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def checkPrime(num):
    if num == 2:
        return True
    if num > 2:
        for n in range(2, num):
            if (num % n) == 0:
                return False
            else:
                return True

def primes(number_of_primes):
    if(number_of_primes <= 0):
        raise ValueError("You must enter a value greater than 0")
    list = []
    n = 2
    while len(list) != number_of_primes:
        if checkPrime(n):
            list.append(n)
        n +=1

    return list
