import time
import square_root_op
from square_root_cython import calculate_square_root_cython


# Without Cython
start_time= time.perf_counter_ns()
square_roots = square_root_op.calculate_square_root(64)
end_time= time.perf_counter_ns()
python_time = end_time - start_time
print("Square Roots (Without Cython):", square_roots)
print(python_time)

    
# With Cython
start_time= time.perf_counter_ns()
square_roots_cython = calculate_square_root_cython(64)
end_time= time.perf_counter_ns()
cython_time = end_time - start_time
print("Square Roots (With Cython):", square_roots_cython)
print(cython_time)



    
