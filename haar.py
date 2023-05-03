import numpy as np


def haar(x, i, J):
    if i == 1:
        m = k = 0
    else:
        IMat = np.zeros([J+1, 2**J])
        IMask = np.zeros([J+1, 2**J])

        ind_s = 1
        for ind_j in range(J+1):
            for ind_i in range(2**ind_j):
                ind_s += 1
                IMask[ind_j, ind_i] = ind_s
                IMat[ind_j, ind_i] = ind_i+ind_j+1

        ind_j, ind_i = np.where(IMask == i)
        m = 2**ind_j
        k = ind_i

    
    #y = np.zeros([1, len(x)])
    y = np.zeros((len(x), ))
    

    # TODO: vectorize setting these 
    if i == 1:
        for j in range(len(x)):
            if 0 <= x[j] < 1:
                y[j] = 1
                #y[j, 0] = 1
                #y[0, j] = 1
            else:
                y[j] = 0
                #y[j, 0] = 0
                #y[0, j] = 0
    else:
        alpha = k / m
        beta = (k + 0.5) / m
        gamma = (k + 1) / m

        for j in range(len(x)):
            if alpha <= x[j] < beta:
                y[j] = 1
                #y[j, 0] = 1
                #y[0, j] = 1
            elif beta <= x[j] < gamma:
                y[j] = -1
                #y[j, 0] = -1
                #y[0, j] = -1
            else:
                y[j] = 0
                #y[j, 0] = 0
                #y[0, j] = 0

    return y #, m, k

# TODO: pytests 

"""
haar([0.5], 1, 3) # + 
(array([[1.]]), 0, 0)

haar([0.99], 2, 6) # + 
a: [0.]

b: [0.5]

g: [1.]

(array([[-1.]]), array([1]), array([0]))

haar([0.1, 0.25, 0.5, 0.75, 0.9], 6, 4)

a: [array([0.25])]

b: [array([0.375])]

g: [array([0.5])]

(array([[0., 1., 0., 0., 0.]]), array([4]), array([1]))
"""