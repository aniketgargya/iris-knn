import matplotlib.pyplot as plt
import pandas as pd

irisFlowers = pd.read_csv("iris.csv").values.tolist()


def createReturnListIndex(listIndex):
    def returnListIndex(inputElement):
        return inputElement[listIndex]

    return returnListIndex


def returnColors(inputElement):
    if inputElement[4] == "setosa":
        return "red"
    elif inputElement[4] == "versicolor":
        return "green"
    elif inputElement[4] == "virginica":
        return "blue"
    else:
        return "purple"


x_vals = list(map(createReturnListIndex(2), irisFlowers))
y_vals = list(map(createReturnListIndex(3), irisFlowers))
color_vals = list(map(returnColors, irisFlowers))

plt.scatter(x_vals, y_vals, color=color_vals)

plt.show()
