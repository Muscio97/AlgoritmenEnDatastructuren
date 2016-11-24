i = 0
try:
    x = 1/i
except:
    print('je kunt niet door nul delen')
print()

import sys
i = 0
try:
    x = 1/i
except:
    print(sys.exc_info())
print()

i = 0
try:
    x = 1/i
except ZeroDivisionError as error_info:
    print(error_info)
print()