x = 56
y = 78
print('x:', x)
print('y:', y)
print('x+y:', x+y)
print()

x = 56
print('x:', x)
print('type(x):', type(x))
print('id(x):', id(x))
y = 56
print('y:', y)
print('id(y):', id(y))
x += 1
print('x:', x)
print('id(x):', id(x))
x = 'string'
print('x:', x)
print('type(x):', type(x))
print('id(x):', id(x))
print()

x = y = 7
print([i for i in dir() if not (i.startswith('__') and i.endswith('__'))])
del x
print([i for i in dir() if not (i.startswith('__') and i.endswith('__'))])
print()



