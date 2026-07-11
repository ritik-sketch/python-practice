'''
def fibonacci(n):
    a,b = 4,30
    fib = []
    for _ in range(n):
        fib.append(a)
        a,b = b, a+b
    return fib
print(fibonacci(8))


n= 12
a,b = 22,88
fib = []
for _ in range(n):
    fib.append(a)
    a,b = b , a+b
print(fib)

'''
'''
def fibonacci(n):
    a, b = 4, 30
    fib = []

    # To set a breakpoint here, click in the margin next to this line.
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
    return fib

print(fibonacci(8))
'''


n = 12
a, b = 22, 88
fib = []

# To set a second breakpoint here, click in the margin next to this line.
for _ in range(n):
    fib.append(a)
    a, b = b, a + b
    
print(fib)