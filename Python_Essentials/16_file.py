f = open('vb1.txt','w') # open de file 'vb1.txt'
# om in te schrijven.
f.write('1 een\n')
f.write('2 twee\n')
f.write('3 drie')
f.close()

f = open('vb1.txt','r') # open een file om uit te lezen
for line in f:
    if line[-1] == '\n':
        line = line[:-1] # verwijder '\n' aan het einde van een regel
    print(line)
f.close()

print()

f= open('vb2.txt','w')
f.writelines(['1 een\n','2 twee\n','3 drie'])
f.close()

f = open('vb2.txt','r')
a = f.readlines()
f.close()

for s in a:
    if s[-1] == '\n':
        s = s[:-1]
    print(s)
    
print()

f = open('vb1.txt','r')
s = f.read()
f.close()

print('repr(s):',repr(s))
a = s.split('\n')
print(a)
for s in a:
    print(s)
print()

f = open('vb1.txt','r')
s = f.read(1)
while s:
    print(s, end = '')
    s = f.read(1)
f.close()
print()

print()

f = open('vb1.txt','r')
s = f.read(1)
while s:
    print(repr(s), end = ',')
    s = f.read(1)
f.close()
print()

f = open('vb3.txt','w')
s1 = 'aaa\nbbb\nccc'
print('s1:',repr(s1))
print('len(s1):',len(s1))
f.write(s1)
f.close()

print()

g1 = open('vb3.txt','r')
s2= g1.read()
print('s2:', repr(s2))
print('len(s2):',len(s2))
g1.close()

print()

g2 = open('vb3.txt','rb')
s3= g2.read()
print('s3:', repr(s3))
print('len(s3):',len(s3))
g2.close()