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

#player1 = Nagdyr("Mús",0, random.randrange(2,7,2))
#rotta1 = Nagdyr("Rotta",random.randrange(1,100), random.randrange(2,7,2))
#rotta2 = Nagdyr("Rotta",random.randrange(1,100), random.randrange(2,7,2))
#rotta3 = Nagdyr("Rotta",random.randrange(1,100), random.randrange(2,7,2))
#hamstur = Nagdyr("Hamstur",random.randrange(1,100), random.randrange(2,7,2))

#print(player1.tegund,player1.afl,player1.stadur)
#print(rotta1.tegund,rotta1.afl,rotta1.stadur)
#print(rotta2.tegund,rotta2.afl,rotta2.stadur)
#print(rotta3.tegund,rotta3.afl,rotta3.stadur)
#print(hamstur.tegund,hamstur.afl,hamstur.stadur)

svar=0
while svar!="2":
    player1 = Nagdyr("Mús", 0, random.randrange(2, 7, 2))
    rotta1 = Nagdyr("Rotta", random.randrange(1, 100), random.randrange(2, 7, 2))
    rotta2 = Nagdyr("Rotta", random.randrange(1, 100), random.randrange(2, 7, 2))
    rotta3 = Nagdyr("Rotta", random.randrange(1, 100), random.randrange(2, 7, 2))
    hamstur = Nagdyr("Hamstur", random.randrange(1, 50), random.randrange(2, 7, 2))
    print(player1.tegund, player1.afl, player1.stadur)
    print(rotta1.tegund, rotta1.afl, rotta1.stadur)
    print(rotta2.tegund, rotta2.afl, rotta2.stadur)
    print(rotta3.tegund, rotta3.afl, rotta3.stadur)
    print(hamstur.tegund, hamstur.afl, hamstur.stadur)
    print("-----Nagdýr-----")
    print("1 - Spila")
    print("2 - Hætta")
    print("-----------------")
    svar=input("Sláðu inn tölu frá bilinu 1-2 ")


    if svar=="1":
        svar1=0
        while svar1!="3":
            print("\n-----Valmynd-----")
            print("1 - Kasta teningi?")
            print("2 - Staðsetning?")
            print("3 - Hætta")
            svar1=input("Sláðu inn tölu frá bilinu 1-3 ")



            if svar1=="1":
                print("\nkastað er teningi ")
                teningur = random.randint(1, 6)
                print("þú fékkst =", teningur)
                #player1.stadur=player1.stadur + teningur
                #print("Þú ert á reit",player1.stadur)

                #Tjekkar hvort músinn fer framhjá rottonum og hamstur
                for x in range(player1.stadur, teningur+player1.stadur):
                    #print("Músinn",player1.stadur)
                    #print("rotta1",rotta1.stadur,"rotta2",rotta2.stadur,"rotta3",rotta3.stadur)
                    x=x+1
                    print(x)
                    if rotta1.stadur == x: #or rotta2.stadur == x or rotta3.stadur == x:
                        print("Þú ert á sama reit og rotta1")
                        if rotta1.afl > player1.afl:
                            print("\nRotta vinnur\n")
                            player1.stadur = player1.stadur - teningur - rotta1.afl
                            print("Þú ferð til baka um",rotta1.afl,"marga reiti")
                        elif rotta1.afl < player1.afl:
                            print("\nPlayer 1 vinnur\n")
                        else:
                            print("Jafntefli")

                        #athuga hvort músin eða rottan hefur meira afl
                    elif rotta2.stadur == x:
                        print("Þú ert á sama reit og rotta2")
                        if rotta2.afl > player1.afl:
                            print("\nRotta vinnur")
                            player1.stadur = player1.stadur - teningur - rotta2.afl
                            print("Þú ferð til baka um", rotta2.afl, "marga reiti")
                        elif rotta2.afl < player1.afl:
                            print("\nPlayer 1 vinnur")
                        else:
                            print("Jafntefli")

                    elif rotta3.stadur == x:
                        print("Þú ert á sama reit og rotta3")
                        if rotta3.afl > player1.afl:
                            print("\nRotta vinnur")
                            player1.stadur=player1.stadur-teningur-rotta3.afl
                            print("Þú ferð til baka um", rotta3.afl, "marga reiti")
                        elif rotta3.afl < player1.afl:
                            print("\nPlayer 1 vinnur")
                        else:
                            print("Jafntefli")

                    elif hamstur.stadur == x:
                        print("\nHAMSTURINN KASTAR ÞÉR ÁFRAM!\n")
                        player1.stadur = player1.stadur + hamstur.afl
                        print("\n Þú lentir á reit",player1.stadur)

                player1.stadur = player1.stadur + teningur
                print("Þú ert á reit", player1.stadur)

                teningur = random.randint(1, 6)
                print("Núna kasta rotturnar")
                att1=random.randint(1,2)
                if att1 == 1:
                    print("Rotta 1 fær", teningur,"og fer áfram")
                    for x in range(rotta1.stadur,rotta1.stadur+teningur):
                        x=x+1
                        if player1.stadur == x:
                            print("Rotta 1 hittir mús")
                            if rotta1.afl > player1.afl:
                                print("\nRotta vinnur")
                                player1.stadur = player1.stadur - rotta1.afl
                                print("Þú ferð til baka um", rotta1.afl, "marga reiti")
                            elif rotta1.afl < player1.afl:
                                print("\nPlayer 1 vinnur")
                                player1.stadur=player1.stadur + 2
                            else:
                                print("Jafntefli")

                    rotta1.stadur = rotta1.stadur + teningur
                    print("Rotta 1 er kominn á reit", rotta1.stadur)
                elif att1 == 2:
                    print("Rotta 1 fær", teningur,"og fer til baka")
                    for x in range(rotta1.stadur,rotta1.stadur - teningur,-1):
                        x=x-1
                        if player1.stadur == x:
                            print("Rotta 1 hittir mús")
                            if rotta1.afl > player1.afl:
                                print("\nRotta vinnur")
                                player1.stadur = player1.stadur - rotta1.afl
                                print("Þú ferð til baka um", rotta1.afl, "marga reiti")
                            elif rotta1.afl < player1.afl:
                                print("\nPlayer 1 vinnur")
                                player1.stadur=player1.stadur + 2
                            else:
                                print("Jafntefli")
                    rotta1.stadur = rotta1.stadur - teningur
                    print("Rotta 1 er kominn á reit", rotta1.stadur)

                teningur = random.randint(1, 6)
                att2 = random.randint(1 , 2)
                if att2 == 1:
                    print("Rotta 2 fær", teningur, "og fer áfram")
                    for x in range(rotta2.stadur,rotta2.stadur + teningur):
                        x=x+1
                        if player1.stadur == x:
                            print("Rotta 2 hittir mús")
                            if rotta2.afl > player1.afl:
                                print("\nRotta vinnur")
                                player1.stadur = player1.stadur - rotta2.afl
                                print("Þú ferð til baka um", rotta2.afl, "marga reiti")
                            elif rotta1.afl < player1.afl:
                                print("\nPlayer 1 vinnur")
                                player1.stadur=player1.stadur + 2
                            else:
                                print("Jafntefli")
                    rotta2.stadur = rotta2.stadur + teningur
                    print("Rotta 2 er kominn á reit", rotta2.stadur)
                elif att2 == 2:
                    print("Rotta 2 fær", teningur, "og fer til baka")
                    for x in range(rotta2.stadur,rotta2.stadur - teningur,-2):
                        x=x-1
                        if player1.stadur == x:
                            print("Rotta 2 hittir mús")
                            if rotta2.afl > player1.afl:
                                print("\nRotta vinnur")
                                player1.stadur = player1.stadur - rotta2.afl
                                print("Þú ferð til baka um", rotta2.afl, "marga reiti")
                            elif rotta2.afl < player1.afl:
                                print("\nPlayer 1 vinnur")
                                player1.stadur=player1.stadur + 2
                            else:
                                print("Jafntefli")
                    rotta2.stadur = rotta2.stadur - teningur
                    print("Rotta 2 er kominn á reit", rotta2.stadur)

                teningur = random.randint(1, 6)
                att3 = random.randint(1 , 2)
                if att3 == 1:
                    print("Rotta 3 fær", teningur, "og fer áfram")
                    for x in range(rotta3.stadur,rotta3.stadur + teningur):
                        x=x+1
                        if player1.stadur == x:
                            print("Rotta 3 hittir mús")
                            if rotta3.afl > player1.afl:
                                print("\nRotta vinnur")
                                player1.stadur = player1.stadur - rotta3.afl
                                print("Þú ferð til baka um", rotta3.afl, "marga reiti")
                            elif rotta3.afl < player1.afl:
                                print("\nPlayer 1 vinnur")
                                player1.stadur=player1.stadur + 2
                            else:
                                print("Jafntefli")
                    rotta3.stadur = rotta3.stadur + teningur
                    print("Rotta 3 er kominn á reit", rotta3.stadur)
                elif att3 == 2:
                    print("Rotta 3 fær", teningur, "og fer til baka")
                    for x in range(rotta3.stadur,rotta3.stadur - teningur,-1):
                        x=x-1
                        if player1.stadur == x:
                            print("Rotta 1 hittir mús")
                            if rotta3.afl > player1.afl:
                                print("\nRotta vinnur")
                                player1.stadur = player1.stadur - rotta3.afl
                                print("Þú ferð til baka um", rotta3.afl, "marga reiti")
                            elif rotta3.afl < player1.afl:
                                print("\nPlayer 1 vinnur")
                                player1.stadur=player1.stadur + 2
                            else:
                                print("Jafntefli")
                    rotta3.stadur = rotta3.stadur - teningur
                    print("Rotta 3 er kominn á reit", rotta3.stadur)

                teningur = random.randint(1, 6)
                print("Núna kastar hamsturinn")
                print("Hamsturinn fær",teningur)
                if player1.stadur > hamstur.stadur:
                #Hvort að hamstur fer framhjá mús
                    for x in range(hamstur.stadur,hamstur.stadur+teningur):
                        x=x+1
                        if player1.stadur == x:
                            print("HAMSTURINN KASTAR ÞÉR ÁFRAM!")
                            player1.stadur=player1.stadur + hamstur.afl
                    hamstur.stadur=hamstur.stadur+teningur
                #Tjekkar hvort hamstur og rotta er á sama stað
                    if hamstur.stadur == rotta1.stadur:
                        print("Hamstur lenti á sama reit og rotta 1")
                        if att1 == 1:
                            rotta1.stadur=rotta1.stadur - 1
                            print("Rottan fer einn afturábak")
                            print("Rotta 1 er á reit",rotta1.stadur)
                            print("Hamsturinn fer einn afturábak")
                            hamstur.stadur = hamstur.stadur - 1
                        elif att1 == 2:
                            rotta1.stadur=rotta1.stadur + 1
                            print("Rottan fer einn áfram")
                            print("Rotta 1 er á reit",rotta1.stadur)
                            print("Hamsturinn fer einn afturábak")
                            hamstur.stadur = hamstur.stadur - 1

                    elif hamstur.stadur == rotta2.stadur:
                        print("Hamstur lenti á sama reit og rotta 1")
                        if att2 == 1:
                            rotta2.stadur=rotta2.stadur - 1
                            print("Rottan fer einn afturábak")
                            print("Rotta 2 er á reit",rotta2.stadur)
                            print("Hamsturinn fer einn afturábak")
                            hamstur.stadur = hamstur.stadur - 1
                        elif att2 == 2:
                            rotta1.stadur=rotta2.stadur + 1
                            print("Rottan fer einn áfram")
                            print("Rotta 2 er á reit",rotta2.stadur)
                            print("Hamsturinn fer einn afturábak")
                            hamstur.stadur = hamstur.stadur - 1

                    elif hamstur.stadur == rotta3.stadur:
                        print("Hamstur lenti á sama reit og rotta 1")
                        if att3 == 1:
                            rotta3.stadur=rotta3.stadur - 1
                            print("Rottan fer einn afturábak")
                            print("Rotta 3 er á reit",rotta3.stadur)
                            print("Hamsturinn fer einn afturábak")
                            hamstur.stadur = hamstur.stadur - 1
                        elif att3 == 2:
                            rotta3.stadur=rotta3.stadur + 1
                            print("Rottan fer einn áfram")
                            print("Rotta 3 er á reit",rotta3.stadur)
                            print("Hamsturinn fer einn afturábak")
                            hamstur.stadur=hamstur.stadur - 1

                elif player1.stadur < hamstur.stadur:
                #Hvort að hamstur fer framhjá mús
                    for x in range(hamstur.stadur,hamstur.stadur-teningur,-1):
                        #x=x
                        print(x)
                        if player1.stadur == x:
                            print("HAMSTURINN KASTAR ÞÉR ÁFRAM!")
                            player1.stadur=player1.stadur + hamstur.afl
                    hamstur.stadur=hamstur.stadur-teningur
                #Tjekkar hvort hamstur og rotta er á sama stað
                    if hamstur.stadur == rotta1.stadur:
                        print("Hamstur lenti á sama reit og rotta 1")
                        if att1 == 1:
                            rotta1.stadur=rotta1.stadur - 1
                            print("Rottan fer einn afturábak")
                            print("Rotta 1 er á reit",rotta1.stadur)
                            print("Hamsturinn fer einn áfram")
                            hamstur.stadur = hamstur.stadur + 1
                        elif att1 == 2:
                            rotta1.stadur=rotta1.stadur + 1
                            print("Rottan fer einn áfram")
                            print("Rotta 1 er á reit",rotta1.stadur)
                            print("Hamsturinn fer einn áfram")
                            hamstur.stadur = hamstur.stadur + 1

                    elif hamstur.stadur == rotta2.stadur:
                        print("Hamstur lenti á sama reit og rotta 1")
                        if att2 == 1:
                            rotta2.stadur=rotta2.stadur - 1
                            print("Rottan fer einn afturábak")
                            print("Rotta 2 er á reit",rotta2.stadur)
                            print("Hamsturinn fer einn áfram")
                            hamstur.stadur = hamstur.stadur + 1
                        elif att2 == 2:
                            rotta1.stadur=rotta2.stadur + 1
                            print("Rottan fer einn áfram")
                            print("Rotta 2 er á reit",rotta2.stadur)
                            print("Hamsturinn fer einn áfram")
                            hamstur.stadur = hamstur.stadur + 1

                    elif hamstur.stadur == rotta3.stadur:
                        print("Hamstur lenti á sama reit og rotta 1")
                        if att3 == 1:
                            rotta3.stadur=rotta3.stadur - 1
                            print("Rottan fer einn afturábak")
                            print("Rotta 3 er á reit",rotta3.stadur)
                            print("Hamsturinn fer einn áfram")
                            hamstur.stadur = hamstur.stadur + 1
                        elif att3 == 2:
                            rotta3.stadur=rotta3.stadur + 1
                            print("Rottan fer einn áfram")
                            print("Rotta 3 er á reit",rotta3.stadur)
                            print("Hamsturinn fer einn áfram")
                            hamstur.stadur=hamstur.stadur + 1

                print("Hamsturinn er kominn á reit",hamstur.stadur)

            elif    svar1=="2":

                print("Þú ert á reit",player1.stadur)
                print("Rotta1",rotta1.stadur)
                print("Rotta2", rotta2.stadur)
                print("Rotta3", rotta3.stadur)
                print("Hamstur", hamstur.stadur)






