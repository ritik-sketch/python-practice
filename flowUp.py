'''
a=[3,4,1,1,7] #create a array
print(a)

a1=[] #create a blank array 
for item in a:
	a1.append(item) # and append the all value from aar [a]

for item in a1:    
    print(item + 1)  # +1 is liye kyu ki hme sbki value us num se jada print krani h 1 replce with 2 , 2 replace with 3 
'''


'''

a=[3,4,1,1,7]

#bubble sort

n=len(a)
for i in range(n):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1],a[j]
print(a)


#[3,4,1,1,7]

i=0
   j=0 [3,4,1,1,7] j=0 (3) j+1=(4) loop ke hisab se a[j] > a[j+1] it means 3<4 = right so output no change 

   j=1  [3,1,4,1,7] because 4<1= false ,so the swaping is max to min 
   j=2  [3,1,1,4,7]  because 4<1 = false then swap value 
   j=3  [3,1,1,4,7] no change because 4<7= True

now move to -- 
i=1
   j=0  [1,3,1,4,7]  because 3<1= fqlse then swap the value 
   j=1  [1,1,3,4,7]  because now again 3<1=false thne value swap 
   j=2  [1,1,3,4,7]  output no change because 3<4=True
   j=3  [1,1,3,4,7]  because condition is full fill 

i=2
   
   j=0  [1,1,3,4,7]  no change because value equal hai 
   j=1  [1,1,3,4,7]  no change because condition is full fill 
   j=2  [1,1,3,4,7]  no change because value full fil

'''

#selection sort 
'''
a=[3,4,1,1,7]

n=len(a)

for i in range(n):
    min_idx=i
    for j in range(i+1,n):
        if a[j]<a[min_idx]:
            a[j], a[min_idx]=a[min_idx] , a[j]
print(a)


#[3,4,1,1,7]

i=0
   j=1   arr j[1]=4 arr[min_idx]=4 4>3 - min
   [3,4,1,1,7]
   j=1
   '''