# David S. Li (110328771)
# CSE 390 HW2 Part 1

from math import exp, sqrt

s = ""
vars = s.split('\t')

# vars should have 6 elements, if not, make an exception here

r = vars[0] #
total_t = vars[1] #
n = vars[2] #
sigma = vars[3] # volatility
s_0 = vars[4] # original stock price
k = vars[5] # strike price, abbreviation for S_{0}

t = total_t / n # delta t

# calculate 'u' and 'p'
# u = e^{sigma * sqrt{t}}
u = exp(sigma * sqrt(t))
d = 1 / u

p = (exp(r * t) - d) / (u - d)

# recursive function for branching
def branch(price, dir): # price is float, dir is boolean where true represents up and false represents down
    s_k1 = 0 # Abbreviation for S_{k + 1}
    if dir == True:
        s_k1 = u * s_0
    else: # dir == False
        s_k1 = d * s_0