'''
Created on 24 nov. 2016

@author: MuscioCraft
'''
from itertools import groupby
a = [0]
b=[0,1]

for i1 in range(max(b)):
    
    a.extend([len(b)])
    b.extend(a)
    print(a, b)



