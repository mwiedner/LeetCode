class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        sum = 0

        flowerbed.insert(0,0)

        i = 0
        while i < len(flowerbed):
            if  i+2 < len(flowerbed):
                if flowerbed[i] == 0:
                    if flowerbed[i+1] == 0 and flowerbed[i+2] == 0:
                        sum+=1
                        flowerbed[i+1] = 1
            i+=1
        
        if flowerbed[len(flowerbed) - 2] == 0 and flowerbed[len(flowerbed)-1] == 0:
            sum+=1


        print(sum)

        if n <= sum:
            return True
        return False