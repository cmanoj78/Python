'''
Special Pythagorean triplet
Problem 9 
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''

c=998
a=1
b=1
found=False
while c>=2 :
    print('c=',c)
    if True :
        b = 1
        a=1000-c-b
        while a>=b :
            #print('a=',a,' b=',b)
            if (a**2)+(b**2) == (c**2) :
                found=True
                print(a,b,c)
                print(a*b*c)
                break
            else :
                a-=1
                b+=1
            

    if found :
        break
    c-=1


