"""
--------- Project Euler Problem 4 ----------
https://projecteuler.net/problem=4

Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
i = 999
j = 999
x=0
prevResult = 0
while j > 99 :
    i=999
    
    while i > 99 :
          x=i
          numStr = str(i*j)
          first3 = str(numStr[0:3])
          length = len(numStr)
          last3reverse = str(numStr[length-1]+numStr[length-2]+numStr[length-3])
          if first3 == last3reverse :
              if prevResult < i*j :
                  prevResult = i*j
              break 
          i-=1
    j-=1

print(prevResult)
