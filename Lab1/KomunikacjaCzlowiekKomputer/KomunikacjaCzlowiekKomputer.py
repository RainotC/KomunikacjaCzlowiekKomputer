from re import X
import matplotlib.pyplot as plt
import numpy as np


def preparing_arrays(file_name, file_len):
    x_axis = np.empty(file_len)
    y_axis = np.empty(file_len)

    for i in range(file_len): #seperating x axis and y axis values
        one_test = file_name[i]
        results = one_test[2:]
        average_result = np.average(results)

        y_axis[i] = average_result
        x_axis[i] = one_test[1]

    return x_axis, y_axis




file_2cel = np.genfromtxt("2cel.csv", delimiter = ",")
data_2cel = file_2cel[1:]
len_2cel = len(data_2cel)
xaxis_2cel, yaxis_2cel = preparing_arrays(file_2cel, len_2cel)

file_cel = np.genfromtxt("cel.csv", delimiter = ",")
data_cel = file_cel[1:]
len_cel = len(data_cel)
xaxis_cel, yaxis_cel = preparing_arrays(file_cel, len_cel)

file_celrs = np.genfromtxt("cel-rs.csv", delimiter = ",")
data_celrs = file_celrs[1:]
len_celrs = len(data_celrs)
xaxis_celrs, yaxis_celrs = preparing_arrays(file_celrs, len_celrs)

file_2celrs = np.genfromtxt("2cel-rs.csv", delimiter = ",")
data_2celrs = file_2celrs[1:]
len_2celrs = len(data_2celrs)
xaxis_2celrs, yaxis_2celrs = preparing_arrays(file_2celrs, len_2celrs)

file_rsel = np.genfromtxt("rsel.csv", delimiter = ",")
data_rsel = file_rsel[1:]
len_rsel = len(data_rsel)
xaxis_rsel, yaxis_rsel = preparing_arrays(file_rsel, len_rsel)

line_rsel = plt.plot(xaxis_rsel, yaxis_rsel, color="blue", label = '1-Evol-RS')
line_celrs = plt.plot(xaxis_celrs, yaxis_celrs, color="green", label ='1-Coev-RS')
line_2celrs = plt.plot(xaxis_2celrs, yaxis_2celrs, color="red", label = '2-Coev-RS')
line_cel = plt.plot(xaxis_cel, yaxis_cel, color="black", label = '1-Coev')
line_2cel = plt.plot(xaxis_2cel, yaxis_2cel, color="magenta", label = '2-Coev')

plt.xlim([0, 500000])
plt.ylim([0.6, 1])
plt.xlabel("Rozegranych gier")
plt.ylabel("Odsetek wygranych gier")
plt.legend()
plt.show()


