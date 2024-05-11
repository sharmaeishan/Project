# square_root_op.py

import numpy as np

def calculate_square_root(numbers):
    if isinstance(numbers, int):
        numbers = [numbers]  # Convert single integer to a list
    roots = []
    for num in numbers:
        roots.append(np.sqrt(num))
    return roots
