from numpy import *
import math
from matplotlib.pyplot import *
from matplotlib.patches import *

def ternary(dec):
    """ The Peano curve takes inputs and returns outputs in ternary form. We want to use inputs in base ten. Hence, we need two functions: one to convert a decimal into a ternary, and a second inverse function """
    if dec >= 1:
        return 1
    else:
        ter = "0."
        while len(ter) <= 17:
            dec *= 3
            c = math.floor(dec)
            dec -= c
            ter += str(int(c))
        return str(ter)

def K(n, t):
    if n % 2 == 0:
        return t
    else:
        return 2 - t

def Px(ter):
    if float(ter) == 1:
        return "1"
    else:
        ter1 = ter + "00000000000"
        X = "0." + str(ter1[2])
        n = 0
        # Get x:
        for i in range(3, len(ter1)-1):
            if i % 2 != 0:
                n += int(ter1[i])
                X += str(K(n, int(ter1[i+1])))
        return X

def Py(ter):
    if float(ter) == 1:
        return "1"
    else:
        ter1 = str(ter) + "00000000000"
        Y = "0."
        n = 0
        for i in range(2, len(ter1)-1):
            if i % 2 == 0:
                n += int(ter1[i])
                Y += str(K(n, int(ter1[i+1])))
        return Y

def decimal(ter):
    if float(ter) >= 1:
        return 1
    else:
        ter1 = ter.replace("0.", "")
        dec = 0
        for i in range(len(ter1)):
            dec += int(ter1[i])*(1.0/(3.0**(i+1)))
        return float(dec)

for n in range(1,5):
    I = arange(0.0, 1.0+0.001, 1.0/(9.0**n))
    It = [ternary(i) for i in I]
    pxt = [decimal(Px(t)) for t in It]
    pyt = [decimal(Py(t)) for t in It]
    P = list(zip(I, pxt))

    fig = figure()
    ax = fig.add_subplot(111)
    ax.set_title("X_{}".format(n))
    currentAxis = gca()
    for i in range(len(P)-1):
        currentAxis.add_patch(Rectangle((P[i][0], P[i][1]), P[i+1][0] - P[i][0],
                                         P[i+1][1] - P[i][1]))
    savefig("px{}".format(n))
