def fib1(n):
    if n <= 1:  # basisgevallen
        return n
    else:
        return fib1(n-1) + fib1(n-2)

def fib2(n):
    if n <= 1:
        return n
    else:
        fvorig,f = 0,1
        for _ in range(2,n+1):
            fvorig,f = f, f+fvorig
    return f

if __name__ == '__main__':
    for i in range(101):
        print(i,fib2(i))
    print()
    for i in range(36):
        print(i,fib1(i))
