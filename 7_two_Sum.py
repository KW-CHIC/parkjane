#두 수의 합 문제 P.173

def two_Sum(nums, target):
    for i in nums:
        another = target - i
        j = nums.index(i)
        if another in nums[j+1:]: #배열 nums에서 앞의 값 인덱스 뒤부터 찾도록 함. -> 배열 nums가 [3,3,4]이고 타깃이 6일 때 출력값이 [0,0]이 될 수 있기 때문 
            all_index = [nums.index(i),nums[j+1:].index(another)+(j+1)] #배열 nums에서 j+1번째부터 인덱스 0으로 시작이니까 (j+1) 더해줘야 함!
            print(all_index)
            break


two_Sum([2,7,11,15], 9)
