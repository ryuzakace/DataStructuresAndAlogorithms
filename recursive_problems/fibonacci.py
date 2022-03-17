'''
1, 1, 2, 3, 5, 8, 13....
'''
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(int(input())))
