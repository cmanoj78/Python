#! python 3

import re

'''
Remove sensitive information such as Social Security or credit card numbers.


'''

# ssnRegex = re.compile(r'\d{3}(\s|-)? \d{2}(\s|-)? \d{4}')
ssnRegex = re.compile(r'\d{3}(\s|-)? \d{2}(\s|-)? \d{4}', re.VERBOSE)
CCRegex = re.compile(r'(\d{4} (\s|-)?){3} \d{4}',re.VERBOSE)

text = ' SSN is 123-45-6789 and the cc is 1324-1344-1235-1235'

print(CCRegex.sub('xxxx-xxxx-xxxx-xxxx',ssnRegex.sub('xxx-xx-xxxx', text)))
