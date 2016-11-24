def showfreq(f):
    for i in range(len(f)):
        print(str(m[i])+':'+str(f[i]),end=' ')
    print()

def topdown_first(n):
    assert(n>0)
    i=0
    while i < len(m) and m[i] <= n: i +=1
    if i == len(m):i -= 1
    if m[i] > n: i-=1
    f = [0]*(i+1)
    while i >= 0:
        f[i] = n//m[i]
        n %= m[i]
        i -= 1
    return [f,n]

def topdown_next(t):
    f,r = t
    if len(f) == 1: f.pop()
    else:
        i=1
        while f[i] == 0: i+=1
        f[i] -= 1
        if f[i] == 0 and i == len(f)-1: f.pop()
        n = r + m[0]*f[0] + m[i]
        i-=1
        while i>=0:
            f[i] = n//m[i]
            n %=m[i]
            i-=1
        t[0] = f
        t[1] = n

m = [1,2,5]
i = 0
t = topdown_first(7)

while t[0]:
    if not t[1]:
        i += 1
        print(str(i)+':',end=' ')
        showfreq(t[0])
    else:
        showfreq(t[0])
    topdown_next(t)

print('==================')

def buttomup_first(n):
    assert(n>0)
    f = [n//m[0]]
    r = n%m[0]
    return [f,r]

def buttomup_next(t):
    f,r = t
    n2 = r + m[0]*f[0]
    i = 1
    while i < len(f) and i < len(m) and n2 < m[i]:
        n2 += m[i]*f[i]
        i += 1
    if i == len(m) or n2 < m[i]:
        while f: f.pop()   # f == []
    else:
        if i == len(f): f.append(1)
        else: f[i] += 1
        f[0] = (n2-m[i])//m[0]
        for j in range(1,i): f[j]= 0
        t[0] = f
        t[1] = (n2-m[i])%m[0]

m = [1,2,5]
i = 0
t = buttomup_first(7)

while t[0]:
    if not t[1]:
        i += 1
        print(str(i)+':',end=' ')
        showfreq(t[0])
    else:
        print('#',end=' ')
        showfreq(t[0])
    buttomup_next(t)




