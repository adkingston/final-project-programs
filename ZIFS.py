import numpy as np
import matplotlib.pyplot as plt
import pylab as pyl


D, R = np.arange(0.0, 1.0+1e-7, 0.1), np.arange(0.0, 2.0+1.e-7, 0.11)
A = [[a, b] for a in D for b in R]


def z1(s):
    return [[0.25*x[0], 0.5*x[1]] for x in s]


def z2(s):
    return [[-0.25*x[0]+0.5, -0.5*x[1]+2] for x in s]


def z3(s):
    return [[-0.25*x[0] + 0.75, 0.5*x[1] + 1] for x in s]


def z4(s):
    return [[0.25*x[0] + 0.75, 0.5*x[1] + 1] for x in s]


def iterations(ifs, seed, steps):
    assert isinstance(ifs, list)
    if steps < 1:
        return seed
    else:
        next_step = []
        for func in ifs:
            next_step += func(seed)
        next_step = iterations(ifs, next_step, steps-1)
    return next_step

a = [[2., 3.]]

A1 = iterations([z1, z2, z3, z4], a, 7)

X1 = [z[0] for z in A1]
Y1 = [z[1] for z in A1]

# # # fig = plt.figure()
plt.plot(X1, Y1, 'bo', markersize=1, markeredgewidth=0.1)
pyl.show()
# fig.savefig("C:\\Users\\Alexander\\OneDrive\\Documents\\School
#                \\University of St. Andrews\\Year 4\\MT4599
#                 Dissertation\\Main Document\\images\\A6.png")


# def hausdorff_dist(A, B):
#     dists = []
#     temp = []
#     for a in A:
#         for b in B:
#             d = math.sqrt(abs(a[0] - b[0])**2 + abs(a[1] - b[1])**2)
#             temp.append(d)
#         dists.append(min(temp))
#         temp = []
#     return max(dists)
