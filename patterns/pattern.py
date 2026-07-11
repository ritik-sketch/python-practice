#number pattern 
'''
11111
22222
33333
44444
55555
'''
'''
def pattern1():
    for i in range(1, 6):        # Outer loop -> 1 से 5 तक (rows)
        for j in range(5):       # Inner loop -> हर row में 5 बार print
            print(i, end="")     # i की value print होगी
        print()                  # New line


pattern1()
'''

#12345
#12345
#12345
#12345
#12345
'''
def pattern2():
    for i in range(5):
        for j in range(1,6):
            print(j , end="")
        print()
pattern2()
'''

#1
#22
#333
#4444
#55555
'''
def pattern3():
    for i in range(1,6):
        for j in range(i):
            print(i, end="")
        print()
pattern3()
'''

#1
#12
#123
#1234
#12345
'''
def pattern4():
    for i in range(1,6):
        for j in range(1, i+1):
            print(j, end="")
        print()
pattern4()
'''

#    1 
#   1 2 
#  1 2 3 
# 1 2 3 4 
#1 2 3 4 5 

'''
def pattern5():
    for i in range(1,6):
        print(" " * (5 - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
pattern5()
'''

#    1                   
 #  2 2 
  #3 3 3 
 #4 4 4 4 
#5 5 5 5 5 
'''
def pattern6():
    for i in range(1, 6):
        print(" " * (5 - i), end="")
        for j in range(i):
            print(i, end=" ")
        print()
pattern6()
'''

#12345
#1234
#123
#12
#1

'''
def pattern7():
    for i in range(5,0,-1):
        for j in range(1, i +1):
            print(j, end="")
        print()
pattern7()
'''

#--------Pattern 8  ------------#  

#    1 
   # 2 3 
   # 4 5 6 
   # 7 8 9 10 
   # 11 12 13 14 15 
'''
def pattern8():
    count = 1
    for i in range(1,6):
        for j in range(i):
            print(count , end=" ")
            count = count + 1
        print()
pattern8()
'''


#------ Pattern 9             
'''
   # 5 4 3 2 1 
    # 5 4 3 2 
     # 5 4 3 
      # 5 4 
       # 5

def pattern9():
    for i in range(5, 0, -1):
        print(" " *(5 - i), end="")
        for j in range(5,5 - i, -1):
            print(j, end=" ")
        print()
pattern9()'''



## Pattern 10            

#     1 2 3 4 5 
#      2 3 4 5 
 #      3 4 5 
  #      4 5 
   #      5
'''
def pattern10():
	for i in range(1,6):
		print(" " * (i - 1), end="")
		for j in range(i,6):
			print(j, end=" ")
		print()
pattern10()	 
'''

#Pattern 11  ---------------                  

  #           1 
   #        2 1 
    #     3 2 1 
     #  4 3 2 1 
     #5 4 3 2 1
'''
def pattern11():
    for i in range(1,6):
        print(" " * (i - 1), end="")
        for j in range(i, 0 , -1):
            print(j, end=" ")
        print()
pattern11()
	 
'''

#Pattern 12
  #          1
  #        2 1 2
   #     3 2 1 2 3
  #    4 3 2 1 2 3 4
   # 5 4 3 2 1 2 3 4 5
'''
def pattern12():
    for i in range(1, 6):
        # Spaces
        print("  " * (5 - i), end="")
        
        # First half: numbers decreasing to 1
        for j in range(i, 0, -1):
            print(j, end=" ")
        
        # Second half: numbers increasing from 2
        for j in range(2, i + 1):
            print(j, end=" ")
        
        print()
pattern12()
'''

#Pattern 13
#          1
#          0 1
#          1 0 1
#          0 1 0 1
#          1 0 1 0 1
'''
def pattern13():
    for i in range(1, 6):
        for j in range(1, i + 1):
            if (i + j) % 2 == 0:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()
pattern13()
'''

#Pattern 14
#      1 2 3 4 5
#        2 3 4 5
#          3 4 5
#            4 5
#              5
#            4 5
#          3 4 5
#        2 3 4 5
#      1 2 3 4 5

'''
def pattern14():
    # Top half
    for i in range(1, 6):
        print("  " * (i - 1), end="")
        for j in range(i, 6):
            print(j, end=" ")
        print()
    
    # Bottom half
    for i in range(4, 0, -1):
        print("  " * (i - 1), end="")
        for j in range(i, 6):
            print(j, end=" ")
        print()
pattern14()
'''

#Pattern 15
#          1
#        1 1
#      1 2 1
#    1 3 3 1
'''
def pattern15():
    from math import factorial

    for i in range(5):
        # Print spaces for alignment
        print("  " * (5 - i), end="")
        
        # Calculate and print binomial coefficients
        for j in range(i + 1):
            # nCr = n! / (r! * (n-r)!)
            nCr = factorial(i) // (factorial(j) * factorial(i - j))
            print(nCr, end="   ")
        print()
pattern15()
'''

#Pattern 16
#      1
#      1 2
 #     1 2 3
  #    1 2 3 4
   #   1 2 3 4 5
     # 1 2 3 4
      #1 2 3
      #1 2
      #1
'''
def pattern16():
    # Top half
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    
    # Bottom half
    for i in range(4, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
pattern16()
'''

#Pattern 17
#      123456
#      234561
#      345612
#      456123
#      561234
#      612345

'''
def pattern17():
    nums = [1, 2, 3, 4, 5, 6]
    for _ in range(6):
        for num in nums:
            print(num, end="")
        print()
        
        # Shift the list
        first = nums.pop(0)
        nums.append(first)
pattern17()
'''

#Pattern 18
#      1
#      2 6
#      3 7 10
#      4 8 11 13
#      5 9 12 14 15

'''
def pattern18():
    for i in range(1,6):
        start_num = i 
        diff = 4
        for j in range(i):
            print(start_num, end=" ")
            start_num += diff
            diff -= 1
        print()
pattern18()
'''


#Pattern 19
#      10101
  #    01010
  #    10101
  #    01010
   #   10101

'''
def pattern19():
    for i in range(1, 6):
        if i % 2 != 0:  # Odd row
            start = 1
        else:  # Even row
            start = 0
            
        for _ in range(5):
            print(start, end="")
            start = 1 - start # Toggle between 0 and 1
        print()
pattern19()
'''


#Pattern 20
 #     1
 #     1 2 1
  #    1 2 3 2 1
   #   1 2 3 4 3 2 1
#      1 2 3 4 5 4 3 2 1

def pattern20():
    for i in range(1, 6):
        # First half (increasing numbers)
        for j in range(1, i + 1):
            print(j, end=" ")
            
        # Second half (decreasing numbers)
        for k in range(i - 1, 0, -1):
            print(k, end=" ")
            
        print()
pattern20()
