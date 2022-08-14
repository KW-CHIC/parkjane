def except_self(nums):
    result = []
    j = 1
    for i in range(0, len(nums)):
        result.append(j)
        j=j*nums[i]
    j=1

    for i in range(len(nums)-1, 0-1, -1):
        result[i] = result[i] * j
        j=j*nums[i]
return result
