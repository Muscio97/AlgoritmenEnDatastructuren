def perm(a):
    assert a
    if len(a) == 1:
        return [a]
    else:
        ap = []
        for i in range(len(a)):           # bepaal alle permutaties die beginnen met a[i]
            ap2 = perm(a[:i]+a[i+1:])     # bepaal permutaties van lijst zonder a[i]
            ap += [[a[i]]+p for p in ap2] # plaats voor iedere permutatie a[i]
        return ap

print(perm([1,2,3]))

import itertools

p = itertools.permutations([7, 3, 9])
print(list(p))