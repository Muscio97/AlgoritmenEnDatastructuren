'''
Created on 24 nov. 2016

@author: MuscioCraft
'''
from itertools import groupby
a = [1,2,3,4,5,6,7,8,9,10]
b=[]

for i1 in a:
    for i2 in a:
        for i3 in a:
            for i4 in a:
                for i5 in a:
                    b.extend(a)

c = [len(list(group)) for key, group in groupby(b)]
print(c)