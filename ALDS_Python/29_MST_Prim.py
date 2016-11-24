class myqueue(list):
    def __init__(self,a=[]):
        list.__init__(self,a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self,x):
        self.append(x)
        
class Vertex:
    def __init__(self, data):
        self.data = data
    
    def __repr__(self):         # voor afdrukken
        return str(self.data)
    
    def __lt__(self, other):    # voor sorteren
        return self.data < other.data

import math
    
INFINITY = math.inf

def vertices(G):
    return sorted(G.keys())

def edges(G):
    a = []
    for u in vertices(G):
        for v in G[u].keys():
            a.append((u,v,G[u][v]))
    a.sort()
    return a

v = [Vertex(i) for i in range(7)]
v = [Vertex(i) for i in list('abcdefg')]

G = {v[0]:{v[1]:72,v[4]:31,v[6]:84},
     v[1]:{v[0]:72,v[2]:19,v[4]:25},
     v[2]:{v[1]:19,v[3]:72,v[4]:22},
     v[3]:{v[2]:72,v[5]:38},
     v[4]:{v[0]:31,v[1]:25,v[2]:22,v[5]:45,v[6]:16},
     v[5]:{v[3]:38,v[4]:45},
     v[6]:{v[0]:84,v[4]:16}}

print("vertices(G):",vertices(G))
print("edges(G):",edges(G))

def clear(G): 
    for v in vertices(G):
        k = [e for e in vars(v) if e != 'data']
        for e in k:
            delattr(v,e)

def MST_Prim(G,s):
    Q = vertices(G)
    for v in Q:
        v.key = INFINITY
        v.predecessor = None
    s.key = 0
    while Q:
#        print([(q,q.key) for q in Q])
        u = min(Q,key=lambda x: x.key)
        Q.remove(u)
        for v in G[u].keys():
            if v in Q and G[u][v] < v.key:
                v.predecessor = u
                v.key = G[u][v]

MST_Prim(G,v[0])

def tree_edges(G):
    a = []
    for v in vertices(G):
        if hasattr(v,'predecessor') and v.predecessor != None: 
            a.append((v,v.predecessor,G[v][v.predecessor]))
            a.append((v.predecessor,v,G[v.predecessor][v]))                   
    a.sort()
    return a

print('tree_edges(G):',tree_edges(G))
       
print([(v,v.key) for v in vertices(G)])        
print(sum([v.key for v in vertices(G)]))       

 


