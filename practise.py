import re

phRegEx = re.compile(r'(\(?\d\d\d\)?)-?(\d\d\d-?\d\d\d\d)')
matchObj = phRegEx.search('my number is 9253656677')
print(matchObj.groups())
print(matchObj.group(1))
print(matchObj.group(2))
print(matchObj.group(0))


heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Spiderman.')

print(mo1.group()
)
mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

print(heroRegex.findall('Tina Fey and Batman'))

nameRegEx = re.compile(r'First Name : (.*) Last Name : (.*)')
mo = nameRegEx.search('First Name : Manoj Last Name : Choudhary')
print(mo.groups())

nameRegEx = re.compile(r'<.*>')
mo = nameRegEx.search('<To serve man> for dinner>')
print(mo.group())

nameRegEx = re.compile(r'<.*?>')
mo = nameRegEx.search('<To serve man> for dinner>')
print(mo.group())

agentNameRegex = re.compile(r'Agent (\w)(\w)\w*')
print(agentNameRegex.sub(r'\1\2****','Agent Alex gave the docs to Agent Bob'))




emailRegex = re.compile(r'''(
       [a-zA-Z0-9._%+-]+      # username
       @                      # @ symbol
       [a-zA-Z0-9.-]+         # domain name
       (\.[a-zA-Z]{2,4})      # dot-something
       )''', re.VERBOSE)


mo=emailRegex.search('manoj.choudhary@fisglobal.com')
print(mo.groups())

dict1 = {"key1":"Val1", "key2":"Val2"}
print(dict1.keys())

#######################
print('------url regex test ---------')
# urlRegex = re.compile(r'http[s]?://(\S*?)([("|\s)?])')
urlRegex = re.compile(r'http[s]?://(\S*?)[("|\s)?]')
searchText = 'ghjk "https://www.fis.com"124354 http://infosys.com"'
print('findall result :')
print(urlRegex.findall(searchText))
print('search result:')
print (urlRegex.search(searchText))

#######################

print('-------- file operations ---------')

print('reading file - C:\Manoj\Personal\Edu\Python\Hello.txt')
helloFile = open(r'C:\Manoj\Personal\Edu\Python\Hello.txt')

print('print file using read()')
print (helloFile.read())

'''
to print again close and reopen file. or comment above read.
Once read the pointer goes to end of file so next readlines wont return anything
'''
#print('print file using readlines()')
#print (helloFile.readlines())

print('close file')
helloFile.close()

''' WRITE TO A FILE '''

helloFile = open(r'C:\Manoj\Personal\Edu\Python\Hello.txt','a')
print('appending to file now.')
helloFile.write('\nThis text was appended using python program')
helloFile.close()
print('file closed. check appended text in file.')



########################
