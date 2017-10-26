#! python3

import pyperclip, re

'''

Project: Phone Number and Email Address Extractor
https://automatetheboringstuff.com/chapter7/

This program is to he boring task of finding every phone number
and email address in a long web page or document copied to clipboard.

'''

# define regex for phone
phRgx = re.compile (r'''(
    (\d{3}|\(\d{3}\))?      # area code
    (\s|-|.)?               # separator
    (\d{3})                 # first 3 digits
    (\s|-|.)?               # separator
    (\d{4})                 # last 4 digits
)''',re.VERBOSE)


# define regex for email 
emailRegex = re.compile(r'''(
       [a-zA-Z0-9._%+-]+      # username
       @                      # @ symbol
       [a-zA-Z0-9.-]+         # domain name
       (\.[a-zA-Z]{2,4})      # dot-something
       )''', re.VERBOSE)

# Get the text off the clipboard.
text = pyperclip.paste()


# Find all phone numbers in the text and store them in a list.
matches = []
PhList = phRgx.findall(text)

for PhNums in PhList :
    number = "-".join([PhNums[1],PhNums[3],PhNums[5]])
    matches.append(number)
    print(number)

# Find all emails in the text and store them in the list.
for emails in emailRegex.findall(text):
    matches.append(emails[0])



# Paste them onto the clipboard.
pyperclip.copy('\n'.join(matches))
print(pyperclip.paste())
   
