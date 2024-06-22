def factorial(n):
    if n > 0:
        return n * factorial(n - 1)  # n! = n * (n-1)!
    else:  # n = 0
        return 1
    
output = factorial(5);
print(output)