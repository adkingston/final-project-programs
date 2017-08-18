import numpy as np
import math
import matplotlib.pyplot as plt

""" This will be a program to graph the Polya space-filling curve; a
generalisation of the Sierpinski space-filling
curve. """


def binary(dec):
    if dec >= 1:
        return "1"
    else:
        bi = "0."
        while len(bi) <= 17:
            dec *= 2
            c = math.floor(dec)
            dec -= c
            bi += str(int(abs(c)))
        return str(bi)


def p_array(theta):
    P = [np.array([[np.cos(theta), np.sin(theta)],
                   [np.sin(theta), -np.cos(theta)]], dtype=float),
         np.array([[np.sin(theta), -np.cos(theta)],
                   [-np.cos(theta), -np.sin(theta)]], dtype=float)]
    return P


def p_list(theta):
    p = [np.array([[0], [0]], dtype=float),
         np.array([[2.0 * np.cos(theta)], [2.0 * np.sin(theta)]], dtype=float)]
    return p


def l(bi, k):
    count = 0
    bi1 = bi.replace("0.", "")
    for element in xrange(len(bi1) - 1):
        if k == int(bi1[element]):
            count += 1
    return count


def prod_p(bi, theta):
    prod = np.identity(2)
    P = p_array(theta)
    bi1 = bi.replace("0.", "")
    for element in xrange(len(bi1) - 1):
        prod = np.dot(prod, P[int(bi1[element])])
    return prod


def polya(bi, theta):
    if bi == "1":
        return np.array([[2], [0]], dtype=float)
    else:
        p = p_list(theta)
        sigma = 0
        bi1 = bi.replace("0.", "")
        X = "0."
        for element in bi1:
            X += element
            sigma += np.cos(theta) ** (l(X, 0) + 1) * np.sin(theta)**(l(X, 1))\
                    * np.dot(prod_p(X, theta), p[int(element)])
    return sigma


n = 10
I = np.arange(0.0, 1.000001, 1.0/2.0**n)
Ib = [binary(i) for i in I]
t = np.deg2rad(90-35)
Q = [polya(i, t) for i in Ib]
# plt.ylim([0, 2])
Px = [Q[i][0] for i in xrange(len(Q))]
Py = [Q[i][1] for i in xrange(len(Q))]

plt.show(plt.plot(I, Py))

#
# def hausdorff_dim_est(a):
#     lower_bound = 1 - a*math.log(a, 4) - (1-a)*math.log((1-a), 4)
#     upper_bound = 1 + math.log((math.sqrt(a)+math.sqrt(1-a)), 2)
#     return [lower_bound, upper_bound]
