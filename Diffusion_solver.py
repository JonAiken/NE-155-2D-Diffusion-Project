import numpy as np
import scipy as sc
from scipy import linalg
from Input_Module import *



#Discretized equations. Forming A
#Capturing influence of left, right, lower, upper and center flux on center of cell.

n, m, sigma_value, Source_value, D_value, delta, epsilon, tol, omega = input(1)

sigma_a = split_matrix(n, m, 2, sigma_value)
avg_sigma_a = avg_matrix(sigma_a, delta, epsilon, n, m)
D = split_matrix(n, m, 2, D_value)


def a_L(i,j):
    if i ==0 or j ==0:   #left or bot vacuum BC
        return 0
    if j == (m - 1) :
        return -(D[j-1][i-1]*epsilon[j-1])/(2*delta[i-1])
    
    return -(D[j-1][i-1]*epsilon[j-1]+D[j][i-1]*epsilon[j]) /(2*delta[i-1])


def a_R(i,j):
    if i == 0 or j == 0 or i == n - 1:
        return 0
    if j == (m - 1):
        return -(D[j-1][i]*epsilon[j-1])/(2*delta[i])
    
    return -(D[j-1][i]*epsilon[j-1] + D[j][i]*epsilon[j])/(2*delta[i])

def a_B(i,j):
    if i ==0 or j ==0:   #left or bot vacuum BC
        return 0
    if i == (n - 1) :
        return -(D[j-1][i-1]*delta[i-1])/(2*epsilon[j-1])
    
    return -(D[j-1][i-1]*delta[i-1] + D[j-1][i]*delta[i])/(2*epsilon[j-1])

def a_T(i,j):
    if i ==0 or j == 0 or j == (m-1):
        return 0
    if  i == (n - 1):
        return (D[j][i-1]*delta[i-1])/(2*epsilon[j])
    return -(D[j][i-1]*delta[i-1] + D[j][i]*delta[i])/(2*epsilon[j])

def a_C(i,j):
    if i ==0 or j == 0:
        return 1
    
    return avg_sigma_a[i][j] - (a_L(i,j) + a_R(i, j) + a_B(i, j) + a_T(i, j))




def center_diagonal(n,i):    #n x n submatrix. Center diagonal is a_c, diagonal above is a_R, diagonal below is a_C
    A_matrix = np.zeros((n,n))
    for x in range(0,n):
        for y in range(0,n):
            if x == y:
                A_matrix[x][y] = a_C(y,i) 
            if x==y and x!= n-1:
                A_matrix[x][y+1] = a_R(y+1,i)
                A_matrix[x+1][y] = a_L(y,i) 
    return A_matrix

def top_diagonal(n,i):  #Use diag func?
    A_matrix = np.zeros((n,n))
    for x in range (0,n):
        for y in range(0,n):
            if x == y:
                A_matrix[x][y] = a_T(y,i)
    return A_matrix

def bottom_diagonal(n,i):
    A_matrix = np.zeros((n,n))
    for x in range (0,n):
        for y in range(0,n):
            if x == y:
                A_matrix[x][y] = a_B(y,i)
    return A_matrix


def combined_A_matrix(n): 
    final_A_matrix = np.zeros((n**2, n**2))
    for i in range(0,n):
        final_A_matrix[ i*n : n+(i*n) , i*n : n+(i*n)] = center_diagonal(n,i)
    for i in range (0,n-1):
        final_A_matrix[i*n: n+ (i * n), n + (i*n) : (2*n) +(i*n)] = top_diagonal(n,i)
        final_A_matrix[ n+(i*n) : (2*n) + (i*n) , i*n : n+ (i * n) ] = bottom_diagonal(n,i)
    return final_A_matrix



    
