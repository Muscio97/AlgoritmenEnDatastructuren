import sys
print(sys.platform)

from sys import platform # of from sys import *
print(platform)

import sys as s
print(s.platform)

print()

print(dir(sys)) # lijst met items
print(vars(sys))