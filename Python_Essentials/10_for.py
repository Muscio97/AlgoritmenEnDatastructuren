for i in range(11,21): # i heeft de waarden 11,12,...,20
    print(i*i)
print()

for i in range(11,21):
    print(i*i,end=' ')
print()

b = [] # b is een lege lijst
for i in range(11,21):
    b.append(i*i)
print('b =' ,b)
print()

b = [i*i for i in range(11,21)]
print('b =' ,b)
print()

a = []
for i in range(11,21):
    k = i*i
    if k%3 != 0:
        a.append(k)
print('a =' ,a)
print()

a = [i*i for i in range(11,21) if i%3 != 0]
print('a =' ,a)
print()

for ch in 'string':
    print(ch, end = ' ')
print()

a = [41,73,52]
b = [2**n for n in a]
print('b =' ,b)
print()

a = ['hoeveel','genezen','bereveel']
u = [list(i).count('e') for i in a]
print('u =' ,u)
print()