'''
Created on 28 nov. 2016

@author: MuscioCraft
'''
from Week_2_2 import Mystack
stack = Mystack()

class Checker():

    def equal_check(temp):
        falid = 1
        for element in temp:
            if(element =='(' or element =='<' or element =='['):
                stack.push(element)
            if(element ==')' or element =='>' or element ==']'):
                if(element ==')'):
                    if(stack.peek()=='('):
                        stack.pop()
                    else:
                        falid = 0
                        return falid, "False"
                if(element ==']'):
                    if(stack.peek()=='['):
                        stack.pop()
                    else:
                        falid = 0
                        return falid, "False"          
                if(element =='>'):
                    if(stack.peek()=='<'):
                        stack.pop()
                    else:
                        falid = 0
                        return falid, "False"
        if(stack.isEmpty()<=0):
            return falid, "True"
        else:
            return Checker.equal_check(temp)

print(Checker.equal_check(input("String: ")))