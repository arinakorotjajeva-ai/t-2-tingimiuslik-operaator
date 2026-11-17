# Küsi kahe inimese nimed. Kontrolli, kas mõlemad nimed koosnevad ainult tähtedest. 
# Kui jah, teata kasutajale, kas nad on täna pinginaabrid või mitte.
#  Kui mõnes nimes on numbreid või muid märke, kuva veateade.
# Otsusta ise, kuidas „pinginaabrid“ määratakse, 
# näiteks juhuslikult või nimede algustähtede järgi.
# Kasuta: isalpha(), capitalize()
pinginaabrid=["Mati"; "Kati"]
nimi1=imput("Sisesta nimi :")
nimi2=imput("Sisesta nimi :")
if nimi1.isalpha() and nimi2.isalpha():
    print(f"Tere (nimi. capitalize ()] ja (nimi2.capitalize ())]")
    if nimi.capitalize() in pinginaabrid:
     print(f"{nimi1} ja {nimi2} in pinginaabrid")
    else:
     print("Nad ei ole pinginaabrid")

else:
  print("Viga: nimed on valesti sisestatud! Kasuta ainult tähed")

  # 3. Remont
 # Küsi ristkülikukujulise toa pikkus ja laius ning arvuta põranda pindala.
# Seejärel küsi, kas kasutaja soovib remonti teha. Kui vastus on jaatav,
# küsi ruutmeetri hind ja arvuta põranda vahetamise hind.
# Lisaküsimus: kas kasutaja teeb remondi ise või kasutab professionaali abi?
# Professionaali puhul küsi ka töö hind ruutmeetri kohta ja 
# arvuta remondi koguhind koos tööga.
# Kasuta: float(), lower() 
# (vastuse „Jah“, „JAH“, „jah“ äratundmiseks), round()
 try: 
    piklus=float(int("Sisesta piklus"))
    laius=Float(inut("Sisesta laius")) 
    pindala(f"Pindala on {pindala}")
    remont=input(" Kas sovide remondi teha jah/ei?"). lower () #tähed on väikes
    if remont=="Jah":
        print("Teeme remonti!")
    try:
        rm_hind=Float(input("Sisesta ruutmetri hind: "))
        hind=round(pindala*rm_himda,2)
        print(f"Päranda vahetamise hind on {hind} euro")

