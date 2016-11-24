class HashEntry:
    def __init__(self,element,isActive):
        self.element = element
        self.isActive = isActive

def isPrime(n):
    if n<=0:
        return False
    elif n<=2:
        return True
    elif n>2 and n%2==0:
        return False
    else:
        i = 3;
        while i*i <= n and n%i != 0:
            i +=2
        return i*i > n

def nextPrime(n):
    if n <= 0:
        return 1
    i = n
    while not isPrime(i):
        i += 1
    return i;

class QuadraticHashTable:
    def __init__(self):
        self.len = 11
        self.size = 0
        self.used = 0
        self.table = [None]*self.len
        print("len: " + str(self.len))

    def __repr__(self):
        s = '-----------------\n'
        for i in range(self.len):
            if self.table[i] != None:
                s = s + '(' + str(i) + ',' + str(self.table[i].element) + \
                ',' + str(self.table[i].isActive) + ")\n";
        s = s + 'len: ' + str(self.len) + '\n'
        s = s + 'size: ' + str(self.size) + '\n'
        s = s + 'used: ' + str(self.used) + '\n'
        s = s + '-----------------\n'
        return s

    def getPos(self,e):
        i = 0
        print('hash:',e,hash(e),hash(e)%self.len)
        current = hash(e)%self.len
        while self.table[current] != None and self.table[current].element != e:
            current = (current+2*i+1) % self.len
            i += 1
        return current

    def search(self,e):
        current = self.getPos(e)
        if self.table[current] != None and self.table[current].isActive:
            return current
        else:
            return -1

    def rehash(self,newLen):
        if newLen >= self.size:
            oldLen = self.len
            oldTable = self.table

            self.size = 0
            self.used = 0
            self.len = newLen
            self.table = [None]*self.len

            for i in range(oldLen):
                if oldTable[i] != None and oldTable[i].isActive:
                    self.insert(oldTable[i].element)
            print('rehash: len: ' + str(self.len))

    def insert(self,e):
        current = self.getPos(e)
        if self.table[current] == None:
            self.table[current] = HashEntry(e,True)
            self.size += 1
            self.used += 1
        elif not self.table[current].isActive:
            self.table[current].isActive = True
            self.size += 1
        else:
            current = -1
        if 2*self.used > self.len:
            self.rehash(nextPrime(4*self.size))
        return current

    def delete(self,e):
        current = self.search(e)
        if current != -1:
            self.table[current].isActive = False
        self.size -= 1
        return current

if __name__ == '__main__':
    qht = QuadraticHashTable()
    qht.insert(12.1)
    print(qht)
    qht.insert(23.1)
    print(qht)
    qht.insert(34.1)
    print(qht)
    qht.insert(45.1)
    print(qht)
    qht.delete(23.1)
    print(qht)
    qht.delete(34.1)
    print(qht)
    qht.rehash(5)
    print(qht)
