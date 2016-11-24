'''
Created on 21 nov. 2016

@author: MuscioCraft
'''

from random import randrange
from itertools import chain




def how_many():
    a=[]
    b=[]
    c=0
    d=0
    while d<100:
        d=d+1
        for i in range(23):
            a.extend([randrange(1,365)])
            b.extend([randrange(1,365)])
    
        for j in range(1,365):
            if(j in a and j in b):
                c=c+1
        a=[0]
        b=[0]        
    return c


print("Aantal keer dat dagen overeen komen: ",how_many())