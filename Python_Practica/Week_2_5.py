'''
Created on 1 dec. 2016

@author: MuscioCraft
'''
from random import randint
from pip.commands.search import highest_version
global tmp
tmp = 0

def swap(a,i,j):
    a[i],a[j] = a[j],a[i]


import random

def qsort(a,low=0,high=-1):
    if high == -1:
        high = len(a) -1
    if low < high:
        tmp = low
        low = m

        swap(a,low, random.randint(low,high))
        m = low
        
        for j in range(low+1,high+1):
            if a[j] < a[low]:
                m += 1
                swap(a,m,j)
        
        swap(a,low,m)
        if m > 0:
            qsort(a,low,m-1)
        qsort(a,m+1,high)

def isSorted(a):
    i = 0;
    while i < len(a)-1 and a[i] <= a[i+1]:
        i += 1

    return i == len(a)-1

if __name__ == '__main__':
    ia = [45,65,34,82,30,22]
    print(ia)
    qsort(ia)
    print(ia)

#     dd = [45.0,65.0,34.0,82.0,30.0,22.0]
#     print(dd)
#     qsort(dd)
#     print(dd)
#  
# #    import random
#  
#     a = [0]*1000
#     for i in range(1000):
#         a[i] = random.randint(0,10000)
#     print("a gegenereerd")
#     print(a[500:510])
#     b = list(a)
#  
#     import timeit
#     timer = timeit.default_timer
#  
#     t1 = timer()
#     qsort(a)
#     print(a[500:510])
#     t2 = timer()
#     print(t2-t1)
#     print(isSorted(a))
#  
#     b.sort()
