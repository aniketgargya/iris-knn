import matplotlib.pyplot as plt
import pandas as pd
import math
import copy

k = 2

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


def genereateDistanceOfFlowerFunction(testFlower):
    def distanceOfFlower(trainFlower):
        return distance(testFlower, trainFlower)

    return distanceOfFlower


def distance(a, b):
    d = math.sqrt(
        ((a[0] - b[0]) ** 2)
        + ((a[1] - b[1]) ** 2)
        + ((a[2] - b[2]) ** 2)
        + ((a[3] - b[3]) ** 2)
    )
    return d


for testFlower in test:
    trainFlowers = copy.deepcopy(train)
    trainFlowers.sort(key=genereateDistanceOfFlowerFunction(testFlower))
    predictions = [0, 0, 0]
    for trainFlower in trainFlowers[0:k]:
        if trainFlower[4] == "setosa":
            predictions[0] = predictions[0] + 1
        if trainFlower[4] == "versicolor":
            predictions[1] = predictions[1] + 1
        if trainFlower[4] == "virginica":
            predictions[2] = predictions[2] + 1
    print(
        "setosa %s, versicolor %s, virginica %s"
        % (predictions[0] / k, predictions[1] / k, predictions[2] / k),
    )

