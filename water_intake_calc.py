klaaside_arv=int(input("Mitu klaasi vett oled joonud?"))
vee_kogus=klaaside_arv* 250
protsent=vee_kogus / 2000 * 100
print(f"Päevanormist on täidetud  {protsent:.1f}%.")

if protsent < 50:
    print("Joo rohkem vett, keha vajab seda!")
elif protsent < 100:
    print("Tubli, jätka samas vaimus!")
else:
    print("Suurepärane, oled oma päevase eesmärgi täitnud!")