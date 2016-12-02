'''
Created on 28 nov. 2016

@author: MuscioCraft
'''
from inspect import stack

class Mystack:
    
    def __init__(self):
        self.stack = []
    
    def push(self,item):
        self.stack.extend([item])
        
    def pop(self):
        if(len(self.stack) > 0):
            temp = self.stack[-1]
            del self.stack[-1]
            return temp
        return 0
    
    def peek(self):
        if(len(self.stack) > 0):
            return self.stack[-1]   
        return 0
    
    def isEmpty(self):
        return len(self.stack)
    
    
TBN = Mystack()
TBN.push('M')
print(TBN.peek())
TBN.push('i')
print(TBN.peek())
TBN.push('k')
print(TBN.peek())
TBN.push('e')
print(TBN.peek())




