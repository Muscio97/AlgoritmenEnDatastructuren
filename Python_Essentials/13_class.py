class Clock():
    
    nclock = 0 # klasse-attribuut

    @staticmethod
    def show_nclock(): # klasse-methode
        print(Clock.nclock)

    def __init__(self, hour=0, minute=0, second=0): # constructor
        self.hour = hour # attribuut
        self.minute = minute # attribuut
        self.second = second # attribuut
        Clock.nclock += 1

    def __del__(self): # destructor
        Clock.nclock -= 1
        print("del aanroep")

    def __repr__(self): # voor print-opdracht
        return "tijd: " + str(self.hour) + ":" + str(self.minute) + ":" + str(self.second)

c1 = Clock(10,25,30)
print(c1)
Clock.show_nclock()
c2 = Clock(10,25,31)
print(c2)
Clock.show_nclock()
del c1
Clock.show_nclock()

def f():
    Clock()
    Clock.show_nclock()
    # destructor wordt aangeroepen
    
print("f entrance")
f()
print("f exit")
Clock.show_nclock()
c2.show_nclock() # werkt alleen als @staticmethod is toegevoegd
del c2
print()

class ClockEx(Clock): # ClockEx is een uitbreiding van Clock

    def tick(self):
        self.second = (self.second+1)%60
        if self.second == 0:
            self.minute = (self.minute+1)%6
        if self.minute == 0:
            self.hour= (self.hour+1)%24

c1 = ClockEx(10,25,30)
print(c1)
Clock.show_nclock()
c1.tick()
print(c1)
print()

c2 = ClockEx(23,59,59)
print(c2)
Clock.show_nclock()
c2.tick()
print(c2)
print()

del c1
c3 = c2
del c2        # del wordt niet aangeroepen,
              # want c3 verwijst ook naar het object
import time
time.sleep(5) # na 5 sec. verschijnt op het scherm: del aanroep
print()