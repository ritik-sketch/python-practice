def selectionsort(arr):
    n = len(arr)
    for i in range(n):
        print(i+1,"pass",end="")
        min_index = i
        print("Current min is", arr[min_index])
        for j in range(i + 1, n):
            print("Current item under observation",arr[j])
            if arr[j] < arr[min_index]:
                print("Current item is less than min")
                min_index = j
                print("Now the min has become", arr[min_index])
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(arr)
    return arr

arr = [8,9,1,3,5]
print(selectionsort(arr))






