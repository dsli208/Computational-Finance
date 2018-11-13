# David S. Li (110328771)
# CSE 390 HW2 Part 1

from math import exp, sqrt
import time

# Data structure for Binary Tree and Binary Tree Node
class BinaryTree():
    def __init__(self, r, n, s_0, k, p):
        self.root = BinaryTreeNode(0, None, 0, r, t, k, p)

    def tree_debug(self):
        self.root.node_debug()

class BinaryTreeNode(): # time_period ranges from 0 to n, and is basically the level/ of the tree
    def  __init__(self, time_period, parent, dir, r, t, k, p): # factor in direction from old branch method when creating new nodes?  Pass in parent as a reference?
        self.parent = parent
        self.time_period = time_period

        # Determining Stock Price
        if dir < 0 and self.parent is not None: # LEFT/DOWN
            self.stock_price = self.parent.stock_price * d
        elif dir > 0 and self.parent is not None: # RIGHT/UP
            self.stock_price = self.parent.stock_price * u
        else:
            self.stock_price = s_0

        # if self.parent is not None:
           # print('parent stock price is ', self.parent.stock_price)
        # print('stock price is ', self.stock_price)

        # debug: what time period we are at
        # print('time period is ', time_period)

        # Assigning left, right, and option price 'f' depending on whether we are at a leaf or not
        if time_period < n: # Branch and create two children
            # print('Down Node')
            self.left = BinaryTreeNode(time_period + 1, self, -1, r, t, k, p) # down
            # print('Up Node')
            self.right = BinaryTreeNode(time_period + 1, self, 1, r, t, k, p) # up
            self.f = exp(-r * t) * (((1 - p) * self.left.f) + ((p) * self.right.f)) # Fix 't', if it is supposed to represent the TOTAL time
            # print('option price at non-leaf node:', self.f)
        else: # LEAF NODE CASE
            self.left = None
            self.right = None
            self.f = k - self.stock_price
            if (self.f < 0):
                self.f = 0
            # print('option price at leaf is ', self.f)

        if k - self.stock_price > self.f:
            self.f = k - self.stock_price


        # option price = stock price - strike price
        #self.f = exp(-r * t) * (p * f_u + (1 - p) * f_d) # Fix 't', if it is supposed to represent the TOTAL time

    def node_debug(self):
        print('Node details: ', self.time_period, self.stock_price, self.f)
        if self.left is not None:
            print('Left/Down')
            self.left.node_debug()
        if self.right is not None:
            print('Right/Up')
            self.right.node_debug()



start = time.time()
filename = input('Enter filename: ')
file = open(filename, "r")
fileText = file.read()
lines = fileText.split('\n')

for line in file:
    lines.append(line)

for line in lines:
    vars = line.split('\t')
    # print(vars)

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

    # calculate 'u' and 'd'}
    u = exp(sigma * sqrt(t))
    d = 1 / u

    # debug for u and d
    print("u is ", u, "and d is ", d)

    p = (exp(r * t) - d) / (u - d)

    # debug for p
    print('p is', p)

    binom_tree = BinaryTree(r, n, s_0, k, p)
    print(binom_tree.root.f)
    print('\n')

    # binom_tree.tree_debug()

end = time.time()
print('Total run time:', end - start, 'ms')

# recursive function for branching
#def branch(price, dir): # price is float, dir is boolean where true represents up and false represents down
#    s_k1 = 0 # Abbreviation for S_{k + 1}
#    if dir is True:
#        s_k1 = u * s_0
#    else: # dir == False
#        s_k1 = d * s_0
