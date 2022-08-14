#배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.

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

print(except_self([1,2,3,4]))
