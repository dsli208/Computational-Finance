# David S. Li (110328771)
# CSE 390 HW2 Part 2

from math import exp, sqrt

filename = "sample"
file = open(filename, "r")
fileText = file.read()
lines = fileText.split('\n')

# for line in file:
    # lines.append(line)

for line in lines:
    vars = line.split('\\t')
    print(vars)

    # vars should have 6 elements, if not, make an exception here
    if len(vars) != 6:
        print("EXCEPTION")
        raise SystemExit # maybe declare your own exception here?

    r = float(vars[0]) # risk free rate
    total_t = float(vars[1]) # T in years
    n = float(vars[2]) # number of equal time periods/steps
    sigma = float(vars[3]) # volatility
    s_0 = float(vars[4]) # original stock price
    k = float(vars[5]) # strike price, abbreviation for S_{0}

    t = total_t / n # delta t

    # calculate 'u' and 'p'
    # u = e^{sigma * sqrt{t}}
    u = exp(sigma * sqrt(t))
    d = 1 / u

    p = (exp(r * t) - d) / (u - d)