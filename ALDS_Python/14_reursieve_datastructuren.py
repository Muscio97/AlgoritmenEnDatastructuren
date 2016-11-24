a = [1]
a.append(a)
print(a)

a = [1]
b = [2,a]
print(a)
print(b)
a.append(b)
print(a)
print(b)