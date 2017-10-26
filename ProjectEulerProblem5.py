"""
--------- Project Euler Problem 5 ----------

https://projecteuler.net/problem=5

Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

--------------------------------------------
"""
    
'''
isPrime(num):
This function is to check if the argument is a prime number

'''
def isPrime(num):
    for j in range(2,(num//2)+1):
        if num%j == 0:
            return False
    return True


'''
firstPrimeFactor(num):
This function returns the first prime factor of the passed argument
'''

def firstPrimeFactor(num):
    for i in range(2,(num//2)+1):
        if (num%i==0) and isPrime(i):
            return i
    return num
            

'''
allPrimeFactors(num):
This function provides all the prime factors for an given argument.
'''
def allPrimeFactors(num):
    lstPrimeFactors=[]
    while num > 1:
        temp = firstPrimeFactor(num)
        lstPrimeFactors.append(temp)
        num = int(num / temp)
    return lstPrimeFactors



'''----------------------

Program to find LCM for all numbers from 1 through 20.

-------------------------'''



allPrimeMultiples=[]
for q in range(2,21):
    newList = allPrimeFactors(q)
    newList.sort()
    allPrimeMultiples.sort()
    for v in newList :
        while (newList.count(v) > allPrimeMultiples.count(v)) :
            allPrimeMultiples.append(v)

LCM = 1
for v in allPrimeMultiples:
    LCM*=v
print ('LCM of all numbers from 1 to 20 is ',LCM)




