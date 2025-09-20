import time


#
# Time complexity = O(2^n)
#
def fib1(n):
    if n <= 1:
        return n

    return fib1(n - 1) + fib1(n - 2)


#
# Using the memoization technique
# Time complexity = O(n)
#
def fib2(n, computed={0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib2(n - 1, computed) + fib2(n - 2, computed)

    return computed[n]


if __name__ == "__main__":
    t_01 = time.time()
    fib1(40)
    t_02 = time.time()

    print(f"Execution without memoization: {t_02 - t_01}")  # 8 seconds

    t_11 = time.time()
    fib2(40)
    t_12 = time.time()

    print(f"Execution with memoization: {t_12 - t_11}")  # 3 * 10^(-5) seconds
