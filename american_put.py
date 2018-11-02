# David S. Li (110328771)
# CSE 390 HW2 Part 1

from math import exp, sqrt

filename = "hello.txt"
file = open(filename, "r")
lines = []
for line in file:
    lines.append(line)

for line in lines:
    vars = line.split('\t')

    # vars should have 6 elements, if not, make an exception here
    if len(vars) != 6:
        raise SystemExit # maybe declare your own exception here?

    r = float(vars[0]) #
    total_t = float(vars[1]) #
    n = float(vars[2]) #
    sigma = float(vars[3]) # volatility
    s_0 = float(vars[4]) # original stock price
    k = float(vars[5]) # strike price, abbreviation for S_{0}

    t = total_t / n # delta t

    # calculate 'u' and 'p'
    # u = e^{sigma * sqrt{t}}
    u = exp(sigma * sqrt(t))
    d = 1 / u

    p = (exp(r * t) - d) / (u - d)

# recursive function for branching
def branch(price, dir): # price is float, dir is boolean where true represents up and false represents down
    s_k1 = 0 # Abbreviation for S_{k + 1}
    if dir is True:
        s_k1 = u * s_0
    else: # dir == False
        s_k1 = d * s_0

# Data structure for Binary Tree and Binary Tree Node
class BinaryTree():
    def __init__(self, n):
        self.root = BinaryTreeNode(0, None, 0)

class BinaryTreeNode():
    def  __init__(self, time, parent, dir): # factor in direction from old branch method when creating new nodes?  Pass in parent as a reference?
        # Determining Stock Price
        if dir < 0:
            self.stock_price = self.parent.stock_price * d
        elif dir > 0:
            self.stock_price = self.parent.stock_price * u
        else:
            self.stock_price = s_0

        #
        if time < n: # Branch and create two children
            self.left = BinaryTreeNode(time + t, self, -1)
            self.right = BinaryTreeNode(time + t, self, 1)
            self.f = exp(-r * t) * (p * self.left.f + (1 - p) * self.right.f) # Fix 't', if it is supposed to represent the TOTAL time
        else: # LEAF NODE CASE
            self.left = None
            self.right = None
            self.f = self.stock_price - k

        self.parent = parent

        # option price = stock price - strike price
        #self.f = exp(-r * t) * (p * f_u + (1 - p) * f_d) # Fix 't', if it is supposed to represent the TOTAL time