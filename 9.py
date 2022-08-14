#배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.

#투 포인터

nums = [-1, 0, 1, 2, -1, -4]

def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums)-2):
        #중복값 건너뜀
        if i>0 and nums[i] == nums[i-1]:
            continue
        #i의 다음 지점을 left, 마지막 지점을 right로 
        left = i+1
        right = len(nums)-1

        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            #투 포인터가 간격 좁혀나가면서 합(sum) 계산
            if sum < 0:
                left += 1
            elif sum >0 :
                right -= 1
            else:
                #출력결과 및 스킵 처리
                result.append([nums[i], nums[left], nums[right]])

                while left<right and nums[left] == nums[left+1]:
                    left+=1
                while left<right and nums[right] == nums[right-1]:
                    right-=1
                left += 1
                right -= 1
    return result
