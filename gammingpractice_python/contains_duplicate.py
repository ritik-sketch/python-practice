def contains_duplicate(nums):
  for i in range(len(nums)):
    for j in range(i+1 , len(nums)):
      if nums[i] == nums[j]:
        return True
  return False  
print(contains_duplicate([1,2,3,4]))


def contains_duplicate_set(nums):
  beg = set()
  for x in nums:
    if x in beg:
      return True
    beg.add(x)
  return False 
print(contains_duplicate_set([11,11]))
    