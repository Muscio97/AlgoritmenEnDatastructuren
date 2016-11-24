class Artikel:
    def __init__(self, nr, naam, prijs):
        self.nr = nr
        self.naam = naam
        self.prijs = prijs

    def __repr__(self):
        return "<< nr: " + str(self.nr) + " naam: " + self.naam + " prijs: " + str(self.prijs) + ">>"
        
a =[ Artikel(35,'stoel',110), Artikel(18,'bank', 330), Artikel(36,'kast', 450), Artikel(5, 'tafel',180)]

d = {a[i].nr:a[i] for i in range(4)}

print(d)
