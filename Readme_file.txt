Project: Square Root Calculation

Overview:
This project demonstrates the calculation of square roots using Python's NumPy library and a user-defined function. The code is organized into separate modules for modularity, and Cython is used to optimize the square root calculation for improved performance.

Modules:
1. main.py: Main program that calculates square roots using NumPy, a user-defined function, and Cython optimization.
2. square_root_op.py: Contains the user-defined functions for square root calculation using NumPy.
3. square_root_cython.pyx: Cython module for optimized square root calculation.
4. setup.py: Script to build the Cython module.

Usage:
1. Modify the numbers list in main.py to calculate square roots for different inputs.
2. Run main.py to compare the time taken for square root calculation with and without Cython optimization.

Instructions:
1. Ensure Python and Cython are installed on your system.
2. Compile the Cython module using the command: python setup.py build_ext --inplace
3. Run main.py to execute the square root calculation code and compare the performance between Python and Cython versions.
