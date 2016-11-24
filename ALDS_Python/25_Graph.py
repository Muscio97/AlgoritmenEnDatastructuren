class Vertex:
    def __init__(self, data):
        self.data = data
    
    def __repr__(self):         # voor afdrukken
        return str(self.data)
    
    def __lt__(self, other):    # voor sorteren
        return self.data < other.data

v = [Vertex(i) for i in range(5)]    

G = {v[0]:[v[1],v[4]], 
     v[1]:[v[0],v[2],v[3],v[4]], 
     v[2]:[v[1],v[3]], 
     v[3]:[v[1],v[2],v[4]],
     v[4]:[v[0],v[1],v[3]]}

def vertices(G):
    return sorted(G)

print("vertices(G):",vertices(G))

def edges(G):
    return [(u,v) for u in vertices(G) for v in G[u]]

print("edges(G):",edges(G))
print("edges(G):",edges(G))
