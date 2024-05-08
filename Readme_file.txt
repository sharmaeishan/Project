Factorial Calculation Program:
This program calculates factorial values using different implementations and compares their performance.

Project Structure:
factorial_main.py: Main program to calculate factorial using Python, NumPy, and Cython implementations.
factorial_operation.py: Module containing functions for factorial calculations.
factorial_cython.pyx: Cython module for accelerated factorial calculation.
setup.py: Script for compiling the Cython module.


Usage:
1.Install Cython:
pip install Cython
2.Compile the Cython module:
python setup.py build_ext --inplace
3.Run the main program:
python factorial_main.py


Results:
The program displays the factorial values and the time taken for each implementation:

Factorial using Python: [Factorial Value], Time taken: [Time] seconds
Factorial using NumPy: [Factorial Value], Time taken: [Time] seconds
Factorial using Cython: [Factorial Value], Time taken: [Time] seconds

