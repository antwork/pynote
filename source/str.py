# encoding:utf-8

# len(str) 
s = 'hello China'
print(len(s))

#
# capitalize
# Return a capitalized version of S, i.e. make the first character
#    have upper case and the rest lower case.
print('big city'.capitalize()) # Big city


#encode:utf-8

#
# casefold

# out: **********************value***********************
print('value'.center(50, '*'))

# out: value*********************************************
print('value'.ljust(50, '*'))

# out: *********************************************value
print('value'.rjust(50, '*'))

# out: 2
print('big city'.count('i')) # 2

#
# encode

# out: True
print('hello'.endswith('lo'))

# out:False
print('hello'.startswith('e'))


# print('^ one ^'.expandtabs(32))

#
# expandtabs
#
# find
print('CHINA'.find('I'))    # Found: return index:2
print('China'.find('I'))    # Not Found: return -1

print('CHINA'.index('I'))

try:
    print('China'.index('I'))
except ValueError as e:
    print(e) # substring not found



#
# format
#
# format_map

# isalnum
print('abc'.isalnum())  # True
print('12ab'.isalnum()) # True
print('+'.isalnum())    # False
#
# isalpha
print('abc'.isalpha())  # True
print('123'.isalpha())  # False

# isdecimal
# Return True if there are only decimal characters in S, False otherwise.
# >>> print('0123456789'.isdecimal())
# True
# >>> print('0123456789a'.isdecimal())
# False

# isdigit
#
# isidentifier
#
# islower
#
# isnumeric
#
# isprintable
#
# isspace
#
# istitle
#
# isupper
#
# Out:apple.banana.orange
arr = ['apple', 'banana', 'orange']
print('.'.join(arr))
#
# ljust
#
# lower
#
# lstrip
#
# maketrans
#
# partition
#
# Out: banana is delicious!
src = "orange is delicious!"
print(src.replace('orange', 'banana'))
#
# rfind
#
# rindex
#
# rjust'#
# rpartition'#
# rsplit'#
# rstrip'#
# split'#
# splitlines'#
# startswith'#
# strip'#
# swapcase'#
# title'#
# translate'#
# upper'#
# zfill'

