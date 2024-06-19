n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))

scelta = input("Seleziona un'opzione: ")

print("1. Addizione")
print("2. Sottrazione")
print("3. Moltiplicazione")
print("4. Divisione")

if scelta == "1":
      print(n1+n2)  
elif scelta == "2":
    print(n1-n2)  
elif scelta == "3":
    print(n1*n2)
elif scelta == "4" and n2!=0:
    print(n1/n2)
else:
    print("Opzione non valida")