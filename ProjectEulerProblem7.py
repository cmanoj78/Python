'''
10001st prime
Problem 7 
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
'''

lstPrimes = [2, 3, 5, 7, 11, 13]
n=14
while len(lstPrimes) < 10001 :
    #print("n=",n)
    isPrime = True
    for i in lstPrimes:
        #print("i=",i)
        if n % i == 0:
            #print(n, " is divisible by ",i)
            n+=1
            isPrime=False
            break
        
    if isPrime :
        print('adding', len(lstPrimes)+1, 'prime : ',n)
        lstPrimes.append(n)

print (n)        
        

