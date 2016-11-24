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
    return sorted(G)

def edges(G):
    return [(u,v) for u in vertices(G) for v in G[u]]

v = [Vertex(i) for i in range(8)]

G = {v[0]:[v[1],v[4]],
     v[1]:[v[0],v[5]],
     v[2]:[v[3],v[5],v[6]],
     v[3]:[v[2],v[6],v[7]],
     v[4]:[v[0]],
     v[5]:[v[1],v[2],v[6]],
     v[6]:[v[2],v[3],v[5],v[7]],
     v[7]:[v[3],v[6]]}

print("vertices(G):",vertices(G))
print("edges(G):",edges(G))

def clear(G): 
    for v in vertices(G):
        k = [e for e in vars(v) if e != 'data']
        for e in k:
            delattr(v,e)

def DFS(G,s):
    global time    
    time += 1
    s.discover = time
    for v in G[s]:
        if not (hasattr(v,'discover')):
            v.predecessor = s 
            DFS(G,v)
    time += 1
    s.finish = time

time = 0 
v[1].predecessor = None    
DFS(G,v[1])    

def show_tree_info(G):
    print('tree:', end = ' ')
    for v in vertices(G):
        print('(' + str(v), end = '') 
        if hasattr(v,'discover'): 
            print(',d:' + str(v.discover), end = '') 
        if hasattr(v,'finish'): 
            print(',f:' + str(v.finish), end = '') 
        if hasattr(v,'predecessor'): 
            print(',p:' + str(v.predecessor),  end = '')
        print(')', end = ' ')
    print()

show_tree_info(G)

def path_DFS(G,u,v):
    DFS(G,u)
    a = []
    if hasattr(v,'predecessor'):
        current = v
        while current:
            a.append(current)
            current = current.predecessor
    a.reverse()
    return a
    
print("path_DFS(G,1,7):",path_DFS(G,v[1],v[7]))    
    
def tree_edges(G):
    a = []
    for v in vertices(G):
        if hasattr(v,'predecessor') and v.predecessor != None: 
            a.append((v,v.predecessor))
            a.append((v.predecessor,v))                   
    a.sort()
    return a

print('tree_edges(G):',tree_edges(G))


