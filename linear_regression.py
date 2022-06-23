import numpy as np
from math import log1p
from matplotlib import pyplot

x = [log1p(i) for i in [1479, 1595, 4301, 6470, 9740, 13282, 17784]]
y = [log1p(i) for i in [0.17470339296668025, 0.1619450650394475, 0.04886708418741835, 0.034249556520420395, 0.02618220048060735, 0.019986229124758337, 0.016356934880176668]]

sqr_x_sum = sum(i ** 2 for i in x)
x_sum = sum(i for i in x)
n = len(x)

x_y_sum = sum(x[i] * y[i] for i in range(len(x)))
y_sum = sum(i for i in y)

a = np.matrix([[sqr_x_sum, x_sum], [x_sum, n]])
b = np.matrix([[x_y_sum, 0], [y_sum, 0]])

x = np.linalg.inv(a) * b

a = 0.20031778
b = -6.51961438

x = [1479, 1595, 4301, 6470, 9740, 13282, 17784]
y = [x[i] * a + b for i in range(len(x))]

pyplot.scatter(x, y)
pyplot.plot(x, y, color="red")
pyplot.suptitle("coefficient of determination: 0.45804266361853196")
pyplot.show()
