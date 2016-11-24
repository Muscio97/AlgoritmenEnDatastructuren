cijferlijst = {'Piet':7.4, 'Jan':3.4, 'Kees':5.5}
print(cijferlijst)
print()

cijferlijst['Karel'] = 8.7 # toevoegen
print(cijferlijst)
print()

cijferlijst['Jan'] = 6.1   # wijzigen
print(cijferlijst)
print()

del cijferlijst['Karel']   # verwijderen
print(cijferlijst)

cijferlijst2 = {'Peter':9.5, 'Henk': 2.3, 'Rob':7.9}
cijferlijst.update(cijferlijst2)
print(cijferlijst)
print()

for i in cijferlijst: # alleen de keys worden getoond
    print(i, end = ' ')
print()
    
for i in sorted(cijferlijst): # alleen de keys worden getoond
    print(i, end = ' ')
print()

for k,v in sorted(cijferlijst.items()):
    print(k,v)
print()

print(sorted(cijferlijst.values()))
print()

class Artikel:
    
    def __init__(self, nr, naam, prijs):
        self.nr = nr
        self.naam = naam
        self.prijs = prijs
        
    def __repr__(self):
        return "<< nr: " + str(self.nr) + " naam: " + self.naam + " prijs: " + str(self.prijs) + " >>"
    
a1 = [None]*4
a1[0] = Artikel(35,'stoel',110)
a1[1] = Artikel(18,'bank',330)
a1[2] = Artikel(36,'kast',450)
a1[3] = Artikel(5,'tafel',180)
print(a1)
a1.sort(key = lambda art: art.nr) #sorteer op nr
print(a1)
print()

d = {'nr':35,'naam':'stoel','prijs':110}

a2 = [None]*4

a2[0] = {'nr':35,'naam':'stoel','prijs':110}
a2[1] = {'nr':18,'naam':'bank','prijs':330}
a2[2] = {'nr':36,'naam':'kast','prijs':450}
a2[3] = {'nr':5,'naam':'tafel','prijs':180}
print(a2)

a2.sort(key = lambda art: art['nr']) # sorteer op nr
print(a2)
a2 = [sorted(art.items()) for art in a2] # sorteer ieder element
print(a2)
print()