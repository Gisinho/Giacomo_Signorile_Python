"""L'obiettivo di questo esercizio è identificare il kernel migliore dell'algoritmo SVM per classificare il tipo di fiore "setosa" e "virginica" del dataset iris.
Di seguito la base per importare il dataset e le classi specifiche"""
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn import datasets, metrics, svm

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y != 1, :2]
y = y[y != 1]

#grafico per vedere il dataset nella totalità
import matplotlib.pyplot as plt

_, ax = plt.subplots()
scatter = ax.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)
ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])
_ = ax.legend(
    scatter.legend_elements()[0], iris.target_names, loc="lower right", title="Classes"
)
plt.show()

# divisione dati addestramento e di test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)

#kernel da testare
kernels = ['linear', 'poly', 'rbf']
results = {}

# Addestramento e valutazione dei modelli SVM
for kernel in kernels:
    clf = SVC(kernel=kernel)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    results[kernel] = accuracy
    
    disp = metrics.ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
    disp.figure_.suptitle("Confusion Matrix")
    print(f"Confusion matrix:\n{disp.confusion_matrix}")
    plt.show()

    plt.show()
    print(f'Kernel: {kernel}, Accuracy: {accuracy}')

miglior_kernel = max(results, key=results.get)
print(f"Il miglior kernel è: {miglior_kernel} con un'accuratezza di {results[miglior_kernel]}")

