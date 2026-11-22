from typing import List, Tuple


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]

    def findMinMax(self, nums: List[int]) -> Tuple[int, int]:
        minimum = min(nums)
        maximum = max(nums)

        return minimum, maximum


s = Solution()

arr = [3, 2, 1, 5, 6, 4]

print("Kth Largest:", s.findKthLargest(arr, 2))
print("Min-Max:", s.findMinMax(arr))