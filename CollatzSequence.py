""" This program is to create a Collatz Sequence """

def collatz(number) :
    result = 0
    if (int(number))% 2 == 0 :
        result = number // 2
    else :
        result = 3 * number + 1

    print (result)
    return result

newNumber = 0
while newNumber <= 0:
    print ('Enter a number > 0 ', end= " : ")
    try :    
        newNumber = int(input())
    except :
        print('Pls enter only integer value')
    
while True :
    newNumber = collatz(newNumber)
    if newNumber == 1 :
        break
       

    
