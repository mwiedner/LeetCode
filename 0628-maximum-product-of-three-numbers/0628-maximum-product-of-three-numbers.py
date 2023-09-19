class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort(reverse=True)

        num1 = nums[0]

        if (num1 < 0):
            num2 = nums[1]
            num3 = nums[2]
            return num1 * num2 * num3

        if (nums[len(nums) - 1] * nums[len(nums) - 2]) > (nums[1] * nums[2]):
            num2 = nums[len(nums) - 1]
            num3 = nums[len(nums) - 2]
        else:
            num2 = nums[1]
            num3 = nums[2]

        print(num1)
        print(num2)
        print(num3)
        
        product = num1 * num2 * num3
        return product