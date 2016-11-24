t = (1,3,5) ; print(t)
a = list(t) ; print(a) # tuple → list
a.reverse() ; print(a) # t.reverse() is niet toegestaan
t = tuple(a); print(t) # list → tuple
t = (1,3,5) ; print(t)
t = t[::-1] ; print(t) # t wijst nu naar een ander tupel-object
print()