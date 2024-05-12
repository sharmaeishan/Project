# square_root_cython.pyx


cpdef int calculate_square_root_cython(int number):
    cdef int root = 0
    cdef int i
    for i in range(number + 1):
        if i * i == number:
            root = i
            break
        elif i * i > number:
            break
    return root

