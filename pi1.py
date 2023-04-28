import numpy as np 


def pi1(x, i, J): 
    if i == 1: 
        m = k = 0
    else: 
        IMat = np.zeros([J+1, 2**J])
        IMask = np.zeros([J+1, 2**J])

        ind_s = 1 

        for ind_j in range(J+1): 
            for ind_i in range(2**ind_j):
                ind_s +=1 
                IMask[ind_j, ind_i] = ind_s
                IMat[ind_j, ind_i] = ind_i + ind_j+1

        m, k = np.where(IMask == i) 
        m = 2**m 

    #y = np.zeros([1, len(x)])
    y = np.zeros((len(x), ))

    if i == 1: 
        for i in range(len(x)): 
            if 0 <= x[i] < 1: 
                y[i] = x[i]
                #y[0, i] = x[i]
            else: 
                y[i] = 0
                #y[0, i] = 0 

    else: 
        alpha = k/m
        beta  = (k+0.5)/m 
        gamma = (k+1)/m

        for i in range(len(x)): 
            if alpha <= x[i] < beta: 
                #y[0, i] = x[i] - alpha 
                y[i] = x[i] - alpha
            elif beta <= x[i] < gamma: 
                y[i] = gamma - x[i]
                #y[0, i] = gamma - x[i]
            else: 
                y[i] = 0
                #y[0, i] = 0 

    return y
