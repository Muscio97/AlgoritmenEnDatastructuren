

r = range(10)       ; print(list(r))
r = range(3,10)     ; print(list(r))
r = range(-4,7)     ; print(list(r))
r = range(0,10,2)   ; print(list(r))
r = range(10,3,-1)  ; print(list(r))
r = range(7,-10,-3) ; print(list(r))
print()

for e in range(1,11):
    print(e*e, end = ' ')
print()
a = [e*e for e in range(1,11)] ; print(a)
print()