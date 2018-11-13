# David S. Li (110328771)
# CSE 390 HW2 Part 1

from math import exp, sqrt
import time

# Data structure for Binary Tree and Binary Tree Node
class BinaryTree():
    def __init__(self, r, n, s_0, k, p):
        self.root = BinaryTreeNode(0, None, 0, r, t, k, p, s_0)

    def tree_debug(self):
        self.root.node_debug()

class BinaryTreeNode(): # time_period ranges from 0 to n, and is basically the level/ of the tree
    def  __init__(self, time_period, parent, dir, r, t, k, p, stock_price_sum): # factor in direction from old branch method when creating new nodes?  Pass in parent as a reference?
        self.parent = parent
        self.time_period = time_period
        self.stock_price_sum = stock_price_sum

        # Determining Stock Price
        if dir < 0 and self.parent is not None:
            self.stock_price = self.parent.stock_price * d
        elif dir > 0 and self.parent is not None:
            self.stock_price = self.parent.stock_price * u
        else:
            self.stock_price = s_0

        # print(time_period, ' ', stock_price_sum)

        #if self.parent is not None:
        #    print('parent stock price is ', self.parent.stock_price)
        # print('stock price is ', self.stock_price)

        # debug: what time period we are at
        # print('time period is ', time_period)

        # Assigning left, right, and option price 'f' depending on whether we are at a leaf or not
        if self.time_period < n: # Branch and create two children
            # print('Down Node')
            self.left = BinaryTreeNode(self.time_period + 1, self, -1, r, t, k, p, self.stock_price_sum + self.stock_price * d) # down
            # print('Up Node')
            self.right = BinaryTreeNode(self.time_period + 1, self, 1, r, t, k, p, self.stock_price_sum + self.stock_price * u) # up
            self.f = exp(-r * t) * (p * self.left.f + (1 - p) * self.right.f) # Fix 't', if it is supposed to represent the TOTAL time
        else: # LEAF NODE CASE
            self.left = None
            self.right = None
            # FIX THIS FOR ASIAN CALL OPTION
            running_avg_price = self.stock_price_sum / (self.time_period + 1)
            # print(stock_price_sum, ' ', time_period + 1, ' ', stock_price_sum / (time_period + 1))
            self.f = running_avg_price - k
            if self.f < 0:
                self.f = 0
            # print('option price: ', self.f)

            # if k - self.stock_price > self.f:
                # self.f = k - self.stock_price

    def node_debug(self):
        print('Node details: ', self.time_period, self.stock_price, self.f, self.stock_price_sum / (self.time_period + 1), self.stock_price_sum)
        if self.left is not None:
            print('Left/Down')
            self.left.node_debug()
        if self.right is not None:
            print('Right/Up')
            self.right.node_debug()


        # option price = stock price - strike price
        #self.f = exp(-r * t) * (p * f_u + (1 - p) * f_d) # Fix 't', if it is supposed to represent the TOTAL time

# "MAIN" Program

start = time.time()
filename = input('Enter filename: ')
file = open(filename, "r")
fileText = file.read()
lines = fileText.split('\n')

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


    p = (exp(r * t) - d) / (u - d)


    binom_tree = BinaryTree(r, n, s_0, k, p)
    print(binom_tree.root.f)
    print('\n')
    # binom_tree.tree_debug()

end = time.time()
print('Total run time:', end - start, 'ms')
