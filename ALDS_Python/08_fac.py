def fac1(n):
    fac = 1
    for i in range(2,n+1):
        fac *= i
    return fac

def fac2(n):
    if n<0:         # error
        return -1
    elif n == 0:    # basisgeval
        return 1
    else:
        return n*fac2(n-1)

if __name__ == '__main__':
    print(fac1(15))
    print(fac2(15))
    print(fac2(-15))
    for i in range(1,26):
        print(fac2(i))
