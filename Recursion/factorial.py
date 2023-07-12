
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def factorial_iterative(n):
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result

print(factorial(5))
print(factorial_iterative(5))