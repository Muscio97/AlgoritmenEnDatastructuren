class myqueue(list):
    def __init__(self,a=[]):
        list.__init__(self,a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self,x):
        self.append(x)

q = myqueue('345')
print('q:', q)

q.enqueue(100)
print('q:', q)

print('q.dequeue():', q.dequeue())
print('q:', q)
