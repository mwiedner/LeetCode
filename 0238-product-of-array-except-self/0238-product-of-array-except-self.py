class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []

        regProd = 1

        i = 0
        while i < len(nums):
            regProd *= nums[i]
            i+=1

        i = 0
        while i < len(nums):
            if nums[i] == 1:
                answer.append(regProd)
            elif nums[i] == -1:
                answer.append(regProd * -1)
            else:
                product = 1
                j = 0
                while j < len(nums):
                    if j != i:
                        product*= nums[j]
                    j+=1
                answer.append(product)
            i+=1
        return answer