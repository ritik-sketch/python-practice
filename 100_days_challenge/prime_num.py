num = 7
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
print("Prime" if is_prime else "Not Prime")



num = 78
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

print("Prime" if is_prime else "Not Prime")



def prime(num):
    if num <= 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
            return False
        return True
print(prime(88))
        