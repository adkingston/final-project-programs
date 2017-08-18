import math
import numpy as np
import matplotlib.pyplot as plt


def quart(dec):
    if dec >= 1:
        return "1"
    else:
        qua = "0."
        while len(qua) <= 10:
            dec *= 4
            c = math.floor(dec)
            dec -= c
            qua += str(int(abs(c)))
        return str(qua)


def eta(qua):
    return qua.count('2', 0, len(qua)-1) % 2

def delta(qua):
    return sum(qua.count(x, 0, len(qua)-1) for x in ['1', '2'] ) % 4

S = np.array([[0, -1], [1, 0]], dtype=float)

s = [np.array([[0], [0]], dtype=float),
     np.array([[2], [0]], dtype=float),
     np.array([[2], [2]], dtype=float),
     np.array([[2], [0]], dtype=float)]


def power_half(qua, i):
    return (-1.0) ** (eta(qua)) / 2.0 ** i


def prods(qua):
    return np.linalg.matrix_power(S, delta(qua))

def k(q):
    if q == 0 or q == 1:
        return 1
    else:
        return -1

def a(q):
    if q == 2:
        return 0
    else:
        return 2

def b(q):
    if q == 0:
        return 0
    else:
        return 2

def h(d, q):
    if d % 2 == 1:
        return a(q)
    else:
        return b(q)


def sierpinski(qua):
    if qua == "1":
        return 2.0
    X = "0."
    qua1 = qua.replace("0.", "")
    sig = 0
    i = 1
    for q in qua1:
        if q == 0:
            i += 1
        else:
            X += q
            sig += power_half(X, i)*k(delta(X))*b(q)
            # sig += power_half(X, i) * np.dot(prods(X), s[int(q)])
            i += 1
    return sig


def sierpinski_graph(iterate, coordinate=2, n=1):
    I = np.arange(0.0, 1.0 + 1e-7, 1.0 / 4.0 ** iterate)
    Iq1 = [quart(i) for i in I]
    if coordinate == 2:
        sfc = [2*sierpinski(q) for q in Iq]
        return plt.plot([x[0] for x in sfc], [y[1] for y in sfc], "b")
    else:
        sfc1 = [float(sierpinski(q)) for q in Iq1]
        plt.plot(I, sfc1, 'k-')
    plt.show()

sierpinski_graph(4, 1)

# fig = plt.figure()
# sierpinski_graph(6, 0)
# fig.savefig("C:\\Users\\Alexander\\OneDrive\\Documents\\School\\University of St. Andrews\\Year 4\\MT4599 Dissertation\\Main Document\\images\\Z_grid.png")
