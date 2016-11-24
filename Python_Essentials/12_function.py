def som(x,y):          # definitie van functie , x en y zijn formele parameters
    z = x+y            # z is een lokale variabele
    return z           # de waarde z wordt teruggegeven

print(som(2,3))        # de waarde z wordt teruggegeven
print(som('aap','je')) # parameters zijn van type 'string'
a =3
b = 1e100              # a en b zijn globale variabelen
print(som(a,b))        # Deze worden toegekend aan de formele parameters.
print()

a = 3 # a is globaal
b = 7 # b is globaal
def g(x,y):
    z = x+y # z is lokaal
    print('locals:', locals().keys())
    print('globals:', globals().keys())
    return z

print(g(a,b))
print()

a = 3 # a is globaal
b = 7 # b is globaal
def g2(x,y):
    a = 55
    print('a = ',a)
    z = x+y
    print('locals:', locals().keys())
    print('globals:', globals().keys())
    return z

print(g2(a,b))
print()
print('a =',a)
print()

a = 3 # a is globaal
b = 7 # b is globaal
def g3(x,y):
    global a
    a = 55
    print('a =',a)
    z = x+y
    print('locals:', locals().keys())
    print('globals:', globals().keys())
    return z

print(g3(a,b))
print()
print('a =',a)
print()

def doeNiets(i): pass # doe niets

x = doeNiets(0)
print(x)
print()

def myabs(i):
    if i < 0:
        return -i
    return i

print(myabs(-3))
print(myabs(6))
print()

def printTafelVanVijf():
    for i in range(1,11):
        print(i,'keer 5 is',5*i)
printTafelVanVijf()
print()

def f(i):
    i *=2
    return i

j = 4;
print(f(j))
print(j) # j blijft ongewijzigd
i = 5
print(f(i))
print(i) # i blijft ongewijzigd
print()

def g4(a):
    a = [4,5,6]
    print(a)
    
a = [4,2,6,1]
print('vooraf:', a)
g4(a)
print('achteraf:', a) # a blijft ongewijzigd.
print()

def h(a):
    a[1] = 25
    print(a)

a = [4,2,6,1]
print('vooraf:',a)
h(a)
print('achteraf:',a) # een element van a is gewijzigd
print()

def machten(i):
    return i*i,i*i*i,i*i*i*i # of return (i*i,i*i*i,i*i*i*i)

u,v,w = machten(5)
print(u,v,w)
print(machten(6)[1])
t = machten(2)
print( t[-1])
u,v,w = t
print( u,v,w)
print()

def f5(i,t=0,h=0):
    return i + 10*t + 100*h

print(f5(3))         # t == 0, h == 0
print(f5(3,4))       # h == 0
print(f5(3,4,5))
print()
print(f5(1,t=9))     # h == 0
print(f5(1,h=2))     # t == 0
print(f5(1,t=9,h=7))
print(f5(1,h=8,t=5)) # t en h mogen
print()

def product(*args):
    product = 1
    for i in args:
        product *= i
    return product

print(product())
print(product(1))
print(product(1,2))
print(product(1,2,3))
print(product(1,2,3,4))
print()

a = [34,35,36,37]
print(product(a[0],a[1],a[2],a[3]))
print(product(*a)) # hetzelfde als product(a[0],a[1],a[2],a[3])
