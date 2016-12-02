'''
Created on 28 nov. 2016

@author: MuscioCraft
'''
def machtv3(a,n):
    assert n > 0
    m = 1
    counter = 0
    while n > 0:
        counter = counter + 1
        if n%2 == 0:
            m = m * (a**2)
            n = n // 2
        else:
            m = m * a**(n-1)
            n = n - 1
    return int(m), count
    

print(machtv3(10, 2))
print(machtv3(10, 10)
print(machtv3(10, 100))
print(machtv3(10, 1000))
print(machtv3(10, 10000))