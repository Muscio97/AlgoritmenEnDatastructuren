'''
Created on 21 nov. 2016

@author: MuscioCraft
'''

from itertools import groupby

a = []
a.extend(range(2, 1001))


def priem(a):
    b=[]
    d=[2,3]
    e=len(d)
    for t in range(e):
        
        print(d)
        for i in a:
            for j in d:
                if(i%j!=0):
                    b.extend([i])
        #--------------------------------------------------
        c = [len(list(group)) for key, group in groupby(b)]  
        #maakt lijst met hoe vaak alle elemneten in c voorkomen 
        #http://stackoverflow.com/questions/2161752/how-to-count-the-frequency-of-the-elements-in-a-list
        #--------------------------------------------------
        for k in range(len(c)):
            if(c[k]==e):
                d.extend([a[k]])
                

    return d
            
print(priem(a))

