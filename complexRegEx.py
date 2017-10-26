import re
phR = re.compile("""(
    (\d{3}|\(\d{3}\))?             # optional area code
    (\s|-|\.)?                     # separator
    \d{3}                          # first 3
    (\s|-|\.)?                     # separator
    \d{4}                          # last 4
    (\s*(ext|x|ext.)\s*\d{1,5})?   #extension
    

)""",re.VERBOSE)


print(phR.search('my phone number is : (925)3656677ext 1250').group())
