# factorial_cython.pyx
def factorial_cython_impl(int n):
    
    if n == 0:
        return 1
    else:
        return n * factorial_cython_impl(n-1)
