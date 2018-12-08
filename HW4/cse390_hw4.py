import pandas as p
import statsmodels.tsa.stattools as sm
import statsmodels.graphics.tsaplots as s
import matplotlib.pyplot as plt
import numpy as np

def calc_acf(data, lag):
    # data segments, separared by lag
    data_seg_1 = data[:lag]
    data_seg_2 = data[lag:]
    acf = sm.acf(data, unbiased=True, nlags=lag)
    return acf

def calc_pacf(data, lag):
    data_seg_1 = data[:lag]
    data_seg_2 = data[lag:]
    pacf = sm.pacf(data, nlags=lag)
    return pacf

data = p.read_csv('bond-returns.csv', sep = "|")

#print(data) # MUST GIVE COLUMN HEADERS in CSV FILE BEFORE WE DO THIS
five_year_data = data[["5Y"]]
print(five_year_data)
acf = calc_acf(five_year_data, 10)
acf_plt = s.plot_acf(acf)
# plt.show()
pacf = calc_pacf(data, 10)
pacf_plt = s.plot_pacf(pacf)
plt.show()