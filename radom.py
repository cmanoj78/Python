import random, sys
for i in range(5):
    print(random.randint(1,100), end=" ")
          

while True:
    print('Type exit to exit')
    response = input()
    if response == 'exit' :
        sys.exit()
    print('you typed : ', response)

