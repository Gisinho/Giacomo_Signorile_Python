import matplotlib.pyplot as plt

clienti = ['Giovanni', 'Bianco', 'Carlo', 'Dino', 'Ernesto']
età = [18, 27, 32, 45, 28]

plt.figure()
plt.bar(clienti, età, color='orange')
plt.title('Grafico a Barre')
plt.xlabel('Nomi')
plt.ylabel('Età')
plt.show()