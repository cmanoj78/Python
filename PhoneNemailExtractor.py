"""
PhoneNemailExtractor

Get the text off the clipboard.(ctrl+a on a web page)
Find all phone numbers and email addresses in the text.
Paste them onto the clipboard.

"""

import re
import pyperclip

# define regex for phone number
phoneRegEx = re.compile("""(
    (\d{3}|\(\d{3}\))?             # optional area code
    (\s|-|\.)?                     # separator
    (\d{3})                          # first 3
    (\s|-|\.)?                     # separator
    (\d{4})                          # last 4
    (\s*(ext|x|ext.)\s*(\d{1,5}))?   #extension
    

)""",re.VERBOSE)

# define regex for email
emailRegEx = re.compile(r'(\w+(\.\w*)*@\w+\.\w{3})')

# copy the text from clipboard
text = pyperclip.paste()
# parse the copied clipboard text for phone
phoneNums = phoneRegEx.findall(text)

# print phone numbers found if any
matches = []
matches.append('List of Phone Nums : ')
for groups in phoneNums :
    phNum = "-".join([groups[1].strip('()'),groups[3],groups[5]])
    if groups[8] != '' :
        phNum += ' x '+ groups[8]
    matches.append(phNum)


matches.append('List of emails : ')

# parse the copied clipboard text for email number
emailList = emailRegEx.findall(text)
for groups in emailList :
    matches.append(groups[0])


print('\n'.join(matches))
