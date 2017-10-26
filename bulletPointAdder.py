#! python3
"""
ADDING BULLETS TO WIKI MARKUP
add bullet points to list of regular text lines from clipboard.
eg lines

Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars


"""

import sys, pyperclip
    

text = pyperclip.paste().strip()
lines = text.split('\n')


for i in range(len(lines)):
    lines[i] = "* " + lines[i]
    print(lines[i])

text = '\n'.join(lines)

pyperclip.copy(text)
