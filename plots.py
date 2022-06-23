import matplotlib.pyplot as plt

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

frequency_m = [i[0] for i in s_m]
reflectance_m = [i[1] for i in s_m]

figure = plt.figure()
ax = figure.add_subplot(1, 1, 1)
ax.scatter(frequency_m, reflectance_m, color='tab:purple')
plt.xlabel("Wavelength, nm")
plt.ylabel("Reflectance")
plt.suptitle("Multem")
plt.show()


cst_lambda = open("cst_lambda.txt").readlines()
cst_lambda = [float(i.rstrip("\n")) for i in cst_lambda]

cst_number_of_cells = open("cst_filenames.txt").readlines()
cst_number_of_cells = [int(i.rstrip("\n")[:5].replace("_", "")) for i in cst_number_of_cells]

accuracy = [abs(cst_lambda[i] - REFERENCE_MULTEM_LAMBDA_0) / REFERENCE_MULTEM_LAMBDA_0 * 100 for i in range(len(cst_lambda))]

figure = plt.figure()
ax = figure.add_subplot(1, 1, 1)
ax.scatter(cst_number_of_cells, accuracy, color='tab:purple')

plt.xlabel("Количество ячеек сетки")
plt.ylabel("Погрешность, %")
plt.show()
