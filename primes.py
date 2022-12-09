"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

def checkPrime(num):
    if num == 2:
        return True

    for i in range(2, int(math.sqrt(num) + 1)):
        if (num % i == 0):
            return False
    return True

def primes(number_of_primes):
    if(number_of_primes <= 0):
        raise ValueError("Please enter a number larger than 0")
        return

    list = []
    i = 2

    while(len(list) < number_of_primes):
        if checkPrime(i):
            list.append(i)

        i += 1
    return list
