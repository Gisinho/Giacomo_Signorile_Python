from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Caricamento del dataset e selezione delle classi specifiche
iris = datasets.load_iris()
X = iris.data[y != 1, :2]  # Utilizziamo solo le prime due caratteristiche
y = iris.target[y != 1]  # Escludiamo la classe "versicolor"

# Divisione dei dati in set di addestramento e di test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Definizione dei kernel da testare
kernels = ['linear', 'poly', 'rbf']
results = {}

# Addestramento e valutazione dei modelli SVM
for kernel in kernels:
    clf = SVC(kernel=kernel)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    results[kernel] = accuracy
    print(f'Kernel: {kernel}, Accuracy: {accuracy:.2f}')

# Identificazione del miglior kernel
best_kernel = max(results, key=results.get)
print(f"Il miglior kernel è: {best_kernel} con un'accuratezza di {results[best_kernel]:.2f}")
