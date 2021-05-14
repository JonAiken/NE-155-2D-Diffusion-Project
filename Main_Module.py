from Diffusion_solver import *
from Input_Module import *
from Iterative_solver import *
import numpy as np
from datetime import datetime

###Get inputs from input module:
n, m, sigma_value, Source_value, D_value, delta, epsilon, tol, omega = input(1)

## Form source, absorption and diffusion matricies.
sigma_a = split_matrix(n, m, 2, sigma_value)
Source = point_matrix(n, m, Source_value)
D = split_matrix(n, m, 2, D_value)
print(graph_func(D, 'Greens', 'Diffusion Coefficients', figSize= (6, 6)))

#Form avg sigma_a and source matrix w/ boundary conditions
avg_sigma_a = avg_matrix(sigma_a, delta, epsilon, n, m)
avg_source = avg_matrix(Source, delta, epsilon, n, m)
print(graph_func(avg_sigma_a, 'Blues', 'Averaged Absorption Cross Section', figSize= (6, 6)))

#BC applied to source for Vacuum boundaries.
# avg_source[:,0], avg_source[0,:] = 0, 0
avg_source[0,:] = 0
avg_source[:,0] = 0
print(graph_func(avg_source, 'Reds', 'Source', figSize= (6, 6)))

#Reshape source into vector.
source_vector = create_source(avg_source, n, m)


#Form A
A_matrix = combined_A_matrix(n)


#iteratively Solve using SOR
x_0 = np.zeros(n*n)
x_0, error, counter = iterations(A_matrix, source_vector, x_0, tol, omega)


# print(xs)
flux = x_0.reshape(n,m)
# print(f'flux: {flux}')
print(f'error: {error}')
print(f'iterations: {counter}')
# print (flux, error, counter)
flux[:,0] = 0
print(graph_func(flux, 'Oranges', 'Flux', figSize= (6, 6)))



print( """
NE 155 2D Diffusion Solver
Jonathan Aiken
Spring 2021""")



# x_0 = np.zeros((n,n))

# print(f'A_matrix: {A_matrix}')
# print(f'source_vector: {source_vector}')
# print(f'x_0: {x_0}')
# print(f'tol: {tol}')
# print(f'omega: {omega}')
# x, error, k = SOR(A_matrix, source_vector, x_0, omega, 25)
# print(x, error, k)
