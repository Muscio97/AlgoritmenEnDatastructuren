'''
Created on 28 nov. 2016

@author: MuscioCraft
'''


def mybin(x):
    hello = ""
    assert type(x) == int
    
    
    if(x==0):
        return '0'
    
    elif(x==1):
        return '1'
    else:
        return hello + str(mybin(x//2)) + str(x % 2)
        
        
print(mybin(2**64))