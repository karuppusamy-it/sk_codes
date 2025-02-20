class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= 2 or len(nums2) <= 2:
            return self._median(sorted(nums1 + nums2))
        nums_to_remove = (min(len(nums1), len(nums2)) - 1) // 2
        if self._median(nums1) >= self._median(nums2):
            return self.findMedianSortedArrays(nums1[:-nums_to_remove], nums2[nums_to_remove:])
        else:
            return self.findMedianSortedArrays(nums1[nums_to_remove:], nums2[:-nums_to_remove])


    def _median(self, nums):
            if len(nums) % 2 == 0:
                return (nums[len(nums)//2 - 1] + nums[len(nums)//2]) / 2
            else:
                return nums[len(nums)//2]