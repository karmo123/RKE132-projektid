perekonnanimi=input("Sisesta oma perekonnanimi:")
sugu= input("Sisesta oma sugu (m või n):")
if sugu == "mees":
    print(f"Tere, härra {perekonnanimi}!")
elif sugu == "naine":
    print(f"Tere, proua {perekonnanimi}")
else:
    print(f"Tere, {perekonnanimi}!")
