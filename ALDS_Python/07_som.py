def som1(n):
    som = 0
    for i in range(1,n+1):
        som = som + i
    return som

def som2(n):
    return (n*(n+1))//2

def som3(n):
    if n <= 0:
        raise Exception('argumenten kleiner dan 1 zijn niet toegestaan')
    elif n == 1:
        return 1
    else:
        return som3(n-1) +n

if __name__ == '__main__':
    print(som1(100))
    print(som2(100))
    print(som3(100))
#    print(som3(0))
