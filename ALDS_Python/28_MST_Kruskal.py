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
        for v in G[u].keys():       # G[u].keys() : alle nodes v die verbonden zijn aan u 
            a.append((u,v,G[u][v]))
    a.sort()
    return a

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

def sorted_edges(G):
    return sorted(edges(G),key=lambda x: x[2]) # sorteer naar gewicht

print("sorted_edges(G):",sorted_edges(G))

def MST_Kruskal(G):
    A = []
    V = vertices(G)
    find_set = {}
    for v in V:
        find_set[v] = set([v])    # v is element van de verzameling find_set[v]  
    E = sorted_edges(G)           # gesorteerd op basis van gewicht
    for (u,v,w) in E:
#        print(find_set)
        if find_set[u] != find_set[v]:    # u en v behoren niet tot dezelfde set 
            A.append((u,v,w))     # heen
            A.append((v,u,w))     # terug 
            s = find_set[u] | find_set[v] # de vereniging van find_set[u]  en find_set[v]
            for e in s:
                find_set[e] = s       # pas partitie aan
    return A 

print("MST_Kruskal(G):",MST_Kruskal(G))       
print(sum([w for (u,v,w) in MST_Kruskal(G) if u<v]))
 


