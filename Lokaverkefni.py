#Lokaverkefni
#Ingólfur Óskarsson
import random




class Nagdyr:


    def __init__(self,tegund,stadur,afl,þyngd,tennur):
        self.tegund=tegund
        self.afl=afl
        self.stadur=stadur
        self.þyngd=þyngd
        self.tennur=tennur



svar=0
while svar!="2":
    player1 = Nagdyr("Mús", 0, random.randrange(2, 7, 2),random.randint(1, 3),random.randrange(2, 7, 2))
    rotta1 = Nagdyr("Rotta", random.randrange(1, 100), random.randrange(2, 7, 2),random.randint(1, 3),random.randrange(2, 7, 2))
    rotta2 = Nagdyr("Rotta", random.randrange(1, 100), random.randrange(2, 7, 2),random.randint(1, 3),random.randrange(2, 7, 2))
    rotta3 = Nagdyr("Rotta", random.randrange(1, 100), random.randrange(2, 7, 2),random.randint(1, 3),random.randrange(2, 7, 2))
    hamstur = Nagdyr("Hamstur", random.randrange(1, 50), random.randrange(2, 7, 2),0,0)
    # Hérna tökum við aflið, þyngdinna og hversu hvassar tennur og leggjum það saman í power
    powermus = player1.afl + player1.þyngd + player1.tennur
    powerrotta1 = rotta1.afl + rotta1.þyngd + rotta1.tennur
    powerrotta2 = rotta2.afl + rotta2.þyngd + rotta2.tennur
    powerrotta3 = rotta3.afl + rotta3.þyngd + rotta3.tennur
    print(player1.tegund, player1.afl, player1.stadur,player1.þyngd,player1.tennur)
    print(rotta1.tegund, rotta1.afl, rotta1.stadur,rotta1.þyngd,rotta1.tennur)
    print(rotta2.tegund, rotta2.afl, rotta2.stadur,rotta2.þyngd,rotta2.tennur)
    print(rotta3.tegund, rotta3.afl, rotta3.stadur,rotta3.þyngd,rotta3.tennur)
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



                for x in range(player1.stadur, teningur+player1.stadur):

                    x=x+1
                    print(x)
                    if rotta1.stadur == x:

                        print("Þú ert á sama reit og rotta 1")
                        if powerrotta1 > powermus:
                            print("\nRottan vinnur\n")
                            player1.stadur = player1.stadur - teningur - rotta1.afl
                            print("Þú ferð til baka um",rotta1.afl,"marga reiti")
                        elif powerrotta1 < powermus:
                            print("\nPlayer 1 vinnur\n")
                        else:
                            print("Jafntefli")

                        #athuga hvort músin eða rottan hefur meira afl
                    elif rotta2.stadur == x:
                        print("Þú ert á sama reit og rotta 2")
                        if powerrotta2 > powermus:
                            print("\nRottan vinnur\n")
                            player1.stadur = player1.stadur - teningur - rotta2.afl
                            print("Þú ferð til baka um", rotta2.afl, "marga reiti")
                        elif powerrotta2 < powermus:
                            print("\nPlayer 1 vinnur\n")
                        else:
                            print("Jafntefli")

                    elif rotta3.stadur == x:
                        print("Þú ert á sama reit og rotta 3")
                        if powerrotta3 > powermus:
                            print("\nRottan vinnur\n")
                            player1.stadur = player1.stadur - teningur - rotta3.afl
                            print("Þú ferð til baka um", rotta3.afl, "marga reiti")
                        elif powerrotta3 < powermus:
                            print("\nPlayer 1 vinnur\n")
                        else:
                            print("Jafntefli")

                    elif hamstur.stadur == x:
                        print("\nHAMSTURINN KASTAR ÞÉR ÁFRAM!\n")
                        player1.stadur = player1.stadur + hamstur.afl
                        print("\n Þú lentir á reit",player1.stadur)

                player1.stadur = player1.stadur + teningur
                if player1.stadur < 0:
                    player1.stadur = 0
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
                            if powerrotta1 > powermus:
                                print("\nRotta 1 vinnur")
                                player1.stadur = player1.stadur - rotta1.afl
                                print("Þú ferð til baka um", rotta1.afl, "marga reiti")
                            elif powerrotta1 < powermus:
                                print("\nMúsin vinnur")
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
                            if powerrotta1 > powermus:
                                print("\nRotta 1 vinnur")
                                player1.stadur = player1.stadur - rotta1.afl
                                print("Þú ferð til baka um", rotta1.afl, "marga reiti")
                            elif powerrotta1 < powermus:
                                print("\nMúsin vinnur")
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
                            if powerrotta2 > powermus:
                                print("\nRotta 2 vinnur")
                                player1.stadur = player1.stadur - rotta2.afl
                                print("Þú ferð til baka um", rotta2.afl, "marga reiti")
                            elif powerrotta2 < powermus:
                                print("\nMúsin vinnur")
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
                            if powerrotta2 > powermus:
                                print("\nRotta 2 vinnur")
                                player1.stadur = player1.stadur - rotta2.afl
                                print("Þú ferð til baka um", rotta2.afl, "marga reiti")
                            elif powerrotta2 < powermus:
                                print("\nMúsin vinnur")
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
                            if powerrotta3 > powermus:
                                print("\nRotta 3 vinnur")
                                player1.stadur = player1.stadur - rotta3.afl
                                print("Þú ferð til baka um", rotta3.afl, "marga reiti")
                            elif powerrotta3 < powermus:
                                print("\nMúsin vinnur")
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
                            if powerrotta3 > powermus:
                                print("\nRotta vinnur")
                                player1.stadur = player1.stadur - rotta3.afl
                                print("Þú ferð til baka um", rotta3.afl, "marga reiti")
                            elif powerrotta3 < powermus:
                                print("\nPlayer 1 vinnur")
                                player1.stadur=player1.stadur + 2
                            else:
                                print("Jafntefli")
                    rotta3.stadur = rotta3.stadur - teningur
                    print("Rotta 3 er kominn á reit", rotta3.stadur)

                teningur = random.randint(1, 6)
                print("Núna kastar hamsturinn")
                if player1.stadur < 0:
                    player1.stadur = 0
                print("Hamsturinn fær",teningur)
                #Hvort hamsturinn fer áfram eða afturábak að músinni
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
                if player1.tennur == 2:
                    print("Þú hefur ekki hvassar tennur.")
                elif player1.tennur == 4:
                    print("Þú ert með hvassar tennur.")
                elif player1.tennur == 6:
                    print("Þú ert með MJÖG hvassar tennur.")
                print("Rotta 1",rotta1.stadur)
                if rotta1.tennur == 2:
                    print("Rotta 1 hefur ekki hvassar tennur.")
                elif rotta1.tennur == 4:
                    print("Rotta 1 er með hvassar tennur.")
                elif rotta1.tennur == 6:
                    print("Rotta 1 er með MJÖG hvassar tennur.")
                print("Rotta 2", rotta2.stadur)
                if rotta2.tennur == 2:
                    print("Rotta 2 hefur ekki hvassar tennur.")
                elif rotta2.tennur == 4:
                    print("Rotta 2 er með hvassar tennur.")
                elif rotta2.tennur == 6:
                    print("Rotta 2 er með MJÖG hvassar tennur.")
                print("Rotta 3", rotta3.stadur)
                if rotta3.tennur == 2:
                    print("Rotta 3 hefur ekki hvassar tennur.")
                elif rotta3.tennur == 4:
                    print("Rotta 3 er með hvassar tennur.")
                elif rotta3.tennur == 6:
                    print("Rotta 3 er með MJÖG hvassar tennur.")
                print("Hamstur", hamstur.stadur)






