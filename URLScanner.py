#! python3

import re, pyperclip
'''

URL scanner
from the clipboard Find website URLs that begin with http:// or https://.

'''

# urlRegex = re.compile(r'http[s]?://(\S*?)["|\s]')
urlRegex = re.compile(r'http[s]?://(\S*?)([("|\s)?])')

text = pyperclip.paste()

urlList = urlRegex.findall(text)
matches=[]
for url in urlList :
    matches.append(url[0])


text = '\n'.join(matches)
print(text)



