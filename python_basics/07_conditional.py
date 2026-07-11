age = 10

if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")

marks = 76

if marks >= 75:
    print("pass")
    res = "first division"
elif marks >= 40:
    print("pass with grace")
    res = "second division"
else:
    print("fail")
    res = "fail"

print(f"result :{res}")