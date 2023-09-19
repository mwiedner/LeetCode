# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

import math

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        att = int(math.ceil(n / 2))
        check = guess(att)
        ceiling = n
        floor = 0

        midpoint = lambda x, y: (x + y) / 2

        while check != 0 :
            print(att)
            print("Check: " + str(check))
            if ceiling - floor == 1:
                print("HELLOOOO")
                if guess(ceiling) == 0:
                    return ceiling
                elif guess(floor) == 0:
                    return floor
            elif check == 1:
                print("too low")
                floor = att
                att = midpoint(att, ceiling)
                check = guess(att)
            elif check == -1:
                print("too high")
                ceiling = att
                att = midpoint(att, floor)
                check = guess(att)

        return att