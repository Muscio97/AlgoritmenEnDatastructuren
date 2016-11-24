print('=====================')

a = [45,65,34,82,30,22]
print('a:', a)

# a.sort()
# print('a:', a)

b = sorted(a)
print('origineel:',a)
print('gesorteerd:',b)


print('=====================')

a = [45,65,34,82,30,22]
print('a:', a)

a.sort(reverse=True)
print('a:', a)

print('=====================')

def neg(x):
    return -x

a = [45,65,34,82,30,22]
print('a:', a)

a.sort(key=neg)
print('a:', a)

print('=====================')

a = [45,65,34,82,30,22]
print('a:', a)

a.sort(key=lambda x: -x)
print('a:', a)

print('=====================')

a = ['100','3000','21','20']

print('a:', a)
print('sorted(a):', sorted(a))
print('sorted(a,key=str):', sorted(a,key=str))
print('sorted(a,key=int):', sorted(a,key=int))
print('sorted(a,key=len):', sorted(a,key=len))

print('=====================')

def insertionSort(a):
    for p in range(1,len(a)):
        tmp = a[p]
        j = p
        while j > 0 and tmp < a[j-1]:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp

a = [45,65,340,82,30,2200]
print('a:', a)

insertionSort(a)
print('a:', a)

print('=====================')

def insertionSort2(a, key):
    for p in range(1,len(a)):
        tmp = a[p]
        j = p
        while j > 0 and key(tmp) < key(a[j-1]):
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp

a = [45,65,340,82,30,2200]
print('a:', a)

insertionSort2(a,lambda x: -x)
print('a:', a)

print('=====================')

import timeit
timer = timeit.default_timer

import random

a = [0]*1000
for i in range(1000):
    a[i] = random.randint(0,100000)

t1 = timer()
print('t1:', t1)    
    
insertionSort(a)

t2 = timer()
print('t2:', t2)

print('t2-t1:', t2-t1)

print('=====================')


v = 0

def insertionSort3(a):
    global v
    for p in range(1,len(a)):
        tmp = a[p] ; v += 1
        j = p
        while j > 0 and tmp < a[j-1]:
            a[j] = a[j-1] ; v += 1
            j -= 1
        a[j] = tmp ; v += 1

a = [0]*1000
for i in range(1000):
    a[i] = random.randint(0,100000)

insertionSort3(a)
print('v:', v)


