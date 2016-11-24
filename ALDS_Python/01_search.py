a = [45,65,34,82,30,22]
x = 30

a.index(x)

print('a.index(x):', a.index(x))

def sequentialSearch1(a,x): # a is een lijst, x is het gezochte element
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

i = sequentialSearch1(a,x)
print('i:', i)

def sequentialSearch2(a,x): # a is een lijst, x is het gezochte element
    i = 0
    for e in a:
        if e == x:
            return i
        else:
            i += 1
    return -1

i = sequentialSearch2(a,x)
print('i:', i)

enum = enumerate(a)
print(list(enum))
print(list(enum))

def sequentialSearch3(a,x): # a is een lijst, x is het gezochte element
    enum = enumerate(a)
    for i,v in enum:
#        print(i,v)
        if v == x:
            return i
    return -1

i = sequentialSearch3(a,x)
print('i:', i)

print('=====================')

def binarySearch(a,x): # a is een lijst, x is het gezochte element
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = ( low + high ) // 2 # gehele deling
        if a[mid] < x:
            low = mid + 1
        elif a[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

print('a:', a)
a.sort()
print('a:', a)

i = binarySearch(a,x)
print('i:', i)
i = binarySearch(a,65)
print('i:', i)

