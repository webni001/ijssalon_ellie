mijn_dictionary = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}

aanbieding = mijn_dictionary["aardbei"] * 0.8

reclame_tekst =f"vandaag in de aanbieding: aardbeien-ijs, 1 liter - slechts € {aanbieding}"
reclame_tekst2 = reclame_tekst[: 65]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3
for el in reclame_tekst4 .lower():
    if el > 5:
print(el)
