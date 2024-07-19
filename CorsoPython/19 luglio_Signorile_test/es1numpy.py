import numpy as np

def genera_temperature(n, minimo, massimo):
    #dataset randomico di 24 numeri che rappresentano le temperature registrate
    temperature = np.random.randint(minimo, massimo, size=24)
    return temperature

def calcola_media(temperature):#calcola la temp media
    t_media = np.mean(temperature)
    return t_media

def calcola_temperatura_minima(temperature):#calcola la temp media
    t_min = np.min(temperature)
    return t_min

def calcola_temperatura_massima(temperature):#calcola la temp media
    t_max = np.max(temperature)
    return t_max

def prob_temperatura(ultima_temp,ore=4, aumento_giornaliero=0.2):
    aumento_ora = aumento_giornaliero/24
    prossime_temperature = []
    for i in range(1, ore + 1):
        prossime_temperature.append(i * aumento_ora+ultima_temp)
    return prossime_temperature


temperature = genera_temperature(24, 15, 35)
print(f"Lista temperature:{temperature}")    
# Calcola e stampa la temperatura media
t_media = calcola_media(temperature)
print(f"Temperatura media: {t_media:.2f}°C")
    
# Calcola e stampa la temperatura minima
t_min = calcola_temperatura_minima(temperature)
print(f"Temperatura minima: {t_min}°C")
    
# Calcola e stampa la temperatura massima
t_max = calcola_temperatura_massima(temperature)
print(f"Temperatura massima: {t_max}°C")
    
# Calcola e stampa la previsione delle temperature per le prossime 4 ore
ultima_temp = temperature[-1] #prendo l'ultima temperatura della lista
prossime_temp = prob_temperatura(ultima_temp)
print(f"Prossime temperature previste: {prossime_temp}")


