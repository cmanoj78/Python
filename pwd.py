#! python3

# pwd.py - This is an insecure password locker program

PASSWORDS = {'gmail' : "gmail pwd",
             'yahoo' : "yahoo pwd",
             'c2p' : 'c2p pwd',
             'fis' : 'fis pwd'}

import sys, pyperclip

if (len(sys.argv) != 2) :
        print ('Usage : pwd.bat <account name>')
        sys.exit()

account = str(sys.argv[1])

if account in PASSWORDS :
    pyperclip.copy(PASSWORDS[account])
    print ('Password copied to clipboard')
else :
    print ('Password not found')

    
