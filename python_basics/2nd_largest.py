def secondLargest(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    return numbers[-2]
numbers = [1,3,2,4,4,5,6,6]
print (secondLargest(numbers))
