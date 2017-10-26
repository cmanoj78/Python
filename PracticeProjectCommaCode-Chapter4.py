"""spam = ['apples', 'bananas', 'tofu', 'cats'] Write a function that
takes a list value as an argument and returns a string with all the
items separated by a comma and a space, with and inserted before the
last item. For example, passing the previous spam list to the function
would return 'apples, bananas, tofu, and cats'. But your function should
be able to work with any list value passed to it."""

def printList(myList):
    returnValue = ""
    
    for i in range(len(myList)):
        if (i==0) :
            returnValue = str(myList[i])

        elif (i == len(myList)-1):
            returnValue = returnValue + ' and ' + str(myList[i])

        else :
            returnValue = returnValue + ', ' + str(myList[i])

    return returnValue

#spam = ['apples', 'bananas', 'tofu', 'cats']
spam = [1,2,3,'s/', 'kuch bhi' ]

print(printList(spam))
