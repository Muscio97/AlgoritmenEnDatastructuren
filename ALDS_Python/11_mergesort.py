def insertionSort(a, low, high):
    for p in range(low + 1,high+1):
        tmp = a[p]
        j = p
        while j > low and tmp < a[j-1]:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp

def rmergeSort(a,low,high):
    if high <= low+5:
        insertionSort(a, low, high )

    else:
#        tmpar = [0]*len(a)
        mid = (high+low)//2

        rmergeSort(a,low,mid)
        rmergeSort(a,mid+1,high)

        # kopieer linker helft in tmp
        tmpar = a[low:mid+1]

        # meng tmp en rechterhelft

        i = low
        j = mid+1
        k = low

        while i<=mid and j<=high:
            if tmpar[i-low] < a[j]:
                a[k] = tmpar[i-low]
                i += 1
            else:
                a[k] = a[j]
                j +=1
            k += 1
        while i <= mid:
            a[k] = tmpar[i-low]
            i += 1
            k += 1

def mergeSort(a):
    rmergeSort(a,0,len(a)-1)

def isSorted(a):
    i = 0;
    while i < len(a)-1 and a[i] <= a[i+1]:
        i += 1

    return i == len(a)-1

if __name__ == '__main__':
    ia = [45,65,34,82,30,22]
    print(ia)
    mergeSort(ia)
    print(ia)

    dd = [45.0,65.0,34.0,82.0,30.0,22.0]
    print(dd)
    mergeSort(dd)
    print(dd)

    import random

    a = [0]*100000
    for i in range(100000):
        a[i] = random.randint(0,1000000)
    print("a gegenereerd")
    print(a[50000])
    b = list(a)

    import timeit
    timer = timeit.default_timer

    t1 = timer()
    mergeSort(a)
    t2 = timer()
    print(t2-t1)
    print(isSorted(a))

    b.sort()
    print(a == b)

