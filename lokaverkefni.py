#Lokaverkefni
#Ingólfur Óskarsson
#Guðlaugur Haukur Árnason
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
print(rotta2.tegund,rotta2.afl,rotta2.stadur)
print(rotta3.tegund,rotta3.afl,rotta3.stadur)
print(hamstur.tegund,hamstur.afl,hamstur.stadur)

svar=0
while svar!="2":
    print("-----Nagdýr-----")
    print("1 - Spila")
    print("2 - Hætta")
    print("----------------")
    svar=input("Sláðu inn tölu frá bilinu 1-2 ")

    if svar=="1":
        svar1=0
        while svar1!="3":
            print("\n-----Valmynd-----")
            print("1 - Kasta teningi?")
            print("2 - Staðsetning?")
            print("3 - Hætta")
            print("-------------------")
            svar1=input("Sláðu inn tölu frá bilinu 1-3 ")



            if svar1=="1":
                print("\nkastað er teningi ")
                teningur = random.randint(1, 6)
                print("þú fékkst =", teningur)
                player1.stadur=player1.stadur + teningur
                teningur = random.randint(1, 6)
                print("Núna kasta rotturnar")
                att=random.randint(1,2)
                if att == 1:
                    print("Rotta 1 fær", teningur,"og fer áfram")
                    rotta1.stadur = rotta1.stadur + teningur
                    print("Rotta 1 er kominn á reit", rotta1.stadur)
                elif att == 2:
                    print("Rotta 1 fær", teningur,"og fer til baka")
                    rotta1.stadur = rotta1.stadur - teningur
                    print("Rotta 1 er kominn á reit", rotta1.stadur)
                teningur = random.randint(1, 6)
                att = random.randint(1 , 2)
                if att == 1:
                    print("Rotta 2 fær", teningur, "og fer áfram")
                    rotta2.stadur = rotta2.stadur + teningur
                    print("Rotta 2 er kominn á reit", rotta2.stadur)
                elif att == 2:
                    print("Rotta 2 fær", teningur, "og fer til baka")
                    rotta2.stadur = rotta2.stadur - teningur
                    print("Rotta 2 er kominn á reit", rotta2.stadur)
                teningur = random.randint(1, 6)
                att = random.randint(1 , 2)
                if att == 1:
                    print("Rotta 3 fær", teningur, "og fer áfram")
                    rotta3.stadur = rotta3.stadur + teningur
                    print("Rotta 3 er kominn á reit", rotta3.stadur)
                elif att == 2:
                    print("Rotta 3 fær", teningur, "og fer til baka")
                    rotta3.stadur = rotta3.stadur - teningur
                    print("Rotta 3 er kominn á reit", rotta3.stadur)
                teningur = random.randint(1, 6)
                print("Núna kastar hamsturinn")
                print("Hamsturinn fær",teningur)
                hamstur.stadur=hamstur.stadur+teningur
                print("Hamsturinn er kominn á reit",hamstur.stadur)

            elif    svar1=="2":
                print("Músin er stödd á reit =",player1.stadur)





