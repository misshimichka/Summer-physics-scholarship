import matplotlib.pyplot as plt
from math import log1p

REFERENCE_MULTEM_LAMBDA_0 = 8.155949067314925287e+02

LAMBDAS_0 = [815.7686337933283, 815.5949067314925, 815.5957126546452, 815.5957537150774,
             815.5957654762514, 815.5957654762514, 815.5957654762514]

figure = plt.figure()
ax = figure.add_subplot(1, 1, 1)
plt.xlabel("LMAX")
plt.ylabel("Lambda0")
ax.scatter([i for i in range(1, 8)], LAMBDAS_0, color='tab:purple')
plt.show()


f_multem = open("result_multem.txt").readlines()
s_m = [list(map(float, i.rstrip("\n").split("\t"))) for i in f_multem]

f_cst = open("result_cst.txt").readlines()
s_c = [list(map(float, i.rstrip("\n").split("\t"))) for i in f_cst]

f_comsol = open("result_comsol.txt").readlines()
s_cm = [list(map(float, i.rstrip("\n").split("\t"))) for i in f_comsol]


frequency_m = [i[0] for i in s_m]
reflectance_m = [i[1] for i in s_m]

figure = plt.figure()
ax = figure.add_subplot(1, 1, 1)
ax.scatter(frequency_m, reflectance_m, color='tab:purple')
plt.xlabel("Wavelength, nm")
plt.ylabel("Reflectance")
plt.suptitle("Multem")
plt.show()

program_name = input("Input program name -> ")

cst_lambda = open(f"{program_name}_lambda.txt").readlines()
cst_lambda = [float(i.rstrip("\n")) for i in cst_lambda]

cst_number_of_cells = open(f"{program_name}_filenames.txt").readlines()
cst_number_of_cells = [int(i.rstrip("\n")[:5].replace("_", "")) for i in cst_number_of_cells]

accuracy = [abs(cst_lambda[i] - REFERENCE_MULTEM_LAMBDA_0) / REFERENCE_MULTEM_LAMBDA_0 * 100 for i in range(len(cst_lambda))]

figure = plt.figure()
ax = figure.add_subplot(1, 1, 1)
ax.scatter(cst_number_of_cells, accuracy, color='tab:purple')

plt.xlabel("Количество ячеек сетки")
plt.ylabel("Погрешность, %")
plt.show()


x1 = cst_number_of_cells
y1 = accuracy
# x1 = [1479, 1595, 4301, 6470, 9740, 13282, 17784]
# y1 = [0.17470339296668025, 0.1619450650394475, 0.04886708418741835, 0.034249556520420395, 0.02618220048060735, 0.019986229124758337, 0.016356934880176668]

figure = plt.figure()
ax = figure.add_subplot(1, 1, 1)
ax.scatter(x1, y1, color='tab:purple')
plt.xscale("log")
plt.yscale("log")

plt.xlabel("Количество ячеек сетки")
plt.ylabel("Погрешность, %")
plt.show()


y = [abs(cst_lambda[i] - REFERENCE_MULTEM_LAMBDA_0) / REFERENCE_MULTEM_LAMBDA_0 * 100 for i in range(len(cst_lambda))]
x = cst_number_of_cells

x1 = sorted(x)[:-4]
y1 = []
for i in range(len(x)):
    if x[i] not in x1:
        y1.append(y[i])
x1 = sorted(x)[-4:]
print("Отсортированные х и у:", x1, y1)

figure = plt.figure()
ax = figure.add_subplot(1, 1, 1)

log_x = [log1p(x1[i] - 1) for i in range(len(x1))]
log_y = [log1p(y1[i] - 1) for i in range(len(y1))]

print("Логарифмированные х и у:", log_x, log_y)

ax.scatter(log_x, log_y, color='tab:purple')
plt.show()

print("y:", max([i[1] for i in s_m]))
print("y:", max([i[1] for i in s_c]))
print("y:", max([i[1] for i in s_cm]))

