import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from scipy import linalg

def input(T):
    if T == 1:
        n = 30
        m = 30
        sigma_value = 200
        Source_value = 60
        D_value = 20
        delta = np.ones(n-1)
        epsilon = np.ones(n-1)
        tol = 10 ** (-6)
        omega = 1.15
        #x_0 = np.zeros((n,n))
        return n, m, sigma_value, Source_value, D_value, delta, epsilon, tol, omega


def split_matrix(n, m, scale, D):
   # split_border = int(n / splits)
    split_border = int(n / 2)
    s_matrix = np.ones((n-1,m-1)) * D
    s_matrix[:, :split_border] = s_matrix[:, :split_border]*scale
    return s_matrix


def point_matrix(n, m, S):
    p_matrix = np.ones((n-1, m-1))
    p_matrix[int((n-1)/2), int((m-1)/2)] = S
    return p_matrix

def uniform_matrix(n,m,D):
    u_matrix = np.zeros((n,m))
    for x in range(0, n):
        for y in range(0,m):
            u_matrix[x][y] = D
    return u_matrix

def create_source(S,n,m):  #source needs to be reshaped and factor in B
    n, m = S.shape
    S_reshaped = S.reshape((n*m), 1)
    return S_reshaped

def avg_matrix(matrix, delta, epsilon, n, m):
    x, y = matrix.shape
    new_matrix = np.zeros((n, m))
    
    #corner cases, only 1 point
    new_matrix[0][0] = (1/4)*(matrix[0][0]*epsilon[0]*delta[0])
    new_matrix[0][y] = (1/4)*(matrix[0][y-1]*epsilon[0]*delta[y-1])
    new_matrix[x][0] = (1/4)*(matrix[x-1][0]*epsilon[x-1]*delta[0])
    new_matrix[x][y] = (1/4)*(matrix[x-1][y-1]*epsilon[x-1]*delta[y-1])   
    
    #edges (right & left). Half of center shown above, 2 less points

    for i in range(1 ,x):
        new_matrix[i][0] = (1/4)*((matrix[i][0]*epsilon[i]*delta[0]) + (matrix[i-1][0]*epsilon[i-1]*delta[0]))
        new_matrix[i][y] = (1/4)*((matrix[i][y-1]*epsilon[i]*delta[y-1]) + (matrix[i-1][y-1]*epsilon[i-1]*delta[y-1]))
        
    
    for j in range(1,y):
        new_matrix[0][j] = (1/4)*((matrix[0][j]*epsilon[0]*delta[j]) + (matrix[0][j-1]*epsilon[0]*delta[j-1]))
        new_matrix[x][j] = (1/4)*((matrix[x-1][j]*epsilon[x-1]*delta[j]) + (matrix[x-1][j-1]*epsilon[0]*delta[j-1]))
    
    #Normal Center Cases: Using bottom right, bottom left, top right & top left 
    for i in range (1,(x)):
        for j in range (1, (y)):
            new_matrix[i][j] = (1/4)*((matrix[i][j]*epsilon[i]*delta[j]) + 
            (matrix[i][j-1]*epsilon[i]*delta[j-1]) + (matrix[i-1][j]*epsilon[i-1]*delta[j]) + (matrix[i-1][j-1]*epsilon[i-1]*delta[j-1]))
     
    return new_matrix

def graph_func(input_matrix, color, title, figSize= (6, 6)):
    plt.imshow(X = input_matrix, cmap=color, interpolation='none', origin = 'lower')
    plt.xticks(np.linspace(0, input_matrix.shape[0]-1, input_matrix.shape[0]))
    plt.yticks(np.linspace(0, input_matrix.shape[1]-1, input_matrix.shape[1]))
    plt.xlim([0, input_matrix.shape[0]-1])
    plt.ylim([0, input_matrix.shape[1]-1])
    plt.title(title, fontsize = 11)
    plt.colorbar()
    plt.show()    


