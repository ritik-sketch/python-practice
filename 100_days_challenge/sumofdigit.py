num = 123 
sum_digits = 0 
while num > 0:
    digit = num % 10   #last digit 
    sum_digits += digit   #add sum 
    num //= 10   #remove last digit 
print(sum_digits)



def sum_digit(n):
    total = 0 
    while n:
        total += n % 10 
        n //= 10
    return total 
print(sum_digit(234))