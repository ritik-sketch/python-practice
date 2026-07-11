'''
num = 1234  # original number hai
rev = 0   #hm empty reverse se suru krenge 

while num > 0 :  # loop tab tak chalega jb tak num zero n ho jaye 
    digit = num % 10 #last digit lena h num % 10 = 4 ho jyega 
    
    
    rev = rev * 10 + digit  # abhi reverse zero hai to hm 0 *10+4 kreng to rev me ab zero ki jagh 4 hoga 
    # Next iteration:
    # digit = 3, rev = 4*10+3 = 43, num=12
    # digit = 2, rev = 43*10+2 = 432, num=1
    # digit = 1, rev = 432*10+1 = 4321, num=0
    num = num // 10 # fir ab last digit remove kreng to 1234 // 10 = 123 bachega 
print(rev)


num = 4321   #original number hoga jise hme reverse krna hoga 
rev = 0      # ek rev variable define kreng jiski value zero hogi operation se pahle tk aur operation hone par ek ek digit aate jayeng isme 
while num > 0 :   # while loop chalaya jb tak numzero se bada hai operation hi tbhi hoga simple bat 
   digit = num % 10  # jab zero se number bada h to hm num % 10 kr denge last digit nikalne ke liye to  4321 % 10 = 1
   rev = rev * 10 + digit  # rev jo variable bnaya th uski value abho zero hi to ab rev 0*10+1 = 1
   num = num // 10 # last digit hta rhe 4321 // 10 = 432
print(rev)

def reverse(num):
    digit = num % 10
    rev = rev * 10 +1
    num = num // 10
num = 4321
rev = str(num)[::-1]
print(int(rev))

'''


##########################################

#reverse a string #0(N)

'''

S = "ritik"
rev = " "
for ch in S:  #pahle loop left to right chalega 
    rev = ch + rev    
    # pehle h -> rev="r"
                         # phir i -> "ir"
                         # phir t -> "tir"
                         # phir i -> "itir"
                         # phir k -> "kitir"
print(rev)  
'''


#with function 



''' 
def string(s):
    rev = ' '
    for ch in s:
        rev = ch + rev
    return rev 
print(string("anjali"))

'''



#with function 
'''
def rev(num):
    rev = 0 
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev 
print(rev(943689841))


n = 9999888888777777666666666655555555444444444333333222222211111111000000000
rev = 0 
while n > 0 :
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print(rev)
'''

def string(s):
    rev = ' '
    for ch in s:
        rev = ch + rev
    return rev 
print(string("ilajna"))


def string(s):
    rev = ' '
    for ch in s:
        rev = ch + rev 
    return rev 
print(string("ddhhhhqhldql"))



def string(s):
    rev = ' '
    for ch in s:
        rev = ch + rev
    return rev 
print(string("yeh"))