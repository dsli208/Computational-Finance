import pandas as p
import statsmodels.tsa.stattools as sm
import statsmodels.graphics.tsaplots as s
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.multiarray import ndarray

def mean(list):
    return sum(list) / len(list)

def covar(list1, list2):
    mean_1 = mean(list1)
    mean_2 = mean(list2)
    sum_1 = 0
    sum_2 = 0
    for i in list1:
        sum_1  = sum_1 + (i - mean_1)

    for i in list2:
        sum_2 = sum_2 + (i - mean_2)

    return 0

def calc_acf(data):
    # data segments, separared by lag
    #df = p.DataFrame(index=index, columns=columns)
    data_seg1 = data.loc[:, ["5Y"]]
    print("Seg 1")
    print(data_seg1)
    acf = []
    variance = data_seg1.var()
    for i in range(1, 11):
        print("Seg 2")
        data_seg2 = data.loc[i + 1:, ["5Y"]]
        print(data_seg2)
        series_1 = p.Series(data_seg1["5Y"])
        series_2 = p.Series(data_seg2["5Y"])
        cov_i = series_1.cov(series_2)
        acf.append(cov_i)

    return acf

def calc_pacf(data, lag):
    data_seg_1 = data[:lag]
    # data_seg1 = data.loc[:, ["5Y"]]
    data_seg_2 = data[lag:]
    # data_seg2 = data.loc[i:, ["5Y"]]
    pacf = sm.pacf(data, nlags=lag, method='ywunbiased')
    return pacf

data = p.read_csv('bond-returns.csv', sep = "|")

#print(data) # MUST GIVE COLUMN HEADERS in CSV FILE BEFORE WE DO THIS
five_year_data = data[["5Y"]]
print(five_year_data) # how do we get this to work as a 1D array?
#five_year_data_1d = p.Series.ravel(five_year_data)
#print(five_year_data_1d)
acf = calc_acf(five_year_data)
print("ACF is", acf)
plt.xlim(1, 10)
acf_plt = s.plot_acf(acf)
# plt.show()
pacf = calc_pacf(five_year_data, 10)
pacf_plt = s.plot_pacf(pacf)
plt.show()