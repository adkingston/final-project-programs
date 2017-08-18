import math
from numpy import *
from matplotlib.pyplot import *

def quart(dec):
    if dec >= 1:
        return 1
    else:
        quar = "0."
        while len(quar) <= 10:
            dec *= 4
            c = math.floor(dec)
            dec -= c
            quar += str(int(abs(c)))
        return str(quar)

def sgn(n):
    if n == 0:
        return 0
    else:
        return 1

def eta(quar, k):
    eta = 0
    quar1 = quar.replace("0.", "")
    for i in range(len(quar1)-1):
        if quar1[i] == k:
            eta += 1
    return eta % 2

H = array([[0, 1], [1, 0]])
h = [array([[0], [0]]), array([[0], [1]]), array([[1], [1]]), array([[2], [1]])]


def hilbert(quar):
    if quar == "1":
        return array([[1],[0]])
    X = "0."
    quar1 = quar.replace("0.", "")
    sig = zeros((2,1))
    i = 1
    for q in quar1:
        X += q
        if q == "0":
            pass
        else:
            H1 = linalg.matrix_power(H, eta(X, "0"))
            H2 = linalg.matrix_power(-1*H, eta(X, "3"))
            sig += (1.0/2.0**i)*dot(dot(H1, H2),h[int(q)])
        i += 1
    return sig

n = 7
I = arange(0.0, 1.0001, 1.0/4.0**n)
Iq = [quart(i) for i in I]

Hx = [hilbert(str(q))[0][0] for q in Iq]
Hy = [hilbert(str(q))[1][0] for q in Iq]

# hil = zip(I, Hy)
# fig = figure()
# ax = fig.add_subplot(111)
# ax.set_title("Hilbert Y_{}".format(n))

# ylim([0, 2])
# currentAxis = gca()
# for i in range(0,len(hil)-2, 2):
#     currentAxis.add_patch(Rectangle((hil[i][0], hil[i][1]),
#                                      hil[i+1][0] - hil[i][0],
#                                      hil[i+1][1] - hil[i][1]))
show(plot(I, Hx))
