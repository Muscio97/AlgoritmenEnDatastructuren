class HashEntry:
    def __init__(self,element,isActive):
        self.element = element
        self.isActive = isActive

class LinearHashTable:
    def __init__(self):
        self.len = 3
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
        current = hash(e)%self.len
        while self.table[current] != None and \
                        self.table[current].element != e:
            current = (current+1) % self.len
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
        if self.used > 0.8*self.len:
            self.rehash(4*self.size)
        return current

    def delete(self,e):
        current = self.search(e)
        if current != -1:
            self.table[current].isActive = False
        self.size -= 1
        return current

if __name__ == '__main__':
    lht = LinearHashTable()
    lht.insert(12.1)
    print(lht)
    lht.insert(23.1)
    print(lht)
    lht.insert(34.1)
    print(lht)
    lht.insert(45.1)
    print(lht)
    lht.delete(23.1)
    print(lht)
    lht.delete(34.1)
    print(lht)
    lht.rehash(5)
    print(lht)
