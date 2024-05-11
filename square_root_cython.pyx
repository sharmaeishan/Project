# square_root_cython.pyx


import numpy as np
cimport numpy as np

cpdef int calculate_square_root_cython(int number):
    cdef int root = int(np.sqrt(number))
    return root

