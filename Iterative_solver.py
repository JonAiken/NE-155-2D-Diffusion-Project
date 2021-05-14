from matplotlib.pyplot import xscale
import numpy as np
import scipy as sci
from scipy import sparse
from scipy import linalg


def sor(A, b, x_0, omega):
    n = len(b)
    n_X = []
    for k in range(0, n):
        sum1 = 0
        sum2 = 0
        for i in range(0, n):
            if (i < k):
                sum1 = sum1 + A[k][i]* n_X[i]
            elif (i > k):
                sum2 = sum2 + A[k][i]* x_0[i]
        xi = (1- omega)* x_0[k] + (omega/(A[k][k]))* (b[k] - sum1 - sum2)
        n_X.append(xi)
    return np.array(n_X)

def iterations(A, b, x_0, tol, omega):
    counter = 0
    error = np.inf
    while error > tol:
        X_new = sor(A, b, x_0, omega)
        error = (np.linalg.norm((X_new - x_0)))    #absolute error
        counter = counter + 1
        x_0 = X_new
    return x_0, error, counter




























# def sor(A, b, x_0, omega):    #As seen in hw6
#     n = len(b)
#     xs = x_0
#     for k in range(0,n):
#         sum1 = 0
#         sum2 = 0
#         for k in range(0,n):
#             for i in range(k):
#                 sum1 = sum1 + A[k,i]*xs[i,k]
#             for i in range(k+1, n):
#                 sum2 = sum2 + A[k,i] * xs[i,k-1]
#             xs = (1-omega)*xs[k,k] + (omega/A[k,k])*(b[k] - sum1 - sum2)
#     return xs

#convergence checker, using abs error.



# def SOR(A, b, x_0, omega, K):     

    # Define the size of our system
    # n = len(x_0)
    # ref = linalg.solve(A,b)
    
    # We've got an initial guess, x_0, and an iteration count to hit, K
    # To track progress through the iterations, we'll store all of our
    # estimates. You wouldn't typically do this, but we will for illustration.
    # x = np.zeros((K+1, n))
    # x[0] = x_0
    # We'd also like to track our error (since we know the real solution)
    # error = np.zeros((K+1, n))
    # error[0] = np.abs(ref - x[0])
    
    # for k in range(0,K):

        # for k in range(0, n):
# 
            # Initialize the summation terms to zero on each iteration
            # sum_1 = 0.0
            # sum_2 = 0.0

            # the k+1 term from 0 to k-1 
            # for i in range(k):

                # sum_1 = sum_1 + A[k][i] * x[k+1][i]

            # the k term from k+1 to n-1
            # for i in range(k+1, n):

                # sum_2 = sum_2 + A[k][i] * x[k][i]

            # x[k+1][k] = (1 - omega) * x[k][k] + omega/A[k][k] * (b[k] - sum_1 - sum_2)
            
        # compute the error
        # error[k+1] = np.abs(ref - x[k+1])

    # return x, error, k






