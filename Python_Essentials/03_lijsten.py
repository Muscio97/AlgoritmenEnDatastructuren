a = [1,99,2,98,3,97]
print(a[-1])
print(a[-3])
print()

a1 = [1,2,3]
a2 = [101,102,103]
print(a1+a2)
print()

a1 = [1,2,3]
a2 = [101,102,103]
print(4*a1)
print(a2*3)
print()

n = 25
b = [0]*n
print(b)
print()

a = [1,2,3,4,5,6,7,8]
del a[6] ; print(a)   # verwijder het zevende element
del a[1:3] ; print(a) # verwijder het 2e en het 3e element
del a[:2] ; print(a)  # verwijder de eerste twee elementen
del a[1:] ; print(a)  # verwijder alle elementen behalve het eerste element
del a[:] ; print(a)   # verwijder alle elementen
print()

a = [1,2,3,2,1] ; print(a)
a.remove(2) ; print(a)  # alternatief:
                        # del a[b.index(2)]
print()

a = [1,2,3,2,1,2,3,2,1] ; print(a)
while 2 in a:
    a.remove(2) ; print(a)
print()

a = [1,2,3,4,5,6,7,8] ; print(a)
a[2] = 99 ; print(a)
print()

a = [1,2,3,4,5,6,7,8] ; print(a)
a[1:3] = [88]         ; print(a) # a[1:3] = 88 niet toegestaan
a[1:3] = [77,177,277] ; print(a)
a[2:5]= []            ; print(a)
print()

a = [1, 1, 1, 1]   ; print(a)
a.insert(0,6)      ; print(a) # voor de lijst plaatsen
a.insert(3,7)      ; print(a) # toevoegen voor het element met positie 3
a.insert(len(a),8) ; print(a) # achter de lijst plaatsen
a.append(8)        ; print(a) # methode 2
a = a + [8]        ; print(a) # methode 3
print()

a = [1, 1, 1, 1]    ; print(a)
a[:0] = [6,66]      ; print(a) # voor de lijst plaatsen
a[4:4] = [7,77]     ; print(a) # toevoegen voor het element met positie 3
a[len(a):] = [8,88] ; print(a) # achter de lijst plaatsen
a.extend([8,88])    ; print(a) # methode 2
a = a + [8,88]      ; print(a) # methode 3
print()

print(min([6,3,5,9]))
print(min('noot','aap','mies'))
print(min('102','13'))
print()

a = [1,-2,3,-4,1,-2,3,-4] ; print(a)
a.sort()                  ; print(a)
a.sort(reverse = True)    ; print(a)
a.reverse()               ; print(a)
i = a.pop()               ; print('na pop-aanroep: i:',i,'a:',a)
i = a.pop(2)              ; print('na pop(2)-aanroep: i:',i,'a:',a)
print(a.count(-4))
print(a.index(1))
print()
