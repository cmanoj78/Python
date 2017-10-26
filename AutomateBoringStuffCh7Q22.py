import re
aa2 = re.compile(r'''
    ^(alice | bob | carol)      # first word
    \s                          # space
    (eats | pets | throws)      # second word
    \s                          # separator
    (apples | cats | baseballs) # third word
    \.$                          # end with period.
''',(re.VERBOSE|re.I))





print(aa2.findall('Alice eats two apples.'))
print(aa2.findall('Bob pets cats.'))
print(aa2.findall('Carol throws baseballs.'))
print(aa2.findall('Alice throws Apples.'))
print(aa2.findall('BOB EATS CATS.'))
print(aa2.findall('Robocop eats apples.'))
print(aa2.findall('ALICE THROWS FOOTBALLS.'))
print(aa2.findall('Carol eats 7 cats.'))
