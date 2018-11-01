# David S. Li (110328771)
# CSE 390 HW2 Part 1

from math import exp, sqrt

s = ""
vars = s.split('\t')

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
        self.root = BinaryTreeNode(0)

class BinaryTreeNode():
    def  __init__(self, time):
        self.left = None
        self.right = None
        self.parent = None # FIX LATER
        self.stock_price = s_0 * exp(r * time)
        f_u = self.parent.stock_price * u
        f_d = self.parent.stock_price * d
        self.f = exp(-r * t) * (p * f_u + (1 - p) * f_d)# Fix 't', if it is supposed to represent the TOTAL time

