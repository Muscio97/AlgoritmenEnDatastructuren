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
    
INFINITY = float("inf")

def vertices(G):
    return sorted(G.keys())

def edges(G):
    a = []
    for u in vertices(G):
        for v in G[u].keys():
            a.append((u,v,G[u][v]))
    return a

v = [Vertex(i) for i in range(5)]

G = {v[0]:{v[1]:10,v[4]:5},
     v[1]:{v[2]:1,v[4]:2},
     v[2]:{v[3]:4},
     v[3]:{v[0]:7,v[2]:6},
     v[4]:{v[1]:3,v[2]:9,v[3]:2}}

print("vertices(G):",vertices(G))
print("edges(G):",edges(G))

def clear(G): 
    for v in vertices(G):
        k = [e for e in vars(v) if e != 'data']
        for e in k:
            delattr(v,e)

def Dijkstra(G,s):
    Q = vertices(G)
    for v in Q:
        v.d = INFINITY
        v.predecessor = None
    s.d = 0

    while Q:
#        print([(q,q.d) for q in Q])
        u = min(Q,key=lambda x: x.d)  # u is het element uit Q met de kleinste distance 
        Q.remove(u)
        for v in G[u].keys():         # v is een buur van u      
            if v in Q and v.d > G[u][v]+ u.d:  # pas indien nodig de distance van v aan 
                v.predecessor = u
                v.d = G[u][v] + u.d

Dijkstra(G,v[0])

def tree_edges(G):
    a = []
    for v in vertices(G):
        if hasattr(v,'predecessor') and v.predecessor != None: 
            a.append((v.predecessor,v,G[v.predecessor][v]))                   
    a.sort()
    return a

print('tree_edges(G):',tree_edges(G))
       
print([(v,v.d) for v in vertices(G)])        
#print(sum([v.key for v in vertices(G)]))     

def shortest_path(G,u,v):
    clear(G)
    Dijkstra(G,u)
    a = []
    if hasattr(v,'predecessor'):
        current = v
        while current:
            a.append(current)
            current = current.predecessor
    a.reverse()
    return a

a = shortest_path(G,v[0],v[2])
print(a)

