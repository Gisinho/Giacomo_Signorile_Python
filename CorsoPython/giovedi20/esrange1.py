numero = int(input("Inserire numero: "))

for i in range(numero,0, -1):
    print(i)

selezione = input("Vuoi ripetere l'operazione?(si/no): ").lower()

if selezione == "si":
    numero = int(input("Inserire numero: "))
    for i in range(numero,0, -1):
        print(i)
elif selezione == "no":
    print("Ok, buona giornata")        
else:
    print("Opzione non valida")