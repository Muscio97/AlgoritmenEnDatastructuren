def fib(n):
    if n <= 1:
        return n
    else:
        a = [0]*(n+1)
        a[0],a[1] = 0,1
        print(a)
        for i in range(2,n+1):
            a[i] = a[i-1] + a[i-2]
            print(a)
    return a[n]
print('fib(10):',fib(10))

def fac(n):
    if n <= 1:
        return 1
    else:
        return n*fac(n-1)

def B(n,k):
    return((fac(n)//fac(k))//fac(n-k))

print('B(20,10):',B(20,10))
