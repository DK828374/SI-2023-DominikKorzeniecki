import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# dane wejściowe
rok = np.array([[2000], [2002], [2005], [2007], [2010]])
bezrobocie = np.array([6.5, 7.0, 7.4, 8.2, 9.0])

# tworzymy obiekt regresji liniowej
reg = LinearRegression()

# trenujemy model na danych wejściowych
reg.fit(rok, bezrobocie)

# wyświetlamy wartości współczynników
print("Wartość współczynnika nachylenia wynosi: {:.3f}".format(reg.coef_[0]))
print("Wartość wyrazu wolnego wynosi: {:.3f}".format(reg.intercept_))

# dokonujemy predykcji dla lat 2000-2025
X_pred = np.array([[i] for i in range(2000, 2026)])
y_pred = reg.predict(X_pred)

# wyświetlamy, w którym roku przekroczy się 12% bezrobocia
for i in range(len(X_pred)):
    if y_pred[i] > 12.0:
        print("Procent bezrobotnych przekroczył 12% w roku {}".format(X_pred[i][0]))
        break



# Wykres regresji liniowej
model = LinearRegression().fit(rok, bezrobocie)
plt.scatter(rok, bezrobocie)
plt.plot(rok, model.predict(rok), color='red')
plt.title("Regresja liniowa procentu bezrobotnych")
plt.xlabel("Rok")
plt.ylabel("Procent bezrobotnych")
plt.show()
