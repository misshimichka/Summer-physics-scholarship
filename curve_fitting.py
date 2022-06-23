from numpy import arange
import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot


# define the true objective function
def exponential(x, a, b):
    return a * np.exp(b * x)


REFERENCE_MULTEM_LAMBDA_0 = 8.155949067314925287e+02
cst_lambda = [815.5011974984836, 814.1700347565692, 815.5094833215086, 814.2740910293278, 815.1963492817918,
              815.3155690929339, 815.3813660379025, 815.4319000647033, 815.4615004037124, 815.4780677945943,
              815.4893987606894]

x = [abs(cst_lambda[i] - REFERENCE_MULTEM_LAMBDA_0) / REFERENCE_MULTEM_LAMBDA_0 * 100 for i in range(len(cst_lambda))]
y = [exponential(x[i], 1, 1) for i in range(len(x))]
pyplot.scatter(x, y, s=20, color='#00b3b3', label='Data')
pyplot.yscale('log')
pyplot.show()

popt, _ = curve_fit(exponential, x, y)
a, b = popt

pyplot.scatter(x, y)
# define a sequence of inputs between the smallest and largest known inputs
x_line = arange(min(x), max(x), 1)
# calculate the output for the range
y_line = exponential(x_line, a, b)
# create a line plot for the mapping function
pyplot.plot(x_line, y_line, '--', color='red')
pyplot.show()
