"""
--------- Project Euler Problem 3 ----------
https://projecteuler.net/problem=3

Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def isPrime(num):
    for i in range(2,(num//2)+1):
       if num%i == 0:
           return False

    return True


bignum = 600851475143
# 600851475143
LPF = 1
for i in range(2,(bignum//2)+1):
    if isPrime(i):
        if bignum%i ==0:
            LPF = i
            print(i)
    
print(LPF)



