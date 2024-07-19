import numpy as np
import matplotlib.pyplot as plt


x = np.random.rand(50)
y = np.random.rand(50)


colors = np.random.rand(50) 
plt.figure()
plt.scatter(x, y, c=colors)
plt.colorbar()
plt.title('Grafico a Dispersione con Colori e Dimensioni Variabili')
plt.xlabel('Asse X')
plt.ylabel('Asse Y')


plt.show()