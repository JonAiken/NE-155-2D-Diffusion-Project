# NE-155-2D-Diffusion-Project
NE 155 final coding project. Creating a 2D diffusion solver.
This was made by an undergrad student doing his best, so don't use this if you want accurate and reliable results.
The goal of this project is to write a 2D diffusion solver with vacuum boundaries
on the left and bottom faces with reflecting boundaries on the top and right faces.

This 2D diffusion solver takes physical constants for diffusion coeficient, absorption cross section and a source term.
This then creates matricies from these contants, which are then averaged. Once boundary conditions have been applied this solver creates a matrix that is 5-banded and solved using the SOR method.

This code has issues with the BC and correctly displaying the flux.

Main Module: calls subroutines listed in specic sequence, prints execution time, and
terminates execution
 Version data subroutine: write code name, version number, author name(s), date and
time of execution to an output file (perhaps also print to screen).
 Input data subroutine: read and/or process the input data. Check all input values
for correctness/sensibility, e.g., all values are positive, array dimensions are correct,
etc. Print an error message and terminate if one or more errors occur, otherwise print
notification of successful input checking.
 Input echo subroutine: print the input data for each cell to the output file (this is good
for reproducibility). Please format this in some useful way.
 Diffusion solver subroutine: implement the discretized diffusion solver here. While
building the surrounding structure you can just have this print \will solve DE here".
