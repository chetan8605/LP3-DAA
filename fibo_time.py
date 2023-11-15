import time

# Non-recursive Fibonacci
def fib_non_recursive(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

# Recursive Fibonacci
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

# Time and space complexity analysis function
def analyze_complexity(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time

    space_complexity = len(str(result))  # Assuming space complexity is related to the size of the result

    return execution_time, space_complexity

# User input
n = int(input("Enter the value of n: "))

# Non-recursive analysis
non_recursive_time, non_recursive_space = analyze_complexity(fib_non_recursive, n)
print(f"Non-recursive Fibonacci: {fib_non_recursive(n)}")
print(f"Time complexity: {non_recursive_time} seconds")
print(f"Space complexity: {non_recursive_space} units")

# Recursive analysis
recursive_time, recursive_space = analyze_complexity(fib_recursive, n)
print(f"Recursive Fibonacci: {fib_recursive(n)}")
print(f"Time complexity: {recursive_time} seconds")
print(f"Space complexity: {recursive_space} units")