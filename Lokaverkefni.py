#Lokaverkefni
#Ingólfur Óskarsson
#Guðlaugur Haukur Árnason
import random #Látið inn random



#Klassi búinn til
class Nagdyr:

    
    def __init__(self,tegund,stadur,afl,þyngd,tennur):#Smiðurinn búinn til
        self.tegund=tegund#Tegund af nagdýri
        self.afl=afl#Hversu mikið afl
        self.stadur=stadur#Staðsetningin
        self.þyngd=þyngd#Þyngdin
        self.tennur=tennur#Hversu hvassar tennur


#While lykkja
svar=0 #Svarið byrjar sem 0
while svar!="3":#Svo lengi að svarið er ekki 3, þá heldur lykkjan áfram
    oftkast1=0#Telur hversu oft spilari 1 kastar
    oftkast2=0#Telur hversu oft spilar 2 kastar
    player1 = Nagdyr("Mús", 0, random.randrange(2, 7, 2), random.randint(1, 3), random.randrange(2, 7, 2))#Stats fyrir player 1(tegund,afl,þyngd og tennur)
    player2 = Nagdyr("Mús", 0, random.randrange(2, 7, 2), random.randint(1, 3), random.randrange(2, 7, 2))#Stats fyrir player 2(tegund,afl,þyngd og tennur)
    rotta1 = Nagdyr("Rotta", random.randrange(1, 100), random.randrange(2, 7, 2),random.randint(1, 3),random.randrange(2, 7, 2))#Stats fyrir rottu 1(tegund,afl,staðsetning,þyngd og tennur)
    rotta2 = Nagdyr("Rotta", random.randrange(1, 100), random.randrange(2, 7, 2),random.randint(1, 3),random.randrange(2, 7, 2))#Stats fyrir rottu 2(tegund,afl,staðsetning,þyngd og tennur)
    rotta3 = Nagdyr("Rotta", random.randrange(1, 100), random.randrange(2, 7, 2),random.randint(1, 3),random.randrange(2, 7, 2))#Stats fyrir rottur 3(tegund,afl,staðsetning,þyngd og tennur)
    hamstur = Nagdyr("Hamstur", random.randrange(1, 50), random.randrange(2, 7, 2),0,0)#Stats fyrir hamstur(tegund,afl og staðsetning)
    kaninan = Nagdyr("Kaninan", random.randrange(1, 50), random.randrange(2, 7, 2), 0, 0)#Stats fyrir kaninu(tegund,afl og staðsetning)
    # Hérna tökum við aflið, þyngdinna og hversu hvassar tennur og leggjum það saman í power
    powermus = player1.afl + player1.þyngd + player1.tennur
    powermus2 = player2.afl + player2.þyngd + player2.tennur
    powerrotta1 = rotta1.afl + rotta1.þyngd + rotta1.tennur
    powerrotta2 = rotta2.afl + rotta2.þyngd + rotta2.tennur
    powerrotta3 = rotta3.afl + rotta3.þyngd + rotta3.tennur
    print("-----Nagdýr-----")
    print("1 - Spila Einn")
    print("2 - Spila Tveir")
    print("3 - Hætta")
    print("-----------------")
    svar=input("Sláðu inn tölu frá bilinu 1-3 ")
    #Tjekkar hvort player 2 er með
    tvoplayer=0
    if svar == "2":
        tvoplayer=1
        svar = "1"

    if svar=="1":
        svar1=0
        while svar1!="3":#While lykkja fyrir leikinn sjálfan
            print("\n-----Valmynd-----")
            print("1 - Kasta teningi?")
            print("2 - Staðsetning?")
            print("3 - Hætta")
            print("-------------------")
            svar1=input("Sláðu inn tölu frá bilinu 1-3 ")



            if svar1=="1":
                print("\n------Mús 1-------")
                print("Mús 1 kastar teningi ")
                teningur = random.randint(1, 6)
                print("Mús 1 fékk =", teningur)


                #For lykkja til að tjekka hvort rotta eða hamstur er á sama reit
                for x in range(player1.stadur, teningur+player1.stadur):

                    x=x+1
                    if rotta1.stadur == x:

                        print("Þú ert á sama reit og rotta 1")
                        #bardagi á milli rottu og mús
                        if powerrotta1 > powermus:
                            print("\nRottan vinnur\n")
                            player1.stadur = player1.stadur - teningur - rotta1.afl
                            print("Þú ferð til baka um",rotta1.afl,"marga reiti")
                        elif powerrotta1 < powermus:
                            print("\nMús 1 vinnur\n")
                        else:
                            print("Jafntefli")#Ef það er jafntefli þá gerist ekkert

                        #athuga hvort músin eða rottan hefur meira afl
                    elif rotta2.stadur == x:
                        print("Þú ert á sama reit og rotta 2")
                        if powerrotta2 > powermus:
                            print("\nRottan vinnur\n")
                            player1.stadur = player1.stadur - teningur - rotta2.afl
                            print("Þú ferð til baka um", rotta2.afl, "marga reiti")
                        elif powerrotta2 < powermus:
                            print("\nMús 1 vinnur\n")
                        else:
                            print("Jafntefli")

                    elif rotta3.stadur == x:
                        print("Þú ert á sama reit og rotta 3")
                        if powerrotta3 > powermus:
                            print("\nRottan vinnur\n")
                            player1.stadur = player1.stadur - teningur - rotta3.afl
                            print("Þú ferð til baka um", rotta3.afl, "marga reiti")
                        elif powerrotta3 < powermus:
                            print("\nMús 1 vinnur\n")
                        else:
                            print("Jafntefli")

                    elif hamstur.stadur == x:#Ef mús/hamstur rekst á hvorn annan þá kastar hamsturinn honum áfram
                        print("\nHAMSTURINN KASTAR ÞÉR ÁFRAM!\n")
                        player1.stadur = player1.stadur + hamstur.afl
                        print("\n Þú lentir á reit",player1.stadur)

                oftkast1=oftkast1 + 1#Telur kast
                player1.stadur = player1.stadur + teningur
                if player1.stadur < 0:#Ef spilarinn fer í mínus, þá er hann settur aftur í 0
                    player1.stadur = 0
                print("Þú ert á reit", player1.stadur)

                if tvoplayer == 1:#Ef player 2 er með þá fer þessi if setning í gang
                    print("\n------Mús 2-------")
                    print("Nú kastar mús 2 ")
                    teningur = random.randint(1, 6)
                    print("Mús 2 fékk =", teningur)

                    for x in range(player2.stadur, teningur + player2.stadur):#For lykkja fyrir player 2 hvort hann rekst á rottu eða kanínu

                        x = x + 1
                        if rotta1.stadur == x:

                            print("Þú ert á sama reit og rotta 1")
                            if powerrotta1 > powermus2:
                                print("\nRottan vinnur\n")
                                player2.stadur = player2.stadur - teningur - rotta1.afl
                                print("Þú ferð til baka um", rotta1.afl, "marga reiti")
                            elif powerrotta1 < powermus2:
                                print("\nMús 2 vinnur\n")
                            else:
                                print("Jafntefli")

                                # athuga hvort músin eða rottan hefur meira afl
                        elif rotta2.stadur == x:
                            print("Þú ert á sama reit og rotta 2")
                            if powerrotta2 > powermus2:
                                print("\nRottan vinnur\n")
                                player2.stadur = player2.stadur - teningur - rotta2.afl
                                print("Þú ferð til baka um", rotta2.afl, "marga reiti")
                            elif powerrotta2 < powermus2:
                                print("\nMús 2 vinnur\n")
                            else:
                                print("Jafntefli")

                        elif rotta3.stadur == x:
                            print("Þú ert á sama reit og rotta 3")
                            if powerrotta3 > powermus:
                                print("\nRottan vinnur\n")
                                player2.stadur = player2.stadur - teningur - rotta3.afl
                                print("Þú ferð til baka um", rotta3.afl, "marga reiti")
                            elif powerrotta3 < powermus2:
                                print("\nMús 2 vinnur\n")
                            else:
                                print("Jafntefli")

                        elif hamstur.stadur == x:
                            print("\nHAMSTURINN KASTAR ÞÉR ÁFRAM!\n")
                            player2.stadur = player2.stadur + hamstur.afl
                            print("\n Þú lentir á reit", player2.stadur)

                    oftkast2=oftkast2 + 1#telur kast
                    player2.stadur = player2.stadur + teningur
                    if player2.stadur < 0:
                        player2.stadur = 0
                    print("Þú ert á reit", player2.stadur)

                teningur = random.randint(1, 6)
                print("\nNúna kasta rotturnar\n")
                print("------Rotta 1-------")
                att1=random.randint(1,2)#Ákveður í hvaða átt rottan fer í
                if att1 == 1:
                    print("Rotta 1 fær", teningur,"og fer áfram")
                    for x in range(rotta1.stadur,rotta1.stadur+teningur):
                        x=x+1
                        if player1.stadur == x:
                            print("Rotta 1 hittir mús 1")
                            if powerrotta1 > powermus:#bardagi á milli rottu og mús
                                print("\nRotta 1 vinnur")
                                player1.stadur = player1.stadur - rotta1.afl
                                print("Mús 1 fer til baka um", rotta1.afl, "marga reiti")
                            elif powerrotta1 < powermus:
                                print("\nMúsin vinnur")
                                player1.stadur=player1.stadur + 2
                                print("Mús 1 fer áfram um 2")
                                print("Mús 1 er kominn á reit", player1.stadur)
                            else:
                                print("Jafntefli")
                    if tvoplayer == 1:
                        for x in range(rotta1.stadur, rotta1.stadur + teningur):
                            x = x + 1
                            if player2.stadur == x:
                                print("Rotta 1 hittir mús 2")
                                if powerrotta1 > powermus2:
                                    print("\nRotta 1 vinnur")
                                    player2.stadur = player2.stadur - rotta1.afl
                                    print("Mús 2 fer til baka um", rotta1.afl, "marga reiti")
                                elif powerrotta1 < powermus2:
                                    print("\nMúsin vinnur")
                                    player2.stadur = player2.stadur + 2
                                    print("Mús 2 fer áfram um 2")
                                    print("Mús 2 er kominn á reit",player2.stadur)
                                else:
                                    print("Jafntefli")

                    rotta1.stadur = rotta1.stadur + teningur
                    if rotta1.stadur > 100:#Ef rotta fer yfir 100 þá fer hún til baka í 100
                        rotta1.stadur = 100
                    print("Rotta 1 er kominn á reit", rotta1.stadur,"\n")
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
                                print("Mús 1 fer áfram um 2")#Ef rotta rekst á mús og músin vinnur, þá fer hún áfram um 2
                                print("Mús 1 er kominn á reit", player1.stadur)
                            else:
                                print("Jafntefli")
                    if tvoplayer == 1:
                        for x in range(rotta1.stadur, rotta1.stadur + teningur):
                            x = x + 1
                            if player2.stadur == x:
                                print("Rotta 1 hittir mús 2")
                                if powerrotta1 > powermus2:
                                    print("\nRotta 1 vinnur")
                                    player2.stadur = player2.stadur - rotta1.afl
                                    print("Mús 2 fer til baka um", rotta1.afl, "marga reiti")
                                elif powerrotta1 < powermus2:
                                    print("\nMúsin vinnur")
                                    player2.stadur = player2.stadur + 2
                                    print("Mús 2 fer áfram um 2")
                                    print("Mús 2 er kominn á reit",player2.stadur)
                                else:
                                    print("Jafntefli")
                    rotta1.stadur = rotta1.stadur - teningur
                    print("Rotta 1 er kominn á reit", rotta1.stadur,"\n")

                teningur = random.randint(1, 6)
                print("------Rotta 2-------")
                att2 = random.randint(1 , 2)
                if att2 == 1:
                    print("Rotta 2 fær", teningur, "og fer áfram")
                    for x in range(rotta2.stadur,rotta2.stadur + teningur):
                        x=x+1
                        if player1.stadur == x:
                            print("\nRotta 2 hittir mús")
                            if powerrotta2 > powermus:
                                print("\nRotta 2 vinnur")
                                player1.stadur = player1.stadur - rotta2.afl
                                print("Þú ferð til baka um", rotta2.afl, "marga reiti")
                            elif powerrotta2 < powermus:
                                print("\nMúsin vinnur")
                                player1.stadur=player1.stadur + 2
                                print("Mús 1 fer áfram um 2")
                                print("Mús 1 er kominn á reit", player1.stadur)
                            else:
                                print("Jafntefli")
                    if tvoplayer == 1:
                        for x in range(rotta2.stadur, rotta2.stadur + teningur):
                            x = x + 1
                            if player2.stadur == x:
                                print("\nRotta 2 hittir mús 2")
                                if powerrotta2 > powermus2:
                                    print("\nRotta 2 vinnur")
                                    player2.stadur = player2.stadur - rotta2.afl
                                    print("Mús 2 fer til baka um", rotta2.afl, "marga reiti")
                                elif powerrotta2 < powermus2:
                                    print("\nMúsin vinnur")
                                    player2.stadur = player2.stadur + 2
                                    print("Mús 2 fer áfram um 2")
                                    print("Mús 2 er kominn á reit",player2.stadur)
                                else:
                                    print("Jafntefli")
                    rotta2.stadur = rotta2.stadur + teningur
                    if rotta2.stadur > 100:
                        rotta2.stadur = 100
                    print("Rotta 2 er kominn á reit", rotta2.stadur,"\n")
                elif att2 == 2:
                    print("Rotta 2 fær", teningur, "og fer til baka")
                    for x in range(rotta2.stadur,rotta2.stadur - teningur,-2):
                        x=x-1
                        if player1.stadur == x:
                            print("\nRotta 2 hittir mús")
                            if powerrotta2 > powermus:
                                print("\nRotta 2 vinnur")
                                player1.stadur = player1.stadur - rotta2.afl
                                print("Þú ferð til baka um", rotta2.afl, "marga reiti")
                            elif powerrotta2 < powermus:
                                print("\nMúsin vinnur")
                                player1.stadur=player1.stadur + 2
                                print("Mús 1 fer áfram um 2")
                                print("Mús 1 er kominn á reit", player1.stadur)
                            else:
                                print("Jafntefli")
                    if tvoplayer == 1:
                        for x in range(rotta2.stadur, rotta2.stadur + teningur):
                            x = x + 1
                            if player2.stadur == x:
                                print("\nRotta 2 hittir mús 2")
                                if powerrotta2 > powermus2:
                                    print("\nRotta 2 vinnur")
                                    player2.stadur = player2.stadur - rotta2.afl
                                    print("Mús 2 fer til baka um", rotta2.afl, "marga reiti")
                                elif powerrotta2 < powermus2:
                                    print("\nMúsin vinnur")
                                    player2.stadur = player2.stadur + 2
                                    print("Mús 2 fer áfram um 2")
                                    print("Mús 2 er kominn á reit",player2.stadur)
                                else:
                                    print("Jafntefli")
                    rotta2.stadur = rotta2.stadur - teningur
                    print("Rotta 2 er kominn á reit", rotta2.stadur,"\n")

                teningur = random.randint(1, 6)
                print("------Rotta 3-------")
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
                                print("Mús 1 fer áfram um 2")
                                print("Mús 1 er kominn á reit", player1.stadur)
                            else:
                                print("Jafntefli")
                    if tvoplayer == 1:
                        for x in range(rotta3.stadur, rotta3.stadur + teningur):
                            x = x + 1
                            if player2.stadur == x:
                                print("\nRotta 3 hittir mús 2")
                                if powerrotta3 > powermus2:
                                    print("\nRotta 3 vinnur")
                                    player2.stadur = player2.stadur - rotta3.afl
                                    print("Mús 2 fer til baka um", rotta3.afl, "marga reiti")
                                elif powerrotta3 < powermus2:
                                    print("\nMúsin vinnur")
                                    player2.stadur = player2.stadur + 2
                                    print("Mús 2 fer áfram um 2")
                                    print("Mús 2 er kominn á reit",player2.stadur)
                                else:
                                    print("Jafntefli")
                    rotta3.stadur = rotta3.stadur + teningur
                    if rotta3.stadur > 100:
                        rotta3.stadur = 100
                    print("Rotta 3 er kominn á reit", rotta3.stadur,"\n")
                elif att3 == 2:
                    print("Rotta 3 fær", teningur, "og fer til baka")
                    for x in range(rotta3.stadur,rotta3.stadur - teningur,-1):
                        x=x-1
                        if player1.stadur == x:
                            print("\nRotta 1 hittir mús 1")
                            if powerrotta3 > powermus:
                                print("\nRotta vinnur")
                                player1.stadur = player1.stadur - rotta3.afl
                                print("Þú ferð til baka um", rotta3.afl, "marga reiti")
                            elif powerrotta3 < powermus:
                                print("\nMúsin vinnur")
                                player1.stadur=player1.stadur + 2
                                print("Mús 1 fer áfram um 2")
                                print("Mús 1 er kominn á reit", player1.stadur)
                            else:
                                print("Jafntefli")
                    if tvoplayer == 1:
                        for x in range(rotta3.stadur, rotta3.stadur + teningur):
                            x = x + 1
                            if player2.stadur == x:
                                print("\nRotta 3 hittir mús 2")
                                if powerrotta3 > powermus2:
                                    print("\nRotta 3 vinnur")
                                    player2.stadur = player2.stadur - rotta3.afl
                                    print("Mús 2 fer til baka um", rotta3.afl, "marga reiti")
                                elif powerrotta3 < powermus2:
                                    print("\nMúsin vinnur")
                                    player2.stadur = player2.stadur + 2
                                    print("Mús 2 fer áfram um 2")
                                    print("Mús 2 er kominn á reit",player2.stadur)
                                else:
                                    print("Jafntefli")
                    rotta3.stadur = rotta3.stadur - teningur
                    print("Rotta 3 er kominn á reit", rotta3.stadur,"\n")

                teningur = random.randint(1, 6)
                print("\n------Hamsturinn-------")
                print("Núna kastar hamsturinn")
                if player1.stadur < 0:
                    player1.stadur = 0
                if player2.stadur < 0:
                    player2.stadur = 0
                print("Hamsturinn fær",teningur)
                #Hvort hamsturinn fer áfram eða afturábak að músinni
                if player1.stadur > hamstur.stadur:
                #Hvort að hamstur Rekst á mús
                    for x in range(hamstur.stadur,hamstur.stadur+teningur):
                        x=x+1
                        if player1.stadur == x:
                            print("\nHAMSTURINN KASTAR ÞÉR ÁFRAM!")
                            player1.stadur=player1.stadur + hamstur.afl
                            print("Þú lentir á reit",player1.stadur,"\n")
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
                        if player1.stadur == x:
                            print("\nHAMSTURINN KASTAR ÞÉR ÁFRAM!")
                            player1.stadur=player1.stadur + hamstur.afl#Ef hamstur/kanínan lendir á spilara, þá kastar hún honum með aflinu sínu
                            print("Þú lentir á reit",player1.stadur,"\n")
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
                if player1.stadur >=100:#Ef þú lendir á hundrað eða ferð yfir þá vinnur þú leikinn
                    print("Til hamingju Mús 1 þú vannst! ")
                    print("     III")
                    print("   IIIIIII")
                    print(" IIII   IIII")
                    print("IIII  1  IIII")                 #bikar
                    print(" IIII   IIII")
                    print("   IIIIIII")
                    print("     III")
                    print("     III")
                    print("     III")
                    print("     III")
                    print("    IIIII")
                    print("   IIIIIII")
                    print("\n Þú Kastaðir Teningnum",oftkast1,"Sinnum")#Sýnir hversu oft þú þurftir að kasta
                    svar1="3"

                if tvoplayer == 1:
                    teningur = random.randint(1, 6)
                    print("\n------Kaninan-------")
                    print("Núna kastar Kaninan")
                    print("Kaninan fær", teningur)
                    # Hvort kaninan fer áfram eða afturábak að músinni
                    if player2.stadur > kaninan.stadur:
                        # Hvort að hamstur fer framhjá mús
                        for x in range(kaninan.stadur, kaninan.stadur + teningur):
                            x = x + 1
                            if player2.stadur == x:
                                print("\nKANÍNAN KASTAR ÞÉR ÁFRAM!")
                                player2.stadur = player2.stadur + hamstur.afl
                                print("Þú lentir á reit",player2.stadur,"\n")
                        kaninan.stadur = kaninan.stadur + teningur
                        # Tjekkar hvort kanína og rotta er á sama stað
                        if kaninan.stadur == rotta1.stadur:
                            print("Kaninan lenti á sama reit og rotta 1")
                            if att1 == 1:
                                rotta1.stadur = rotta1.stadur - 1
                                print("Rottan fer einn afturábak")
                                print("Rotta 1 er á reit", rotta1.stadur)
                                print("Kaninan fer einn afturábak")
                                kaninan.stadur = kaninan.stadur - 1
                            elif att1 == 2:
                                rotta1.stadur = rotta1.stadur + 1
                                print("Rottan fer einn áfram")
                                print("Rotta 1 er á reit", rotta1.stadur)
                                print("Kaninan fer einn afturábak")
                                kaninan.stadur = kaninan.stadur - 1

                        elif kaninan.stadur == rotta2.stadur:
                            print("Kaninan lenti á sama reit og rotta 1")
                            if att2 == 1:
                                rotta2.stadur = rotta2.stadur - 1
                                print("Rottan fer einn afturábak")
                                print("Rotta 2 er á reit", rotta2.stadur)
                                print("Kaninan fer einn afturábak")
                                kaninan.stadur = kaninan.stadur - 1
                            elif att2 == 2:
                                rotta1.stadur = rotta2.stadur + 1
                                print("Rottan fer einn áfram")
                                print("Rotta 2 er á reit", rotta2.stadur)
                                print("Kaninan fer einn afturábak")
                                kaninan.stadur = kaninan.stadur - 1

                        elif kaninan.stadur == rotta3.stadur:
                            print("Kaninan lenti á sama reit og rotta 1")
                            if att3 == 1:
                                rotta3.stadur = rotta3.stadur - 1
                                print("Rottan fer einn afturábak")
                                print("Rotta 3 er á reit", rotta3.stadur)
                                print("Kaninan fer einn afturábak")
                                kaninan.stadur = kaninan.stadur - 1
                            elif att3 == 2:
                                rotta3.stadur = rotta3.stadur + 1
                                print("Rottan fer einn áfram")
                                print("Rotta 3 er á reit", rotta3.stadur)
                                print("Kaninan fer einn afturábak")
                                kaninan.stadur = kaninan.stadur - 1

                    elif player2.stadur < kaninan.stadur:
                        # Hvort að Kanina fer framhjá mús
                        for x in range(kaninan.stadur, kaninan.stadur - teningur, -1):
                            if player2.stadur == x:
                                print("\nKANÍNAN KASTAR ÞÉR ÁFRAM!")
                                player2.stadur = player2.stadur + kaninan.afl
                                print("Þú lentir á reit",player2.stadur,"\n")
                        kaninan.stadur = kaninan.stadur - teningur
                        # Tjekkar hvort kanina og rotta er á sama stað
                        if kaninan.stadur == rotta1.stadur:
                            print("Kaninan lenti á sama reit og rotta 1")
                            if att1 == 1:
                                rotta1.stadur = rotta1.stadur - 1
                                print("Rottan fer einn afturábak")
                                print("Rotta 1 er á reit", rotta1.stadur)
                                print("Kaninan fer einn áfram")
                                kaninan.stadur = kaninan.stadur + 1
                            elif att1 == 2:
                                rotta1.stadur = rotta1.stadur + 1
                                print("Rottan fer einn áfram")
                                print("Rotta 1 er á reit", rotta1.stadur)
                                print("Kaninan fer einn áfram")
                                kaninan.stadur = kaninan.stadur + 1

                        elif kaninan.stadur == rotta2.stadur:
                            print("Kaninan lenti á sama reit og rotta 1")
                            if att2 == 1:
                                rotta2.stadur = rotta2.stadur - 1
                                print("Rottan fer einn afturábak")
                                print("Rotta 2 er á reit", rotta2.stadur)
                                print("Kaninan fer einn áfram")
                                kaninan.stadur = kaninan.stadur + 1
                            elif att2 == 2:
                                rotta1.stadur = rotta2.stadur + 1
                                print("Rottan fer einn áfram")
                                print("Rotta 2 er á reit", rotta2.stadur)
                                print("Kaninan fer einn áfram")
                                kaninan.stadur = kaninan.stadur + 1

                        elif kaninan.stadur == rotta3.stadur:
                            print("Kaninan lenti á sama reit og rotta 1")
                            if att3 == 1:
                                rotta3.stadur = rotta3.stadur - 1
                                print("Rottan fer einn afturábak")
                                print("Rotta 3 er á reit", rotta3.stadur)
                                print("Kaninan fer einn áfram")
                                kaninan.stadur = kaninan.stadur + 1
                            elif att3 == 2:
                                rotta3.stadur = rotta3.stadur + 1
                                print("Rottan fer einn áfram")
                                print("Rotta 3 er á reit", rotta3.stadur)
                                print("Kanínan fer einn áfram")
                                kaninan.stadur = kaninan.stadur + 1

                    print("Kanínan er kominn á reit", kaninan.stadur)
                    if player2.stadur >= 100:
                        print("Til hamingju Mús 2 þú vannst! ")
                        print("     III")
                        print("   IIIIIII")
                        print(" IIII   IIII")
                        print("IIII  1  IIII") #bikar
                        print(" IIII   IIII")
                        print("   IIIIIII")
                        print("     III")
                        print("     III")
                        print("     III")
                        print("     III")
                        print("    IIIII")
                        print("   IIIIIII")
                        print("\n Þú Kastaðir Teningnum",oftkast2,"Sinnum")
                        svar1 = "3"

            elif    svar1=="2":
                #Hér er sýnt alla stats á öllum nagdýronum
                print("Mús 1 er á reit",player1.stadur)
                print("Mús 1 er",player1.þyngd,"kg.")
                if player1.tennur == 2:
                    print("Mús 1 hefur ekki hvassar tennur.")
                elif player1.tennur == 4:
                    print("Mús 1 ert með hvassar tennur.")
                elif player1.tennur == 6:
                    print("Mús 1 ert með MJÖG hvassar tennur.")
                if tvoplayer == 1:#Ef player 2 er með þá fer þessi if setning í gang
                    print("Mús 2 er á reit", player2.stadur)
                    print("Mús 2 er",player2.þyngd,"kg.")
                    if player2.tennur == 2:
                        print("Mús 2 hefur ekki hvassar tennur.")
                    elif player2.tennur == 4:
                        print("Mús 2 ert með hvassar tennur.")
                    elif player2.tennur == 6:
                        print("Mús 2 ert með MJÖG hvassar tennur.")
                print("Rotta 1 er á reit",rotta1.stadur)
                print("Rotta 1 er",rotta1.þyngd,"kg")
                if rotta1.tennur == 2:
                    print("Rotta 1 hefur ekki hvassar tennur.")
                elif rotta1.tennur == 4:
                    print("Rotta 1 er með hvassar tennur.")
                elif rotta1.tennur == 6:
                    print("Rotta 1 er með MJÖG hvassar tennur.")
                print("Rotta 2 er á reit", rotta2.stadur)
                print("Rotta 2 er", rotta2.þyngd, "kg")
                if rotta2.tennur == 2:
                    print("Rotta 2 hefur ekki hvassar tennur.")
                elif rotta2.tennur == 4:
                    print("Rotta 2 er með hvassar tennur.")
                elif rotta2.tennur == 6:
                    print("Rotta 2 er með MJÖG hvassar tennur.")
                print("Rotta 3 er á reit", rotta3.stadur)
                print("Rotta 3 er", rotta3.þyngd, "kg")
                if rotta3.tennur == 2:
                    print("Rotta 3 hefur ekki hvassar tennur.")
                elif rotta3.tennur == 4:
                    print("Rotta 3 er með hvassar tennur.")
                elif rotta3.tennur == 6:
                    print("Rotta 3 er með MJÖG hvassar tennur.")
                print("Hamstur er á reit", hamstur.stadur)
                if tvoplayer == 1:
                    print("Kanínan er á reit",kaninan.stadur)
