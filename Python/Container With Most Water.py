class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            water = width * h
            max_water = max(max_water, water)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water


if __name__ == "__main__":
    obj=Solution()
    height=[2,3,10,5,7,8,9]
    Op=obj.maxArea(height)
    print(Op)
