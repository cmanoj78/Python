x=500 # assign number greater than 2

def listPrimeNumTill(x) :
   for n in range (2,x):
        for i in range(2,((n//2))+1):
            if n % i == 0 :
                print( n , 'equals', i , '*', n//i)
                break

        else :
            print (n , 'is a prime number')



        
listPrimeNumTill(11)
