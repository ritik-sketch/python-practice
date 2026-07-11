def star(n):
    for i in range(n):

        spaces = ' ' * (n - i - 1)

        stars = '*' * (2 * i + 1)

        print(spaces + stars)
star(3)

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b