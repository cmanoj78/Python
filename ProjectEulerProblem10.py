'''
Summation of primes
Problem 10 
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''

x=3
lstP=[2]
isPrime=False
while x<2000000 :
    #print('x=',x)
    isPrime=True
    print
    for i in lstP :
        if (x>=i/2)and(x%i==0):
            isPrime=False
            break

    if isPrime :
        lstP.append(x)
        #print('added prime ',x)
    x+=1

print(sum(lstP))

# Ans 142913828922
