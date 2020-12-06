mile = 0.62
odabir = 0

print("Dobrodošli! Svrha ovog programa je pretvaranje kilometara u milje.")
km = int(input("Molim unesite broj kilometara koje želite pretvoriti u milje:"))

while odabir != "ne":
    print(km * mile)
    odabir = input("Želite li izvršiti još jednu konverziju? da/ne")
    if odabir == "da":
        km = int(input("Molim unesite broj kilometara koje želite pretvoriti u milje:"))
    else:
        print("Doviđenja!")