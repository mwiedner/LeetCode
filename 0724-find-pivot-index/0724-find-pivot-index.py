class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        totalSum = 0

        for number in nums:
            totalSum += number

        leftSum = 0
        rightSum = totalSum
        answer = -1

        print("Total Sum: " + str(totalSum))
        print()

        i=0
        while i < len(nums):
            rightSum -= nums[i]
            print("Left: " + str(leftSum))
            print("Right: " + str(rightSum))
            print("Index: " + str(i))
            print()
            if leftSum == rightSum:
                answer = i
                break
            leftSum += nums[i]
            i+=1
        return answer