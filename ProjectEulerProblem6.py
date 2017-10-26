'''
Sum square difference
Problem 6 
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
'''

def sumOfSquares(num):
    if num==1:
        return 1
    else :
        return (num**2)+sumOfSquares(num-1)

numsum = 0
def sumFromOneToNum(num):
    if num==1:
        numsum = 1
    else :
        numsum = (num)+ sumFromOneToNum(num-1)
         
    return numsum


print ((sumFromOneToNum(100))**2 - sumOfSquares(100))


