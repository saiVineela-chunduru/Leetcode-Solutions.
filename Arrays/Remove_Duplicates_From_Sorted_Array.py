
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k








Input: nums = [1, 1, 2, 2, 3]

Output: 3

Modified array: [1, 2, 3, _, _]





Time complexity: O(n)



Space complexity: O(1)
