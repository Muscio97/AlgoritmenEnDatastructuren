'''
Created on 21 nov. 2016

@author: MuscioCraft
'''

a = "een123zin45 6met-632meerdere+7777getallen"

def getNumbers(s):
   b = [i for i in a if i.isdigit()] 
   return b
#nog geen spaces
        
print(getNumbers(a))      