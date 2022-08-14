#n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.


def pair_sum(nums):
  sum=0
  nums.sort()
  
  for i, j in enumerate(nums):
    if i%2 == 0:
      sum+=j
  return sum

print(pair_sum([1,4,3,2]))
