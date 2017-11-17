#Lokaverkefni
#Ingólfur Óskarsson
import random




class Nagdyr:
    #stadur=0
    #afl=random.randint(0,6)

    def __init__(self,tegund,stadur,afl):
        self.tegund=tegund
        self.afl=afl
        self.stadur=stadur

    #def stadur(self):
     #   if stadur <= 100:
      #      print("Þú vinnur")
       # else:
        #    print("Þú er á reit",stadur)

    #def afl(self):
     #   self.afl=random.randint(0,6,2)

    #def rottu(self):
        #self.stadur=random.randint(1,100)
        #self.afl=random.randint(0,6,2)


   # def hamstur(self):
    #    self.stadur=random.randint(1,100)
     #   self.afl = random.randint(0,6,2)

    #def mus(self):
        #self.stadur=0
        #self.afl = random.randint(0, 6, 2)


#stadur=0
#afl=0

player1 = Nagdyr("Mús",0, random.randrange(2,7,2))
rotta1 = Nagdyr("Rotta",random.randrange(1,100), random.randrange(2,7,2))
rotta2 = Nagdyr("Rotta",random.randrange(1,100), random.randrange(2,7,2))
rotta3 = Nagdyr("Rotta",random.randrange(1,100), random.randrange(2,7,2))
hamstur = Nagdyr("Hamstur",random.randrange(1,100), random.randrange(2,7,2))
print(player1.tegund,player1.afl,player1.stadur)
print(rotta1.tegund,rotta1.afl,rotta1.stadur)
print(rotta2.tegund,rotta2.afl,rotta3.stadur)
print(rotta3.tegund,rotta3.afl,rotta3.stadur)
print(hamstur.tegund,hamstur.afl,hamstur.stadur)

#kasta= random.randint()



