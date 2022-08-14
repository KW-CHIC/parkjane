def pair_sum(nums):
  sum=0
  nums.sort(0)
  
  for i, j in enumerate(nums):
    if i%2 == 0:
      sum+=j
  return sum
