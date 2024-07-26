import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv("https://raw.githubusercontent.com/madmashup/targeted-marketing-predictive-engine/master/banking.csv")
print(df)

""" def aggiungi_categoria(df): #aggiungo categoria al df usando il metodo apply per passare una funzione al df

    def categoria(job):
        df = df[df['job'] != 'unknown']
        if job == "student" or job == "unemployed" or job == "housemaid":
            return 0
        elif job == "blue-collar" or job == "technician" or job == "services" or job == "self-employed":
            return 1
        elif job == "retired" or job == "entrepreneur"or job == "management" or job == "admin.":
            return 2
            
    df['Categoria Lavoro'] = df['job'].apply(categoria)
    print("DataFrame con Categoria Lavoro: \n", df, "\n")
    return df

#aggiungi_categoria(df)
 """

def analisi_dati(df):

    df = df[df['job'] != 'unknown']
    
    def categoria(job):
        if job == "student" or job == "unemployed" or job == "housemaid":
            return 0
        elif job == "blue-collar" or job == "technician" or job == "services" or job == "self-employed":
            return 1
        elif job == "retired" or job == "entrepreneur"or job == "management" or job == "admin.":
            return 2
        else:
            return -1  

    df['job'] = df['job'].apply(categoria)

    #escludiamo gli unknown
    df = df[(df['default'] != 'unknown') & (df['housing'] != 'unknown') & (df['loan'] != 'unknown')]

    df.loc[:, 'default'] = df['default'].map(lambda x: 1 if x == 'yes' else 0)
    df.loc[:, 'housing'] = df['housing'].map(lambda x: 1 if x == 'yes' else 0)
    df.loc[:, 'loan'] = df['loan'].map(lambda x: 1 if x == 'yes' else 0)

    print("DataFrame modificato: \n", df)
    return df

def regressione_logistica(df):
    X = df[["age","job","default","housing", "loan", "campaign"]]       
    y = df["y"]
    #print(X.shape)
    #print(y.shape)

    # dividiamo i dati in train e test
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model = LogisticRegression(solver='liblinear', random_state=0).fit(X_train, y_train)
    predizione = model.predict(X_test)
    score = model.score(X_train, y_train)
    print("Score: ", score, "\n")
    print("classi:", model.classes_, "\n")
    print("intercetta:", model.intercept_, "\n")
    print("coefficienti:", model.coef_, "\n")

    cm = confusion_matrix(y_test, predizione)
    print(cm)

    #grafico della confusion matrix
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(cm)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
    ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
    ax.set_ylim(1.5, -0.5)
    for i in range(2):
        for j in range(2):
            ax.text(j, i, cm[i, j], ha='center', va='center', color='red')
    plt.show()

    #report
    print(classification_report(y_test, predizione))


df = analisi_dati(df)
regressione_logistica(df)