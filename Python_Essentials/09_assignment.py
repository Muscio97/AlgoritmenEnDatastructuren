i,j,k,d = 10,20,30,40  ; print(i,j,k,d)
t = (i+5,j-4,k*2,d//3) ; print(t) # pack
i,j,k,d = t            ; print(i,j,k,d) # unpack
c1,c2,c3 = 'xyz'       ; print(c1,c2,c3) # unpack string
print()

a = [2,4,6,8] ; print(a)
b = a
b[2] = 22     ; print(a)
print(id(a),id(b))
print()

a = [2,4,6,8] ; print(a)
b = list(a) # alternatief: b = a.copy()
b[2] = 22 ; print(a)
print(id(a),id(b))
print()