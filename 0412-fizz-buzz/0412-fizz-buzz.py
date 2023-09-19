class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        nums = []

        i = 1
        while i <= n:
            if i % 3 == 0 and i % 5 == 0:
                nums.append("FizzBuzz")
            elif i % 3 == 0:
                nums.append("Fizz")
            elif i % 5 == 0:
                nums.append("Buzz")
            else:
                nums.append(str(i))
            i+=1
        return nums