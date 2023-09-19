class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)

        ExpectedSum = ((length - 1) / 2) * length
        ExpectedSum += length
        print("Expected Sum: " + str(ExpectedSum))

        sum = 0

        for numbaz in nums:
            sum += numbaz

        diff = ExpectedSum - sum
        print("Sum: " + str(sum))
        print("Diff: " + str(diff))

        # Case if 0 is missing
        if diff < 0:
            return 0
        # Case if nothing is missing
        elif diff == 1 and ExpectedSum == length:
            return length
        elif length == 1 and diff == 0:
            return 0
        elif diff == 0 and ExpectedSum == length:
            return 1
        else:
            return diff