s = 'string'         ; print(s) # omsloten door enkele quoten
s = "nog een string" ; print(s) # omsloten door dubbele quoten
ch = 'a'             ; print(ch) # een karakter
s = ''               ; print('len(s):',len(s)) # de lege string
s = "een string"[4:] ; print(s) # slicing
ch = 'string'[-1]    ; print(ch) # laatste karakter van string
s = "aa'bb"          ; print(s) # bevat enkele quote
s = 'aa"bb'          ; print(s) # bevat dubbele quote
s = 'aa\'bb\"cc'     ; print(s) # bevat enkele en dubbele quote
tekst = """regel 1
regel 2
regel 3"""           ; print(tekst) # meerdere regels
r = r'a\tb'          ; print(r) # letterlijke tekst
s = 'a\tb'           ; print(s) # '\t' wordt niet letterlijk afgedrukt
print(r'a\tb' == 'a\\tb') # r'a\tb' is hetzelfde als 'a\\tb'
print()

s = 'kees'               ; print(s) ; print('id:',id(s))
s.replace('ee','oo')     ; print(s) # s blijft ongewijzigd
s = s.replace('ee','oo') ; print(s) ; print('id:',id(s)) # s wijst nu naar een ander object
print()

s = "lower case"
print(s.upper()) ; print('s:',s)
s = s.upper() ; print('s:',s)
print()

s = "string1" + "string2" ; print(s)
s = "herhaling"*3 ; print(s)
s = "deelstring"[:4] ; print(s)
print()

i = "hoeveel e's in deze niet veelzeggende lange zin".count('e')  ; print(i)
i = "hoeveel en's in deze niet veelzeggende lange zin".count('en'); print(i)
i = "de eerste 'e' in deze zin".index('e')                        ; print(i)
i = "de eerste 'en' in deze veelzeggende zin".index('en')         ; print(i)
i = "de tweede 'en' in deze veelzeggende zin"[12:].index('en')    ; print(i)
print()

s = 'zoek een woord in een regel'
try:
    i = s.index('woord') ; print(i)
except:
    print('not found')
i = s.find('woord')      ; print(i)
i = s.count('woord')     ; print(i)
b = 'woord' in s         ; print(b)
try:
    i = s.index('test')  ; print(i)
except:
    print('not found')
i = s.find('test')       ; print(i)
i = s.count('test')      ; print(i)
b = 'test' in s          ; print(b)
print()

import string
print('whitespace-characters:', string.whitespace.encode())
print()

s = 'string'
a = list(s); print(a)
# alternatief: a = [e for e in s]
print()

s = 'een string met \t white \t\n characters'
a = s.split() ; print(a)
print()

s = 'eenvbstringvbmetvbeenvbseparator'
a = s.split('vb') ; print(a)
print()

s = 'a b  c   d'
a = s.split(' ') ; print(a)
print()

s = 'regel 1\n regel 2\n regel 3'
a = s.split('\n') ; print(a)
# alternatief: a = s.splitlines() ; print(a)
print()

s = 'vb'.join(['een', 'string', 'met', 'een', 'separator'])
print(s)
print()

s = ''.join(['s', 't', 'r', 'i', 'n', 'g'])
print(s)
print()

print('π') # niet via het toetsenbord kun je π intikken
print()

print('\u03c0') # wel via het toetsenbord mogelijk
print()

print('π'.encode('UTF-8'))  # alternatief: print('π'.encode())
                            # defaultencoding: utf-8
print()

import locale
print(locale.getpreferredencoding())
import sys
print(sys.getdefaultencoding())
print()