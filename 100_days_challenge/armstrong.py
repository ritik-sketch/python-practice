num = 153 
total= 0 
n = num
digits = len(str(num))

while n > 0:
    digit = n % 10
    total += digit ** digits
    n //= 10
if total == num:
    print("armstrong")
else:
    print("not armstrong")
print(num)



def armstrong(num):
    sum = 0
    digitss = len(str(num))
    n = num
    while n:
        sum += (n % 10) ** digits
        n //= 10
    return sum == num 
print(armstrong(153))