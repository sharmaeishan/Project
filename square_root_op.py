# square_root_op.py

def calculate_square_root(numbers):
    if isinstance(numbers, int):
        numbers = [numbers]  # Convert single integer to a list
    roots = []
    for num in numbers:
        roots.append(num**0.5)
    return roots
