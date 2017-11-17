import random
svar=0
while svar!="2":
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











