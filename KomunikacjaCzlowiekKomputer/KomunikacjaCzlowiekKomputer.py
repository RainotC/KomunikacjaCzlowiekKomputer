from re import X
import matplotlib.pyplot as plt
import numpy as np

file = np.genfromtxt("2cel.csv", delimiter = ",")
newfile = file[1:]

x_axis = np.empty(len(newfile))
y_axis = np.empty(len(newfile))



for i in range(len(newfile)):
    one_test = newfile[i]
    results = one_test[2:]
    average_result = np.average(results)

    y_axis[i] = average_result
    x_axis[i] = one_test[1]




