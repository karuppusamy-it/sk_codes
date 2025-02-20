class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  
        n = len(nums)

        # 1st element 
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue  # Same as previous so can skip. 

            # Looking for 2nd and 3rd elements
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                # Success
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # Search for last repeat left pointer. 
                    while left < right and nums[left] == nums[left + 1]: 
                        left += 1  
                    # Search for last repeat right pointer
                    while left < right and nums[right] == nums[right - 1]: 
                        right -= 1  

                    # Shrink window
                    left += 1
                    right -= 1

                elif total < 0: left += 1 # Need more
                else: right -= 1 # Need less

        return res