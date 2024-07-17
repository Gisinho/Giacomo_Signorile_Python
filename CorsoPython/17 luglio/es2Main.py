import es2Funzioni as es2

def main():
    df = es2.crea_dataframe()
    
    while True:
        print("\nMenu")
        print("1. Aggiungi colonna Totale Vendite")
        print("2. Mostra totale vendite per prodotto")
        print("3. Trova prodotto più venduto")
        print("4. Trova città con maggiori vendite")
        print("5. Filtra vendite maggiori di 120 euro")
        print("6. Ordina vendite in ordine decrescente")
        print("7. Mostra quantità venduta per città")
        print("0. Esci")

        scelta = input("\nScegli un'operazione: ")
        
        if scelta == '1':
            es2.aggiungi_totale_vendite(df)
        elif scelta == '2':
            es2.raggruppare_totale_vendite(df)
        elif scelta == '3':
            es2.prodotto_piu_venduto(df)
        elif scelta == '4':
            es2.citta_massime_vendite(df)
        elif scelta == '5':
            es2.df_maggiori_vendite(df)
        elif scelta == '6':
            es2.vendite_desc(df)
        elif scelta == '7':
            es2.quantita_per_citta(df)
        elif scelta == '0':
            print("Arrivederci!")
            break
        else:
            print("Scelta non valida. Riprova.")

main()