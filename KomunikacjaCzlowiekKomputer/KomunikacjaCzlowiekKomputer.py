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


plt.plot(xaxis_2cel, yaxis_2cel, color="red")
plt.xlabel("Rozegranych gier")
plt.ylabel("Odsetek wygranych gier")

plt.show()


