#높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.

#투 포인터

def trap(height):
    volume = 0
    left, right = 0, len(height)-1
    left_max, right_max = height[left], height[right]
    
    
    while left < right:
        if left_max <= right_max :
            volume += left_max - height[left]
            left += 1
            left_max = max(left_max, height[left])
        else :
            volume += right_max - height[right]
            right -= 1
            right_max = max(right_max, height[right])
            
    return volume

print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
