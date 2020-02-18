from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

irisFlowers = pd.read_csv("iris.csv").values.tolist()

setosa = list(filter(lambda irisFlower: irisFlower[4] == "setosa", irisFlowers))
versicolor = list(filter(lambda irisFlower: irisFlower[4] == "versicolor", irisFlowers))
virginica = list(filter(lambda irisFlower: irisFlower[4] == "virginica", irisFlowers))

setosa_train = setosa[0:45]
setosa_test = setosa[45:50]

versicolor_train = versicolor[0:45]
versicolor_test = versicolor[45:50]

virginica_train = virginica[0:45]
virginica_test = virginica[45:50]

train = setosa_train + versicolor_train + virginica_train
test = setosa_test + versicolor_test + virginica_test


trainX = list(map(lambda x: x[0:4], train))
trainY = list(map(lambda x: x[4], train))
testX = list(map(lambda x: x[0:4], test))
testY = list(map(lambda x: x[4], test))

model = KNeighborsClassifier(n_neighbors=5)
model.fit(trainX, trainY)
print(model.predict(testX))
