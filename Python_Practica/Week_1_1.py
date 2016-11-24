'''
Created on 21 nov. 2016

@author: MuscioCraft
'''


a = [int(x) for x in input("Uw getal: ")]

def mymax(a):
    max=0
    for i in a:
        assert(i!=0)
        if(i>max):
            max=i
    return max
    

print("Max is", mymax(a))
